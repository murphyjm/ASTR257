**********
Installing
**********

Here are some notes on installing
packages useful for ASTR 257.
This is mainly a listing.

Python 3.7
==========

We strongly recommend installing with Anaconda.
Detailed installation instructions are provided
by that package.

We will assume that your package includes
`matplotlib`, `numpy`, `scipy`, and `astropy`.

ASTR 257
========

This repository can only be obtained via GitHub.
It is best that you clone the repository and
then do a `develop` installation.::

    cd <to where you want the Repo>
    git clone https://github.com/askemer/ASTR257.git
    cd ASTR257
    python setup.py develop

That will push the code into your environment.
And if you need to update the repo later
(with a `git pull` command), the changes will
be immediately visible to you.

Additional Packages
===================

Here is a listing of pacakges you are likely to
use in ASTR 257.

We recommend that you use `Anaconda <https://www.continuum.io/downloads/>`_
to install and/or update these packages.

* `photutils <https://photutils.readthedocs.io/en/stable/>`_ version 0.7
* `ginga <https://github.com/ejeschke/ginga>`_ version 2.7.2 or later

If you are using Anaconda, you can check the presence of these packages with::

	conda list "^python|numpy|astropy|scipy|matplotlib|photutils"

If the packages have been installed, this command should print
out all the packages and their version numbers.

If any of these packages are missing you can install them
with a command like::

	conda install astropy
	or
	pip install photutils

If any of the packages are out of date, they can be updated
with a command like::

	conda update scipy


