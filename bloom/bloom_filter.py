class BloomFilter(object):

    def __init__(self, num_bits):
        self.num_bits = num_bits

    def __repr__(self):
        return u"BloomFilter(num_bits=%s)" % self.num_bits
