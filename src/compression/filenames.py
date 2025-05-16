
from .constants import COMPRESSION_SUFFIX



def split_suffix(filename, suffixes=()):
    tempname = filename.lower()
    if isinstance(tempname, bytes):
        tempname = tempname.decode()
    for suffix in sorted(suffixes, key=len, reverse=True):
        if isinstance(suffix, bytes):
            suffix = suffix.decode()
        if tempname.endswith(suffix):
            return filename[:-len(suffix)], filename[-len(suffix):]
    return filename, None



def strip_suffix(filename, suffixes=()):
    filename, suffix = split_suffix(filename, suffixes)
    return filename



def infer_compression_format(filename):
    """
    Infer from the filename extension the compression format used,
    or None.

    If passed a fileobj, returns None.
    """
    if isinstance(filename, (str, bytes)):
        tempname = filename.lower()
        if isinstance(tempname, bytes):
            tempname = tempname.decode()
        for fileformat in sorted(COMPRESSION_SUFFIX):
            if tempname.endswith(COMPRESSION_SUFFIX[fileformat]):
                return fileformat
    return None



def split_compression_suffix(filename):
    fileformat = infer_compression_format(filename)
    if fileformat is None:
        return filename, None
    else:
        return split_suffix(filename, COMPRESSION_SUFFIX[fileformat])



def strip_compression_suffix(filename):
    filename, suffix = split_compression_suffix(filename)
    return filename
