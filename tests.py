from unittest import TestCase
from bloom import BloomFilter

class TestRepr(TestCase):
    def test_repr(self):
        self.assertEqual(repr(BloomFilter(num_bits=10, num_hashers=5)),
                         "BloomFilter(num_bits=10, num_hashers=5)")
