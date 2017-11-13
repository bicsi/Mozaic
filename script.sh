
RUNA=python3\ main.py\ --quiet\ --repeat_neighbors
echo "Generating a"

$RUNA --hor_count=100 data/imaginiTest/liberty.jpg a/liberty100.jpg
$RUNA --hor_count=100 data/imaginiTest/adams.JPG a/adams100.jpg
$RUNA --hor_count=100 data/imaginiTest/romania.jpeg a/romania100.jpg
$RUNA --hor_count=100 data/imaginiTest/ferrari.jpeg a/ferrari100.jpg
$RUNA --hor_count=100 data/imaginiTest/tomJerry.jpeg a/tomJerry100.jpg
$RUNA --hor_count=100 data/imaginiTest/obama.jpeg a/obama100.jpg

$RUNA --hor_count=75 data/imaginiTest/liberty.jpg a/liberty75.jpg
$RUNA --hor_count=75 data/imaginiTest/adams.JPG a/adams75.jpg
$RUNA --hor_count=75 data/imaginiTest/romania.jpeg a/romania75.jpg
$RUNA --hor_count=75 data/imaginiTest/ferrari.jpeg a/ferrari75.jpg
$RUNA --hor_count=75 data/imaginiTest/tomJerry.jpeg a/tomJerry75.jpg
$RUNA --hor_count=75 data/imaginiTest/obama.jpeg a/obama75.jpg

$RUNA --hor_count=50 data/imaginiTest/liberty.jpg a/liberty50.jpg
$RUNA --hor_count=50 data/imaginiTest/adams.JPG a/adams50.jpg
$RUNA --hor_count=50 data/imaginiTest/romania.jpeg a/romania50.jpg
$RUNA --hor_count=50 data/imaginiTest/ferrari.jpeg a/ferrari50.jpg
$RUNA --hor_count=50 data/imaginiTest/tomJerry.jpeg a/tomJerry50.jpg
$RUNA --hor_count=50 data/imaginiTest/obama.jpeg a/obama50.jpg

$RUNA --hor_count=25 data/imaginiTest/liberty.jpg a/liberty25.jpg
$RUNA --hor_count=25 data/imaginiTest/adams.JPG a/adams25.jpg
$RUNA --hor_count=25 data/imaginiTest/romania.jpeg a/romania25.jpg
$RUNA --hor_count=25 data/imaginiTest/ferrari.jpeg a/ferrari25.jpg
$RUNA --hor_count=25 data/imaginiTest/tomJerry.jpeg a/tomJerry25.jpg
$RUNA --hor_count=25 data/imaginiTest/obama.jpeg a/obama25.jpg

RUNB=python3\ main.py\ --quiet\ --place_random\ --hexagon
echo "Generating b"

$RUNB data/imaginiTest/liberty.jpg b/liberty.jpg
$RUNB data/imaginiTest/adams.JPG b/adams.jpg
$RUNB data/imaginiTest/romania.jpeg b/romania.jpg
$RUNB data/imaginiTest/ferrari.jpeg b/ferrari.jpg
$RUNB data/imaginiTest/tomJerry.jpeg b/tomJerry.jpg
$RUNB data/imaginiTest/obama.jpeg b/obama.jpg

RUNC=python3\ main.py\ --quiet 
echo "Generating c"

$RUNC data/imaginiTest/liberty.jpg c/liberty.jpg
$RUNC data/imaginiTest/adams.JPG c/adams.jpg
$RUNC data/imaginiTest/romania.jpeg c/romania.jpg
$RUNC data/imaginiTest/ferrari.jpeg c/ferrari.jpg
$RUNC data/imaginiTest/tomJerry.jpeg c/tomJerry.jpg
$RUNC data/imaginiTest/obama.jpeg c/obama.jpg


RUND=python3\ main.py\ --quiet\ --dataset\ cifar-10-batches-py\ --hexagon\ --shuffle
echo "Generating d"

$RUND --cifar_cat automobile data/auto.png d/auto.jpg
$RUND --cifar_cat dog data/dog.jpg d/dog.jpg
$RUND --cifar_cat cat data/cat.jpg d/cat.jpg
$RUND --cifar_cat horse data/horse.jpg d/horse.jpg
$RUND --cifar_cat ship data/ship.jpg d/ship.jpg


RUNBA=python3\ main.py\ --quiet\ --hexagon\ --repeat_neighbors
echo "Generating bonus a"

$RUNBA data/imaginiTest/liberty.jpg bonus_a/liberty.jpg
$RUNBA data/imaginiTest/adams.JPG bonus_a/adams.jpg
$RUNBA data/imaginiTest/romania.jpeg bonus_a/romania.jpg
$RUNBA data/imaginiTest/ferrari.jpeg bonus_a/ferrari.jpg
$RUNBA data/imaginiTest/tomJerry.jpeg bonus_a/tomJerry.jpg
$RUNBA data/imaginiTest/obama.jpeg bonus_a/obama.jpg


RUNBB=python3\ main.py\ --quiet\ --hexagon
echo "Generating bonus b"

$RUNBA data/imaginiTest/liberty.jpg bonus_b/liberty.jpg
$RUNBA data/imaginiTest/adams.JPG bonus_b/adams.jpg
$RUNBA data/imaginiTest/romania.jpeg bonus_b/romania.jpg
$RUNBA data/imaginiTest/ferrari.jpeg bonus_b/ferrari.jpg
$RUNBA data/imaginiTest/tomJerry.jpeg bonus_b/tomJerry.jpg
$RUNBA data/imaginiTest/obama.jpeg bonus_b/obama.jpg

RUNBE=python3\ main.py\ --quiet\ --hexagon\ --shuffle
echo "Generating bonus extra"

$RUNBE data/imaginiTest/liberty.jpg bonus_extra/liberty.jpg
$RUNBE data/imaginiTest/adams.JPG bonus_extra/adams.jpg
$RUNBE data/imaginiTest/romania.jpeg bonus_extra/romania.jpg
$RUNBE data/imaginiTest/ferrari.jpeg bonus_extra/ferrari.jpg
$RUNBE data/imaginiTest/tomJerry.jpeg bonus_extra/tomJerry.jpg
$RUNBE data/imaginiTest/obama.jpeg bonus_extra/obama.jpg


