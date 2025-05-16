# compression

## About

Open a gzip-/bgzip-/bzip2-/lzma-/xz-compressed file or uncompressed file
in binary or text mode.

The `filename` argument can be an actual filename (a str or bytes object), or
an existing file object to read from or write to. Use `"-"` to open a file
object to the appropriate stdin/stdout stream requested via mode. Serial
readling via HTTP and FTP URL file path is supported.

The `mode` argument can be `"r"`, `"rb"`, `"w"`, `"wb"`, `"x"`, `"xb"`, `"a"` or `"ab"` for
binary mode, or `"rt"`, `"wt"`, `"xt"` or `"at"` for text mode. The default mode is
`"rt"`. The default `compresslevel` for compression streams is 9.

For binary mode, the `encoding`, `errors`, and `newline` arguments must not be
provided.

For text mode, a compressed stream object is created, then wrapped in an
`io.TextIOWrapper` instance with the specified encoding, error handling
behavior, and line ending(s).

To read from/write to compressed streams from stdin/stdout or existing
file-like objects, the appropriate compression `open()` function object must
be passed via the `opener` attribute (e.g., `opener=gzip.open`). When writing
`compresslevel` must be set to a value between 1 and 9, inclusive (default
is 9).

This module relies on the `io`, `gzip`, `lzma`, `bz2`, `bz2file`, and `pysam` modules 
internally, but other can be supplied via the opener attribute, which must
return a callable object. `bz2file` is only required for Python versions 
earlier than 3.3.

See Also: `help(io.open)`


## Examples

```python3
from compression import open

# open a file for reading on the local file system:
infile = open("input.fastq.gz", mode='r')

# open a file for reading on a remote server via HTTP protocol
infile = open("http://path/to/remote/input.fastq.gz")

# open a file for reading/writing to STDIN/STDOUT stream. To read
# compressed files, must specify the `opener` attribute explicitly:
import gzip
from compression.constants import STDIO

infile = open(STDIO, mode='r', opener=gzip.open)

outfile = open(STDIO, mode='w', opener=gzip.open)
```

## Other dependencies

- pysam
- urllib
- locale
- os
- io
- sys
