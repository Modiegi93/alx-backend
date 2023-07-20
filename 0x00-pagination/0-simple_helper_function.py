#!/usr/bin/env python3
""" Paginating with page and page size"""


def index_range(page, page_size):
    """ Return a list containing start and end index"""
    page = max(page, 1)
    page_size = max(page_size, 1)

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
