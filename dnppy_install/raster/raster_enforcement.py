

__all__=['is_rast',         # complete
         'enf_rastlist']    # complete


def is_rast(filename):
    """ Verifies that input filenamecore.exists, and is of raster format"""

    import os
    
    rast_types=['bil','bip','bmp','bsq','dat','gif','img','jpg','jp2','png','tif',
                'BIL','BIP','BMP','BSQ','DAT','GIF','IMG','JPG','JP2','PNG','TIF']
    ext = filename[-3:]

    if os.path.isfile(filename):
        for rast_type in rast_types:
            if ext == rast_type:
                return(True)

    return(False)


def enf_rastlist(filelist):

    """
    ensures a list of inputs filepaths contains only valid raster tyeps
    """

    # first place the input through the same requirements of any filelist
    filelist        = core.enf_filelist(filelist)
    new_filelist    = []

    for filename in filelist:
        ext=filename[-3:]

        if os.path.isfile(filename):
            if is_rast(filename):
                new_filelist.append(filename)

    return(new_filelist)
