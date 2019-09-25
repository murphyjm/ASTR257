import numpy as np
from astropy.stats import sigma_clipped_stats
from photutils import DAOStarFinder

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib import rcParams
rcParams["font.family"] = "serif"
rcParams["font.serif"] = "Times New Roman"
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = [r'\usepackage{amsmath} \usepackage{bm} \usepackage{physics}']
%config InlineBackend.figure_format = 'retina' # For high quality figures

def find_sources(data):
    mean, median, std = sigma_clipped_stats(data, sigma=3.0) # Background statistics
    
    # Adjust these params by hand/eye
    daofind = DAOStarFinder(fwhm=3.0, threshold=5.*std_v, sharplo=0.0, sharphi=0.5,
                            roundlo=-0.2, roundhi=0.2, peakmax=5e4, exclude_border=True)
    sources_v = daofind(ngc6819_v - median_v)
    for col in sources_v.colnames:
        sources_v[col].info.format = '%.8g'  # for consistent table output
    print(sources_v)
    return sources
