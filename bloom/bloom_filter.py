class BloomFilter(object):

    def __init__(self, num_bits, num_hashers):
        self.num_bits = num_bits
        self.num_hashers = num_hashers
        self.bits = [False] * num_bits
        self.hashers = [get_hasher() for i in range(num_hashers)]

    def __repr__(self):
        return u"BloomFilter(num_bits={0}, num_hashers={1})".format(
            self.num_bits,
            self.num_hashers,
        )


def get_hasher():
    def hasher(target):
        pass
    return hasher
