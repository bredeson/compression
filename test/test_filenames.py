import unittest
from compression.filenames import split_suffix, strip_suffix, infer_compression_format
from compression.constants import COMPRESSION_SUFFIX

class TestFilenames(unittest.TestCase):
    def test_split_suffix_found(self):
        # Use known suffixes from COMPRESSION_SUFFIX
        filename = 'file.txt.gz'
        suffixes = ['.gz', '.txt']
        base, suffix = split_suffix(filename, suffixes)
        self.assertEqual(base, 'file.txt')
        self.assertEqual(suffix, '.gz')

    def test_split_suffix_not_found(self):
        filename = 'file.txt'
        suffixes = ['.gz', '.bz2']
        base, suffix = split_suffix(filename, suffixes)
        self.assertEqual(base, 'file.txt')
        self.assertIsNone(suffix)

    def test_split_suffix_bytes(self):
        filename = b'file.txt.gz'
        suffixes = [b'.gz', b'.txt']
        base, suffix = split_suffix(filename, suffixes)
        self.assertEqual(base, b'file.txt')
        self.assertEqual(suffix, b'.gz')

    def test_strip_suffix(self):
        filename = 'file.txt.gz'
        suffixes = ['.gz', '.txt']
        stripped = strip_suffix(filename, suffixes)
        self.assertEqual(stripped, 'file.txt')

    def test_strip_suffix_no_match(self):
        filename = 'file.txt'
        suffixes = ['.gz', '.bz2']
        stripped = strip_suffix(filename, suffixes)
        self.assertEqual(stripped, 'file.txt')

    def test_infer_compression_format_string(self):
        for fmt, suffixes in COMPRESSION_SUFFIX.items():
            for suf in suffixes:
                fname = f'test{suf}'
                self.assertEqual(infer_compression_format(fname), fmt)

    def test_infer_compression_format_bytes(self):
        for fmt, suffixes in COMPRESSION_SUFFIX.items():
            for suf in suffixes:
                fname = f'test{suf}'.encode()
                self.assertEqual(infer_compression_format(fname), fmt)

    def test_infer_compression_format_none_string(self):
        self.assertIsNone(infer_compression_format('file.txt'))

    def test_infer_compression_format_none_bytes(self):
        self.assertIsNone(infer_compression_format(b'file.txt'))


if __name__ == '__main__':
    unittest.main()
