Implementation of a simple Bloom Filter based on description in http://codekata.com/kata/kata05-bloom-filters/ .

Tested on python3.6 on a unix shell.

# Usage
1. Run `make venv` to create a virtual environment with all the dependencies installed.
2. Run `source venv/bin/activate` to activate the virtual env.
3. Run `make test` to execute a simple test.


# Sample Run
```
(venv)~/personal/bloom_filter (master) $ make test
venv/bin/python bloom_filter_test.py
Total entries added 1894
Searching for 200 entries:
    100 entries from added set,
    100 entries from not added set
False positive: 2
Not present: 98
```

# Modifying the tests
The test by default creates a Bloom Filter with error probability of 0.01 (1%) and adds all the entries from `names_added.txt` in the filter. 
It then checks for the presence of 100 random entries from each of `named_added.txt` and `names_not_added.txt` and outputs the result.

You can modify the test variables by changing the following variables in `bloom_filter_test.py`.
- ERROR_PROBABILITY
- NUMBER_OF_TEST_ENTRIES_ADDED
- NUMBER_OF_TEST_ENTRIES_NOT_ADDED

# What does the various files mean?

1. `bloom_filter.py`: Contains implementation of the filter.
2. `bloom_filter_test.py`: Sample program to test the implementation.
3. `names_added.txt`: Test data that is added to the bloom filter.
4. `names_not_added.txt`: Test data that is not added but its presence is checked in the filter. Used to determine the number of false positives.

# Future Improvements

1. Take Bloom Filter capacity and error tolerance as input from the user.
2. Use different hash functions for each required hash.
3. Make the filter scalable when required and not be capacity restricted.

