""" Several, hopefully useful methods for image viewing, processing, etc."""

import subprocess
import time
import warnings

from astropy.io import fits

# Ginga
try:
    from ginga.util import grc
except:
    flg_ginga = False
else:
    flg_ginga = True


def connect_to_ginga(host='localhost', port=9000, raise_err=False, allow_new=False):
    """
    Connect to a RC Ginga.

    Args:
        host (:obj:`str`, optional):
            Host name.
        port (:obj:`int`, optional):
            Probably should remain at 9000
        raise_err (:obj:`bool`, optional):
            Raise an error if no connection is made, otherwise just
            raise a warning and continue
        allow_new (:obj:`bool`, optional):
            Allow a subprocess to be called to execute a new ginga
            viewer if one is not already running.

    Returns:
        RemoteClient: connection to ginga viewer.
    """
    if not flg_ginga:
        warnings.warn('You must install ginga before using this method')
        return
    # Start
    viewer = grc.RemoteClient(host, port)
    # Test
    ginga = viewer.shell()
    try:
        tmp = ginga.get_current_workspace()
    except:
        if allow_new:
            subprocess.Popen(['ginga', '--modules=RC'])
            time.sleep(3)
            return grc.RemoteClient(host, port)

        if raise_err:
            raise ValueError
        else:
            warnings.warn('Problem connecting to Ginga.  Launch an RC Ginga viewer and '
                      'then continue: \n    ginga --modules=RC')

    # Return
    return viewer

def view_in_ginga(img, exten=0, clear=False, chname='Image'):
    """  Display an image in the Ginga viewer

    Modified from ginga.show_image() in PypeIt

    Args:
        img (img or np.ndarray:
        exten:

    Returns:

    """

    if not flg_ginga:
        warnings.warn('You must install ginga before using this method')
        return

    # Read or set the image data.  This will fail if the input is a
    # string and astropy.io.fits cannot read the image.
    img = fits.open(img)[exten].data if isinstance(img, str) else img


    # Instantiate viewer
    viewer = connect_to_ginga()
    if clear:
        # Clear existing channels
        shell = viewer.shell()
        chnames = shell.get_channel_names()
        for ch in chnames:
            shell.delete_channel(ch)
    ch = viewer.channel(chname)

    # Header
    header = {}
    header['NAXIS1'] = img.shape[1]
    header['NAXIS2'] = img.shape[0]

    # Giddy up
    ch.load_np(chname, img, 'fits', header)
    canvas = viewer.canvas(ch._chname)

    # Giddy up
    ch.load_np(chname, img, 'fits', header)
    canvas = viewer.canvas(ch._chname)

    # These commands set up the viewer. They can be found at
    # ginga/ginga/ImageView.py
    out = canvas.clear()
    out = ch.set_color_map('ramp')
    out = ch.set_intensity_map('ramp')
    out = ch.set_color_algorithm('linear')
    out = ch.restore_contrast()
    out = ch.restore_cmap()

