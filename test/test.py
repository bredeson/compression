#!/usr/bin/env python3

import io, gzip, lzma

try:
    import bz2
except ImportError:
    import bz2file as bz2
    
from urllib.request import urlopen
from compression import open, bgzip

print("TEST caller writing:")
print("  test.caller.bed")
with open("test.caller.bed", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.bed.gz")    
with open("test.caller.bed.gz", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.bed.bz2")    
with open("test.caller.bed.bz2", mode='w', compression=None) as o:
    print("chr\t0\t1", file=o)

print("  test.caller.bed.xz")    
with open("test.caller.bed.xz", mode='w', compression=None) as o:
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
    
print("TEST stream writing:")
print("  test.stream.bed")
with __builtins__.open("test.stream.bed", mode='w') as s:
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

    
print("TEST caller reading:")
print("  test.caller.bed")
with open("test.caller.bed", mode='r') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bed.gz")
with open("test.caller.bed.gz", mode='r') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bed.bz2")
with open("test.caller.bed.bz2", mode='r') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bed.xz")
with open("test.caller.bed.xz", mode='r') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.io-bare.bed")
with open("test.caller.io-bare.bed", mode='r', compression=io) as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.io-str.bed")
with open("test.caller.io-str.bed", mode='r', compression='io') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.gzip-bare.bed")
with open("test.caller.gzip-bare.bed", mode='r', compression=gzip) as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.gzip-str.bed")
with open("test.caller.gzip-str.bed", mode='r', compression='gzip') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bgzip-bare.bed")
with open("test.caller.bgzip-bare.bed", mode='r', compression=bgzip) as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bgzip-str.bed")
with open("test.caller.bgzip-str.bed", mode='r', compression='bgzip') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bzip2-bare.bed")
with open("test.caller.bzip2-bare.bed", mode='r', compression=bz2) as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.bzip2-str.bed")
with open("test.caller.bzip2-str.bed", mode='r', compression='bz2') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.lzma-bare.bed")
with open("test.caller.lzma-bare.bed", mode='r', compression=lzma) as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  test.caller.lzma-str.bed")
with open("test.caller.lzma-str.bed", mode='r', compression='lzma') as i:
    l = next(i).strip()
    print(l == "chr\t0\t1")

print("  https://portal.nersc.gov/dna/plant/assembly/demo/unordered.hic.p_ctg.assembly")
with open("https://portal.nersc.gov/dna/plant/assembly/demo/unordered.hic.p_ctg.assembly", mode='r') as i:
    l = next(i).strip()
    print(l == ">h1tg000001l 1 27403807")

print("  https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz")
with open("https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz", mode='r', compression=bgzip) as i:
    l = next(i).strip()
    print(l == ">XLv73.000102974.5L")

print("  https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz")
with open("https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz", mode='r', compression=gzip) as i:
    l = next(i).strip()
    print(l == ">XLv73.000102974.5L")


print("TEST stream reading:")
print("  test.stream.bed")
with __builtins__.open("test.stream.bed", mode='r') as s:
    i = open(s, mode='r', compression=None)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.io-bare.bed")
with __builtins__.open("test.stream.io-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=io)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.io-str.bed")
with __builtins__.open("test.stream.io-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='io')
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.gzip-bare.bed")
with __builtins__.open("test.stream.gzip-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=gzip)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.gzip-str.bed")
with __builtins__.open("test.stream.gzip-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='gzip')
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.bgzip-bare.bed")
with __builtins__.open("test.stream.bgzip-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=bgzip)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.bgzip-str.bed")
with __builtins__.open("test.stream.bgzip-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='bgzip')
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.bzip2-bare.bed")
with __builtins__.open("test.stream.bzip2-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=bz2)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.bzip2-str.bed")
with __builtins__.open("test.stream.bzip2-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='bz2')
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()
    
print("  test.stream.lzma-bare.bed")
with __builtins__.open("test.stream.lzma-bare.bed", mode='r') as s:
    i = open(s, mode='r', compression=lzma)
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  test.stream.lzma-str.bed")
with __builtins__.open("test.stream.lzma-str.bed", mode='r') as s:
    i = open(s, mode='r', compression='lzma')
    l = next(i).strip()
    print(l == "chr\t0\t1")
    i.close()

print("  https://portal.nersc.gov/dna/plant/assembly/demo/unordered.hic.p_ctg.assembly")
with urlopen("https://portal.nersc.gov/dna/plant/assembly/demo/unordered.hic.p_ctg.assembly") as s:
    i = open(s, mode='r', compression=None)
    l = next(i).strip()
    print(l == ">h1tg000001l 1 27403807")
    i.close()

print("  https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz")
with urlopen("https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz") as s:
    i = open(s, mode='r', compression=bgzip)
    l = next(i).strip()
    print(l == ">XLv73.000102974.5L")
    i.close()

print("  https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz")
with urlopen("https://portal.nersc.gov/dna/plant/assembly/Xtrop/XENLA_JGIv73.fa.gz") as s:
    i = open(s, mode='r', compression=gzip)
    l = next(i).strip()
    print(l == ">XLv73.000102974.5L")
    i.close()

    
