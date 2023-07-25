#!/usr/bin/env python3
""" Class Basic Cache"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and implements caching system"""
    def __init__(self):
        """Initialize the BasicCache"""
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """LIFO algorithm , add element"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.last_key))
            self.cache_data.pop(self.last_key)
        self.last_key = key

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            return self.cache_data[key]
