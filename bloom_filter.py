"""
This file implements a basic Bloom Filter based on the description given in
http://codekata.com/kata/kata05-bloom-filters/.

It allows for the following features:
- Add data in the filter.
- search for data.

The following additional libraries are used:
- Using https://pypi.org/project/mmh3/ for generating the hashes. This is a non-cryptographic hash, is faster than md5 and sha hashes and allows to pass in seed to generate different hash for same data.

- Using https://pypi.org/project/bitarray/ for a bitarray in python.
Bitarray can also be created in-house using technique described here https://wiki.python.org/moin/BitArrays


Implementation
=================
Initializes a BloomFilter object with a capacity equal to max_elements and default error probability as 0.01 (1%).
"""
import math
import mmh3
import bitarray
from typing import Any


class BloomFilter:
    def __init__(self, max_elements: int, error_probability: float = 0.01):
        # total bits needed to store max_elements
        self.total_bits: int = self._calculate_bits_needed(max_elements, error_probability)

        # total hash functions needed
        self.total_hashes: int = self._calculate_total_hash_functions_needed(max_elements)

        # bit array to store the data
        self.bit_store = bitarray.bitarray(self.total_bits)
        self.bit_store.setall(False)

    def _calculate_bits_needed(self, max_elements: int, error_probability: float) -> int:
        # formula copied from https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
        return math.ceil((-1 * max_elements*math.log(error_probability)) / (math.log(2)**2))

    def _calculate_total_hash_functions_needed(self, max_elements: int) -> int:
        # formula copied from https://en.wikipedia.org/wiki/Bloom_filter#Optimal_number_of_hash_functions
        return math.ceil((self.total_bits / max_elements) * math.log(2))

    def add(self, data: Any) -> bool:
        if self.contains(data):
            return False

        for i in range(self.total_hashes):
            self.bit_store[self._get_bit_position(data, seed=i)] = True

    def contains(self, data: Any) -> bool:
        return all(
            self.bit_store[self._get_bit_position(data, seed=i)]
            for i in range(self.total_hashes)
        )

    def _get_bit_position(self, data: Any, seed: int) -> int:
        return self._get_hash(data, seed) % self.total_bits

    def _get_hash(self, data: Any, seed: int) -> int:
        return mmh3.hash(data, seed, signed=False)
