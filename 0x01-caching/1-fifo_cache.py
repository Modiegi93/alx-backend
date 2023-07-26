#!/usr/bin/env python3
""" Class Basic Cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and implements caching system"""

    def __init__(self):
        """Initialize the FIFOCache"""
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def _pop(self):
        """FIFO algorithm, remove element"""
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]

    def _push(self, key, item):
        """FIFO algorithm, add element"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self._pop()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._push(key, item)

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            val = self.cache_data[key]
            return val
