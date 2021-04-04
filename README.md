
Help Mario to Get Out! BFS and A* algorithm comparision

Mario is trapped in a weird world so let's help him to get out from there.
Problem-solver agent design

The problem has three possible maps configuration:

easy 

[[inf,  -1, inf,   0],
 [inf, inf, inf,  -1],
 [inf,  -1, inf,  -1],
 [inf ,  -1, inf, inf]]
 
 medium 

[[inf, -1 , -1,  -1, -1, -1, inf, inf, inf, inf],
[inf, inf, inf, -1, -1, -1, inf, inf, inf, inf],
[inf, -1 , inf, -1, inf, inf, inf, inf, inf, inf],
[inf, -1 , inf, -1, inf, inf, -1, -1, -1, inf],
[inf, -1,  inf, inf, inf, inf, inf, -1, -1, inf],
[-1,  -1,  inf, inf, -1, -1, inf, inf, -1, inf],
[-1,  -1,  inf, inf, inf, inf, inf, inf, 0, inf],
[inf, inf, inf, -1, -1, -1, inf, inf, inf, inf],
[inf, inf, inf, inf, inf, -1, inf, inf, inf, -1],
[inf, inf, -1, -1, -1, -1, inf, inf, -1, -1]])

hard

[[inf, -1 , -1,  -1,  -1,  -1,  inf, inf, inf, -1, -1, inf, -1, -1, -1],
[inf, inf, inf, -1,  -1,  -1,  inf, inf, inf, -1, -1, -1, inf, -1, -1],
[inf, -1 , inf, -1,  inf, inf, inf, inf, inf, -1, -1, inf, inf, -1, -1],
[inf, -1 , inf, -1,  inf, inf, -1,  -1,  -1,  -1, inf, inf, inf, inf, inf],
[inf, -1,  inf, inf, inf, inf, inf, -1,  -1,  inf, inf, -1, inf, inf, inf],
[-1,  -1,  inf, inf, -1,  -1,  inf, -1, -1,  inf, inf, inf, inf, -1, -1],
[-1,  -1,  inf, inf, inf, inf, inf, inf,  -1,  inf, inf, inf, inf, -1, -1],
[inf, inf, inf, -1,  -1,  -1,  inf, inf, inf, inf, inf, -1, inf, inf, inf],
[-1,  inf, inf, inf, inf, -1,  inf, inf, inf, -1, inf, -1, inf, -1, -1],
[inf,  inf, -1,  -1,  -1,  -1,  inf, inf, -1, -1, inf, -1, inf, inf, inf],
[inf,  inf, -1,  -1,  -1,  -1,  inf, inf, -1, -1, inf, -1, inf, inf, inf],
[-1,  inf, -1,  -1,  -1,  -1,  -1, -1, -1, -1, inf, inf, inf, inf, -1],
[-1,  inf, -1,  -1,  -1,  -1,  -1, -1, -1, -1, -1, inf, inf, inf, inf],
[-1,  -1, -1,  -1,  -1,  -1,  -1, -1, -1, -1, inf, inf, -1, inf, inf],
[-1,  -1, -1,  -1,  -1,  -1,  -1, -1, -1, -1, inf, inf, -1, inf, 0]]


where the empty spaces are represented by inf; the spaces ocuped fort a wall by -1 and the pipes by 0

You can also select the algorithm you want to resolve the problem (BFS or A*)
It returns a map of the path where the algorithm has moved, and the branching factor.
With that information we can compare and verificate which algorithm is more efficient

Installation Guide

You need to have installed in your local machine:

python 3.7
numpy library

To run the project execute:

$python main.py
