import random


class BloomFilter(object):

    def __init__(self, num_bits, num_hashers):
        self.num_bits = num_bits
        self.num_hashers = num_hashers
        self.num_elements = 0
        self.bits = [False] * num_bits
        self.hashers = [self.get_hasher() for i in range(num_hashers)]

    def __repr__(self):
        return u"BloomFilter(num_bits={0}, num_hashers={1})".format(
            self.num_bits,
            self.num_hashers,
        )

    def get_hasher(self):
        random_factor = random.randint(0, self.num_bits - 1)

        def hasher(target):
            hashed = hash(target)
            hashed = hashed % self.num_bits
            hashed += random_factor
            hashed = hashed % self.num_bits
            return hashed
        return hasher

    def add_element(self, element):
        for hasher in self.hashers:
            position = hasher(element)
            self.bits[position] = True
        self.num_elements += 1

    def query_for(self, element):
        for hasher in self.hashers:
            position = hasher(element)
            if not self.bits[position]:
                # Definitely not in set
                return False
        # May be false positive
        return True

    @property
    def bits_set(self):
        found = 0
        for bit in self.bits:
            if bit:
                found += 1
        return found

    @property
    def ratio_bits_set(self):
        return 1.0 * self.bits_set / self.num_bits
