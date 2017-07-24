Setting Up
==========

First, download GUDHI, one of the `.tar.gz`s on this page with
`python` in its name, save it in the `./gudhi` folder, and
exit `setup.sh` to make sure it knows it's there.

Make sure you follow the steps
[here](https://lists.gforge.inria.fr/pipermail/gudhi-contact/2017-May/000016.html)
which are annoying but necessary (unless the GUDHI people updated the
library).

Make sure that Boost, CGAL, Eigen, and optionally also Intel TBB are installed on your
system. On OS X, I was able to do this all with Homebrew:

    $ brew install boost cgal eigen tbb

Also, you need to be running Python>=3.6.

Then,

    $ . setup.sh

To test and see if everything worked, try

    $ python3 $GUDHI_PATH/example/alpha_complex_from_points_example.py

(note that `GUDHI_PATH` was set by `setup.sh`).


Usage
=====

TBD.