#!/usr/bin/env python3
"""Paginate a database of popular baby names"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Return a list containing start and end index"""
    page = max(page, 1)
    page_size = max(page_size, 1)

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page and page size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_items = len(dataset)
        total_pages = math.ceil(total_items / page_size)

        if page > total_pages:
            return []

        start_index, end_index = index_range(page, page_size)
        return dataset[start_index:end_index]
