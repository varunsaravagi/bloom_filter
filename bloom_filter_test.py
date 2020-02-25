"""
Test program to test the bloom filter implementation.

This adds all the names given in names_added.txt (~2000) in the filter.
Then we test for presence of a total of 200 random entries from names_added.txt and names_not_added.txt files.

Program outputs the total number of False Positive and Not Present entries.
"""

from bloom_filter import BloomFilter
from random import shuffle

ERROR_PROBABILITY = 0.01
NUMBER_OF_TEST_ENTRIES_ADDED = 100
NUMBER_OF_TEST_ENTRIES_NOT_ADDED = 100


def test_bloom_filter():
    bloom_filter = BloomFilter(max_elements=2000, error_probability=ERROR_PROBABILITY)
    _insert_data(bloom_filter)
    _check_data(bloom_filter)

def _insert_data(bloom_filter):
    with open('names_added.txt') as f:
        for test_data in f:
            bloom_filter.add(test_data.strip('\n'))

def _check_data(bloom_filter):
    test_data, test_data_added, test_data_not_added = _create_test_data()
    false_positive, probably_present, not_present = 0, 0, 0
    for data in test_data:
        if bloom_filter.contains(data):
            if data in test_data_not_added:
                false_positive += 1
            else:
                probably_present += 1
        else:
            not_present += 1

    print(f"Total entries added {len(test_data_added)}")
    print(
        f"""Searching for {len(test_data)} entries:
        {NUMBER_OF_TEST_ENTRIES_ADDED} entries from added set,
        {NUMBER_OF_TEST_ENTRIES_NOT_ADDED} entries from not added set""",
    )
    print(f"False positive: {false_positive}")
    print(f"Not present: {not_present}")

def _create_test_data():
    test_datas_added = []
    test_datas_not_added = []

    with open('names_added.txt') as f:
        for test_data in f:
            test_datas_added.append(test_data.rstrip('\n'))

    with open('names_not_added.txt') as f:
        for test_data in f:
            test_datas_not_added.append(test_data.rstrip('\n'))

    shuffle(test_datas_added)
    shuffle(test_datas_not_added)

    return test_datas_added[:NUMBER_OF_TEST_ENTRIES_ADDED] + test_datas_not_added[:NUMBER_OF_TEST_ENTRIES_NOT_ADDED], set(test_datas_added), set(test_datas_not_added)


if __name__ == '__main__':
    test_bloom_filter()
