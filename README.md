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

TBD, but the place to look is `scripts/alpha_complex_persistent_homology.py`.


References
==========

 - Math background and survey of software packages: https://arxiv.org/pdf/1506.08903.pdf

 - helpful: http://www.dyinglovegrape.com/math/topology_data_1.php
 < follows http://www.ams.org/journals/bull/2009-46-02/S0273-0979-09-01249-X/S0273-0979-09-01249-X.pdf

 - a textbook: http://www.math.cornell.edu/~hatcher/AT/AT.pdf
 - "accessible" textbook, Munkres: http://webmath2.unito.it/paginepersonali/sergio.console/Dispense/Elements%20of%20Algebraic%20Topology%20-%20James%20R.%20Munkres.pdf

 - interesting overview of Rips, and feasible approximation: https://arxiv.org/pdf/1203.6786.pdf
 < by http://donsheehy.net/
 < visualized? http://donsheehy.net/cavanna15visualizing.html
 < nerve of cones: http://donsheehy.net/research/cavanna15geometric.pdf

 - net-trees:
 < original http://sarielhp.org/p/04/lipschitz/lipschitz.pdf
 < slides http://sarielhp.org/p/04/lipschitz/lips_slides.pdf
 < sheehy explains http://donsheehy.net/research/jahanseir15cover.pdf