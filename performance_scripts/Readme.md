# Notes on performance

- I have defined productions scale as being able to handle 10 M games, almost instantly 1 second.


# Naive solution

1. Naive Solution Baseline:

tableague-py3.9) ➜  tableague git:(measure_performance) ✗ time tableague --filename ./scripts/large_file.txt > large_result_test.txt
tableague --filename ./scripts/large_file.txt > large_result_test.txt  15.63s user 0.23s system 99% cpu 15.942 total


2. Performance tweak

Most interesting performance tweak seems to try to get the time for 10 M games to around 1 second, as this is a magic number for user experience.


