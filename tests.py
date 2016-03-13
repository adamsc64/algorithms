from unittest import TestCase
from bloom import BloomFilter


class TestBloomFilter(TestCase):

    def test_repr(self):
        self.assertEqual(repr(BloomFilter(num_bits=10, num_hashers=5)),
                         "BloomFilter(num_bits=10, num_hashers=5)")

    def test_hash_consistent(self):
        bf = BloomFilter(10, 5)
        hasher = bf.get_hasher()
        hashed1 = hasher('sdlksdlkf')
        hashed2 = hasher('sdlksdlkf')
        self.assertEqual(type(hashed1), int)
        self.assertEqual(hashed1, hashed2)
