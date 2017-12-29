import numpy as np


def read_wishlists(filename):
    """Reads input files, assumes files are in the ./data subdirectory.
    
    Example
    child_wishlists = read_wishlists('child_wishlist_v2.csv')
    santa_wishlists = read_wishlists('gift_goodkids_v2.csv') 
    """    
    wishlists = []
    with open("data/{filename}".format(filename=filename)) as f:
        for l in f.readlines():
            wishlist = l.rstrip().split(',')
            wishlists.append(wishlist)
    return np.array(wishlists)[:,1:]