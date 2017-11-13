from scipy import spatial
import utils

import matplotlib.pyplot as plt
import numpy as np
import numpy.random as nrand


def load_data(dataset_path, ref_image_path, cifar_cat, show_dataset): 
    print('Reading dataset and ref image...')

    if cifar_cat == '':
        dataset = utils.load_coll_dataset(dataset_path)
    else:
        dataset = utils.load_cifar_dataset(dataset_path, cifar_cat)
    
    ref_image = utils.load_image_from_file(ref_image_path)

    print('Dataset size: {}'.format(dataset.shape[0]))
    print('Ref image shape: {}'.format(ref_image.shape[0:2]))
    
    if show_dataset:
        h, w, i = dataset[0].shape
        gallery = (dataset[0:100].reshape(10, 10, h, w, i)
                .swapaxes(1, 2)
                .reshape(h * 10, w * 10, i))
        plt.imshow(gallery)
        plt.show()

    return dataset, ref_image

def calc_grid_dimensions(dataset, ref_image, hor_count): 
    ref_aspect_ratio = ref_image.shape[1] / ref_image.shape[0]
    item_aspect_ratio = dataset.shape[2] / dataset.shape[1]

    ver_count = round(hor_count * item_aspect_ratio / ref_aspect_ratio)
    return hor_count, ver_count

def parse_args():
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Builds a mosaic-style grid for a picture')
    parser.add_argument('--dataset', default='data/colectie')
    parser.add_argument('path_to_image')
    parser.add_argument('output_path')
    parser.add_argument('--cifar_cat', default='')
    parser.add_argument('--hor_count', type=int, default=100)
    
    add_optional = lambda x: parser.add_argument(x, 
            action='store_const', const=True, default=False)
    
    add_optional('--quiet')
    add_optional('--place_random')
    add_optional('--choose_random')
    add_optional('--repeat_neighbors')
    add_optional('--hexagonal')
    add_optional('--shuffle')


    args = parser.parse_args()
    return args

def calc_sse(a, b):
    return np.sum((a - b)**2)

def main(args):

    dataset, ref_image = load_data(args.dataset, 
            args.path_to_image, args.cifar_cat, not args.quiet)
    hor_count, ver_count = calc_grid_dimensions(dataset, ref_image, args.hor_count)
   
    # Resize image
    item_dims = dataset.shape[1], dataset.shape[2]
    item_h, item_w = item_dims

    new_size = (ver_count * item_h, hor_count * item_w)
    ref_image = utils.resize_image(ref_image, new_size)
    image_h, image_w = new_size

    print('Resized image to: {}'.format(new_size))
    print('to fit item size: {}'.format(item_dims))

    print('Preparing...')

    if (args.hexagonal):
        region = utils.generate_hex(item_dims)
    else:
        region = utils.generate_rect(item_dims)
    
    mean_fn = lambda x: utils.calc_mean_color(x, region) 
    means = list(map(mean_fn, dataset))

    result = np.zeros(ref_image.shape, dtype=np.uint8)
    tree = spatial.KDTree(means)

    print('Computing...')
    
    # The number of pictures inserted
    lim = ver_count * hor_count
    # If random criterion is chosen, make more
    # to avoid having ugly holes
    if args.place_random:
        lim *= 5

    offsets = []
    if args.place_random:
        offsets = zip(nrand.randint(image_h - item_h, size=lim),
            nrand.randint(image_w - item_w, size=lim))
    else:
        if args.hexagonal: 
            X1, Y1 = np.mgrid[0:image_h:item_h, 0:image_w-item_w:2*item_w-item_h]
            X2, Y2 = np.mgrid[item_h//2:image_h-item_h:item_h, 
                    item_w-item_h//2:image_w-item_w:2*item_w-item_h]
            X = np.concatenate([X1.ravel(), X2.ravel()])
            Y = np.concatenate([Y1.ravel(), Y2.ravel()])
            offsets = zip(X.ravel(), Y.ravel())
        else:
            X, Y = np.mgrid[0:image_h:item_h, 0:image_w:item_w]
            offsets = zip(X.ravel(), Y.ravel())
   
    offsets = list(offsets)
    offsets.sort()
    mem = {}

    for x, y in offsets:
        offset = (x, y)
        seek = utils.calc_mean_color(ref_image, region, offset)

        best_pic = 0
        if args.choose_random:
            best_pic = nrand.randint(len(means))
        else:
            if (args.repeat_neighbors or args.place_random):
                best_pic = tree.query(seek)[1]
            else:
                # 4 NN's are always enough
                best_pics = tree.query(seek, 8)[1]
                if args.shuffle:
                    nrand.shuffle(best_pics)

                # Get the list of pics to avoid
                avoid = []
                if args.hexagonal:
                    deltas = [(-item_h, 0), (-item_h//2, item_h//2 - item_w),
                            (-item_h//2, -item_h//2 + item_w)]
                else:
                    deltas = [(-item_h, 0), (0, -item_w), (-item_h, -item_w)]

                for dx, dy in deltas:
                    lookup = x + dx, y + dy
                    avoid.append(mem.get(lookup, -1))
                
                # Get an idx which isn't already placed
                idx = 0
                while best_pics[idx] in avoid:
                    idx = idx + 1
                best_pic = best_pics[idx]

                # Memoization
                mem[offset] = best_pic


        result = utils.paint_region(result, 
                dataset[best_pic], region, offset)

    print('Writing result...')
    
    utils.save_result(result, args.output_path)

    print('Done! Check {} for result'.format(args.output_path))

if __name__ == '__main__':
    main(parse_args())
