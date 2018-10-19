# D-RATS Renewed

This is hopefully the future home for D-RATS development. The system is being modernized to Python3 and will use the latest GTK library in python pygobject. This should give the D-RATS project a renewed lifespan on multiple platforms. Once we get the old code stable we can consider accepting feature requests.

# Description

 D-RATS is a communications tool for D-STAR amateur radio low-speed data
 (DV mode).
 It provides:
   Multi-user chat capabilities;
   File transfers
   Structured data transport (forms); and
   Position tracking and mapping.


## Installation instructions

Use the Debian Linux standard packaging tools, or run, according to
your system (from inside d-rats root source directory):

     $ cd libexec
     $ make
     $ make install
     $ cd ..
     $ python setup.py install --prefix=/usr/ --install-lib=/usr/lib/python2.7/dist-packages/

## Support

Support? We don't need no stinking support.

## Authors

Dan Smith (KK7DS)
Jonathan Kelley (N5IPT)
