This fork of the original repository includes a python binding to use GDBSCAN (GPU optimized DBSCAN algorithm) with python, with native numpy support. It is also included a GDBSCAN version, named GDBSCAN_RT, which preallocates GPU memory, it still has some issues but it should save some time if the DBSCAN algorithm should be performed in real time.
You can find an example usage in ```gdbscan.py```, and the original readme below.

======

DBSCAN
======

dbscan.h - DBSCAN C++ Boost OpenMP implementation

dbscan_vp.h - DBSCAN vp tree kNN implementation using Eigen https://en.wikipedia.org/wiki/Vantage-point_tree

vp tree DBSCAN benchmark Intel(R) Xeon(R) CPU E5-2690 v2 @ 3.00GHz

![DBSCAN vptree benchmark](newplot.png?raw=true)
