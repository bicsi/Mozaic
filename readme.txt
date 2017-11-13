----------------------------------------------
PROIECT 1 VEDERE ARTIFICIALA
Bicsi Lucian, grupa 235
----------------------------------------------

Proiectul a fost scris in Python 3, folosind
bibliotecile numpy, scipy (pentru operatii 
vectorizate rapide) si matplotlib (pentru
afisarea de grafice).


----------------------------------------------
Instructiuni de rulare:
----------------------------------------------

Pentru a rula proiectul, se va folosi comanda:

python3 main.py {calea imaginii de referinta}
    {calea imaginii output} [optiuni]

Pentru a afla optiunile cu care se poate rula,
folositi comanda:

python3 main.py -h

Rezultatele proiectului sunt grupate pe
subpuncte si se afla in directoare aferente.
Pentru a regenera rezultatele, se poate folosi
comanda:

./script.sh

----------------------------------------------
Cod sursa
----------------------------------------------

Algoritmul de baza se afla in fisierul main.py.

Exista totusi si cateva functii ajutatoare
(utilitare) implementate in fisierul utils.py.

----------------------------------------------
Note
----------------------------------------------

Fiecare folder are un fisier readme aferent,
care prezinta comentarii asupra subpunctului.

Folderele bonus_a si bonus_b reprezinta
rezultatele partii bonus a proiectului
(imagini hexagonale)

Folderul bonus_extra reprezinta o modalitate
diferita de a elimina pattern-urile regulate
din cadrul mozaicului, descrisa informal astfel:
   
   Pentru completarea unei celule in caroiaj,
   in loc sa se considere cea mai apropiata
   culoare medie, se va lua o poza aleatoare
   dintre cele mai bune K (K = 8) care nu
   este deja folosita in celule adiacente.

Din motive de versatilitate si performanta,
am ales sa folosesc structura KDTree din cadrul
bibliotecii scipy.spatial pentru a raspunde
rapid la query-uri de tip K-nearest-neighbor.
Aceasta mica modificare a facut ca o generare
cu --horizontal-count 100 sa se faca de
aproximativ 20 ori mai repede (~5s vs ~3m).
