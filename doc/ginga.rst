*****
Ginga
*****

Ginga is a Python based platform for image display.
It has much the same functionality as `ds9` but with
a considerably different look and feel.

Standard
========

As with other image viewers, you can load a FITS image
into ginga from the command line or via the GUI itself.
An example::

    ginga your_FITS_file.fits

Inside Python
=============

For debugging code related to data reduction
and image analysis, it is essential to be able to
display the image.  This is done in two steps with
Ginga.

Launch RC Ginga
---------------

You need to first launch a Remote Control version
of Ginga from the command line.  As so::

    ginga --modules=RC

A Ginga window will launch and you will see "RC" in
a tab in the upper right.

Wrapper to Ginga
----------------

We provide a simple wrapper to Ginga that faciliates
image viewing.  Here is how it goes::

    img = np.arange((100,100))
    from astr257 import img_utils
    # Do it
    img_utils.view_in_ginga(img)

Now check your RC Ginga window.



