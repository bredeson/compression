#!/usr/bin/env python3

import os, sys
import io, gzip, lzma
import subprocess

_PYTHON_VERSION = sys.version_info[:2]

if _PYTHON_VERSION < (3,3):
    import bz2file as bz2
else:
    import bz2
    
    
from urllib.request import urlopen
from compression import open, bgzip

print("TEST caller writing:")
print("  test.caller.none.bed")
with open("test.caller.none.bed", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.none.bed.gz")    
with open("test.caller.none.bed.gz", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.none.bed.bz2")    
with open("test.caller.none.bed.bz2", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.none.bed.xz")    
with open("test.caller.none.bed.xz", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.io-bare.bed")
with open("test.caller.io-bare.bed", mode='w', compression=io) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.io-str.bed")
with open("test.caller.io-str.bed", mode='w', compression='io') as o:
    print("chr\t0\t1", file=o)    

print("  test.caller.gzip-bare.bed")
with open("test.caller.gzip-bare.bed", mode='w', compression=gzip) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.gzip-str.bed")
with open("test.caller.gzip-str.bed", mode='w', compression='gzip') as o:
    print("chr\t0\t1", file=o)    

print("  test.caller.bgzip-bare.bed")
with open("test.caller.bgzip-bare.bed", mode='w', compression=bgzip) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.bgzip-str.bed")
with open("test.caller.bgzip-str.bed", mode='w', compression='bgzip') as o:
    print("chr\t0\t1", file=o)    

print("  test.caller.bzip2-bare.bed")
with open("test.caller.bzip2-bare.bed", mode='w', compression=bz2) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.bzip2-str.bed")
with open("test.caller.bzip2-str.bed", mode='w', compression='bz2') as o:
    print("chr\t0\t1", file=o)    

print("  test.caller.lzma-bare.bed")
with open("test.caller.lzma-bare.bed", mode='w', compression=lzma) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.lzma-str.bed")
with open("test.caller.lzma-str.bed", mode='w', compression='lzma') as o:
    print("chr\t0\t1", file=o)    

print("  test.caller.xz-str.bed")
with open("test.caller.xz-str.bed", mode='w', compression='xz') as o:
    print("chr\t0\t1", file=o)    



print("")    
print("TEST caller reading:")
print("  test.caller.none.bed")
with open("test.caller.none.bed", mode='r') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.none.bed.gz")
with open("test.caller.none.bed.gz", mode='r') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.none.bed.bz2")
with open("test.caller.none.bed.bz2", mode='r') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.none.bed.xz")
with open("test.caller.none.bed.xz", mode='r') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.io-bare.bed")
with open("test.caller.io-bare.bed", mode='r', compression=io) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.io-str.bed")
with open("test.caller.io-str.bed", mode='r', compression='io') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.gzip-bare.bed")
with open("test.caller.gzip-bare.bed", mode='r', compression=gzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.gzip-str.bed")
with open("test.caller.gzip-str.bed", mode='r', compression='gzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.bgzip-bare.bed")
with open("test.caller.bgzip-bare.bed", mode='r', compression=bgzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.bgzip-str.bed")
with open("test.caller.bgzip-str.bed", mode='r', compression='bgzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.bzip2-bare.bed")
with open("test.caller.bzip2-bare.bed", mode='r', compression=bz2) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.bzip2-str.bed")
with open("test.caller.bzip2-str.bed", mode='r', compression='bz2') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.lzma-bare.bed")
with open("test.caller.lzma-bare.bed", mode='r', compression=lzma) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.lzma-str.bed")
with open("test.caller.lzma-str.bed", mode='r', compression='lzma') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  test.caller.xz-str.bed")
with open("test.caller.xz-str.bed", mode='r', compression='xz') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

    
print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.none.bed")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.none.bed", mode='r', compression=None) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.io.bed")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.io.bed", mode='r', compression='io') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
    
print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.gzip.bed.gz")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.gzip.bed.gz", mode='r', compression='gzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
    
print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bgzip.bed.gz")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bgzip.bed.gz", mode='r', compression='bgzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bzip2.bed.bz2")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bzip2.bed.bz2", mode='r', compression='bz2') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.lzma.bed.xz")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.lzma.bed.xz", mode='r', compression='lzma') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.xz.bed.xz")
with open("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.xz.bed.xz", mode='r', compression='xz') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
    

    
print("")
print("TEST stream writing:")
print("  test.stream.none.bed")
with __builtins__.open("test.stream.none.bed", mode='w') as s:
    o = open(s, mode='w', compression=None)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.io-bare.bed")
with __builtins__.open("test.stream.io-bare.bed", mode='w') as s:
    o = open(s, mode='w', compression=io)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.io-str.bed")
with __builtins__.open("test.stream.io-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='io')
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.gzip-bare.bed")
with __builtins__.open("test.stream.gzip-bare.bed", mode='w') as s:
    o = open(s, mode='w', compression=gzip)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.gzip-str.bed")
with __builtins__.open("test.stream.gzip-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='gzip')
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.bgzip-bare.bed")
with __builtins__.open("test.stream.bgzip-bare.bed", mode='w') as s:
    o = open(s, mode='w', compression=bgzip)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.bgzip-str.bed")
with __builtins__.open("test.stream.bgzip-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='bgzip')
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.bzip2-bare.bed")
with __builtins__.open("test.stream.bzip2-bare.bed", mode='w') as s:
    o = open(s, mode='w', compression=bz2)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.bzip2-str.bed")
with __builtins__.open("test.stream.bzip2-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='bz2')
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.lzma-bare.bed")
with __builtins__.open("test.stream.lzma-bare.bed", mode='w') as s:
    o = open(s, mode='w', compression=lzma)
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.lzma-str.bed")
with __builtins__.open("test.stream.lzma-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='lzma')
    print("chr\t0\t1", file=o)
    o.close()

print("  test.stream.xz-str.bed")
with __builtins__.open("test.stream.xz-str.bed", mode='w') as s:
    o = open(s, mode='w', compression='xz')
    print("chr\t0\t1", file=o)
    o.close()



print("")    
print("TEST stream reading:")
print("  test.stream.none.bed")
with __builtins__.open("test.stream.none.bed", mode='r') as s:
    i = open(s, mode='r', compression=None)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.io-bare.bed")
with __builtins__.open("test.stream.io-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=io)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.io-str.bed")
with __builtins__.open("test.stream.io-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='io')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.gzip-bare.bed")
with __builtins__.open("test.stream.gzip-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=gzip)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.gzip-str.bed")
with __builtins__.open("test.stream.gzip-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='gzip')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.bgzip-bare.bed")
with __builtins__.open("test.stream.bgzip-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=bgzip)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.bgzip-str.bed")
with __builtins__.open("test.stream.bgzip-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='bgzip')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.bzip2-bare.bed")
with __builtins__.open("test.stream.bzip2-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=bz2)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.bzip2-str.bed")
with __builtins__.open("test.stream.bzip2-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='bz2')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"
    
print("  test.stream.lzma-bare.bed")
with __builtins__.open("test.stream.lzma-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=lzma)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  test.stream.lzma-str.bed")
with __builtins__.open("test.stream.lzma-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='lzma')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.none.bed")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.none.bed") as s:
    i = open(s, mode='r', compression=None)
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.io.bed")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.io.bed") as s:
    i = open(s, mode='r', compression='io')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.gzip.bed.gz")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.gzip.bed.gz") as s:
    i = open(s, mode='r', compression='gzip')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"
    
print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bgzip.bed.gz")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bgzip.bed.gz") as s:
    i = open(s, mode='r', compression='bgzip')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bzip2.bed.bz2")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.bzip2.bed.bz2") as s:
    i = open(s, mode='r', compression='bz2')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"
    
print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.lzma.bed.xz")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.lzma.bed.xz") as s:
    i = open(s, mode='r', compression='lzma')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"

print("  https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.xz.bed.xz")
with urlopen("https://raw.githubusercontent.com/bredeson/compression/refs/heads/main/test/test.xz.bed.xz") as s:
    i = open(s, mode='r', compression='xz')
    l = next(i).strip()
    i.close()
    assert l == "chr\t0\t1"
    

    
print("")    
print("TEST stdio writing:")
print("  test.stdio.none.bed")
with __builtins__.open("test.stdio.none.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.none.py > test.stdio.none.bed", shell=True)
with open("test.stdio.none.bed", mode='r', compression=None) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.none.py")


print("  test.stdio.io-bare.bed")
with __builtins__.open("test.stdio.io-bare.py", mode='w') as s:
    c = """
import io
from compression import STDIO, open
with open(STDIO, mode='w', compression=io) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.io-bare.py > test.stdio.io-bare.bed", shell=True)
with open("test.stdio.io-bare.bed", mode='r', compression=io) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.io-bare.py")


print("  test.stdio.io-str.bed")
with __builtins__.open("test.stdio.io-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='io') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.io-str.py > test.stdio.io-str.bed", shell=True)
with open("test.stdio.io-str.bed", mode='r', compression='io') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.io-str.py")


print("  test.stdio.gzip-bare.bed")
with __builtins__.open("test.stdio.gzip-bare.py", mode='w') as s:
    c = """
import gzip
from compression import STDIO, open
with open(STDIO, mode='w', compression=gzip) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.gzip-bare.py > test.stdio.gzip-bare.bed", shell=True)
with open("test.stdio.gzip-bare.bed", mode='r', compression=gzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.gzip-bare.py")


print("  test.stdio.gzip-str.bed")
with __builtins__.open("test.stdio.gzip-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='gzip') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.gzip-str.py > test.stdio.gzip-str.bed", shell=True)
with open("test.stdio.gzip-str.bed", mode='r', compression='gzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.gzip-str.py")


print("  test.stdio.bgzip-bare.bed")
with __builtins__.open("test.stdio.bgzip-bare.py", mode='w') as s:
    c = """
from compression import bgzip
from compression import STDIO, open
with open(STDIO, mode='w', compression=bgzip) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.bgzip-bare.py > test.stdio.bgzip-bare.bed", shell=True)
with open("test.stdio.bgzip-bare.bed", mode='r', compression=bgzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.bgzip-bare.py")


print("  test.stdio.bgzip-str.bed")
with __builtins__.open("test.stdio.bgzip-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='bgzip') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.bgzip-str.py > test.stdio.bgzip-str.bed", shell=True)
with open("test.stdio.bgzip-str.bed", mode='r', compression='bgzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.bgzip-str.py")


print("  test.stdio.bzip2-bare")
with __builtins__.open("test.stdio.bzip2-bare.py", mode='w') as s:
    c = """
import bz2
from compression import STDIO, open
with open(STDIO, mode='w', compression=bz2) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.bzip2-bare.py > test.stdio.bzip2-bare.bed", shell=True)
with open("test.stdio.bzip2-bare.bed", mode='r', compression=bz2) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.bzip2-bare.py")


print("  test.stdio.bzip2-str.bed")
with __builtins__.open("test.stdio.bzip2-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='bz2') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.bzip2-str.py > test.stdio.bzip2-str.bed", shell=True)
with open("test.stdio.bzip2-str.bed", mode='r', compression='bz2') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.bzip2-str.py")


print("  test.stdio.lzma-bare")
with __builtins__.open("test.stdio.lzma-bare.py", mode='w') as s:
    c = """
import lzma
from compression import STDIO, open
with open(STDIO, mode='w', compression=lzma) as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.lzma-bare.py > test.stdio.lzma-bare.bed", shell=True)
with open("test.stdio.lzma-bare.bed", mode='r', compression=lzma) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.lzma-bare.py")


print("  test.stdio.lzma-str.bed")
with __builtins__.open("test.stdio.lzma-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='lzma') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.lzma-str.py > test.stdio.lzma-str.bed", shell=True)
with open("test.stdio.lzma-str.bed", mode='r', compression='lzma') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.lzma-str.py")


print("  test.stdio.xz-str.bed")
with __builtins__.open("test.stdio.xz-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='w', compression='xz') as o:
    print("chr\t0\t1", file=o)
    """
    print(c, file=s)
subprocess.run("python test.stdio.xz-str.py > test.stdio.xz-str.bed", shell=True)
with open("test.stdio.xz-str.bed", mode='r', compression='xz') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
os.remove("test.stdio.xz-str.py")


print("")
print("TEST stdio reading:")
print("  test.stdio.none.bed")
with __builtins__.open("test.stdio.none.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression=None) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.none.bed | python test.stdio.none.py", shell=True)
os.remove("test.stdio.none.py")


print("  test.stdio.io-bare.bed")
with __builtins__.open("test.stdio.io-bare.py", mode='w') as s:
    c = """
import io
from compression import STDIO, open
with open(STDIO, mode='r', compression=io) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.io-bare.bed | python test.stdio.io-bare.py", shell=True)
os.remove("test.stdio.io-bare.py")


print("  test.stdio.io-str.bed")
with __builtins__.open("test.stdio.io-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='io') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.io-str.bed | python test.stdio.io-str.py", shell=True)
os.remove("test.stdio.io-str.py")


print("  test.stdio.gzip-bare.bed")
with __builtins__.open("test.stdio.gzip-bare.py", mode='w') as s:
    c = """
import gzip
from compression import STDIO, open
with open(STDIO, mode='r', compression=gzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.gzip-bare.bed | python test.stdio.gzip-bare.py", shell=True)
os.remove("test.stdio.gzip-bare.py")


print("  test.stdio.gzip-str.bed")
with __builtins__.open("test.stdio.gzip-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='gzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.gzip-str.bed | python test.stdio.gzip-str.py", shell=True)
os.remove("test.stdio.gzip-str.py")


print("  test.stdio.bgzip-bare.bed")
with __builtins__.open("test.stdio.bgzip-bare.py", mode='w') as s:
    c = """
from compression import bgzip
from compression import STDIO, open
with open(STDIO, mode='r', compression=bgzip) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.bgzip-bare.bed | python test.stdio.bgzip-bare.py", shell=True)
os.remove("test.stdio.bgzip-bare.py")


print("  test.stdio.bgzip-str.bed")
with __builtins__.open("test.stdio.bgzip-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='bgzip') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.bgzip-str.bed | python test.stdio.bgzip-str.py", shell=True)
os.remove("test.stdio.bgzip-str.py")


print("  test.stdio.bzip2-bare.bed")
with __builtins__.open("test.stdio.bzip2-bare.py", mode='w') as s:
    c = """
import bz2
from compression import STDIO, open
with open(STDIO, mode='r', compression=bz2) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.bzip2-bare.bed | python test.stdio.bzip2-bare.py", shell=True)
os.remove("test.stdio.bzip2-bare.py")


print("  test.stdio.bzip2-str.bed")
with __builtins__.open("test.stdio.bzip2-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='bz2') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.bzip2-str.bed | python test.stdio.bzip2-str.py", shell=True)
os.remove("test.stdio.bzip2-str.py")


print("  test.stdio.lzma-bare.bed")
with __builtins__.open("test.stdio.lzma-bare.py", mode='w') as s:
    c = """
import lzma
from compression import STDIO, open
with open(STDIO, mode='r', compression=lzma) as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.lzma-bare.bed | python test.stdio.lzma-bare.py", shell=True)
os.remove("test.stdio.lzma-bare.py")


print("  test.stdio.lzma-str.bed")
with __builtins__.open("test.stdio.lzma-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='lzma') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.lzma-str.bed | python test.stdio.lzma-str.py", shell=True)
os.remove("test.stdio.lzma-str.py")


print("  test.stdio.xz-str.bed")
with __builtins__.open("test.stdio.xz-str.py", mode='w') as s:
    c = """
from compression import STDIO, open
with open(STDIO, mode='r', compression='xz') as i:
    l = next(i).strip()
    assert l == "chr\t0\t1"
"""
    print(c, file=s)
subprocess.run("cat test.stdio.xz-str.bed | python test.stdio.xz-str.py", shell=True)
os.remove("test.stdio.xz-str.py")
