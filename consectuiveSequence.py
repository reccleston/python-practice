# Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
import sys

def consecutiveSequence(seq1, seq2):
    # concat lists
    # sort 
    # check if concat'd list is conseq
    seq2 = list(map(int, seq2.split(',')))
    seq1 = list(map(int, seq1.split(',')))
    combined_sorted_sequence = sorted(seq1 + seq2)
    return combined_sorted_sequence == list(range(min(combined_sorted_sequence), max(combined_sorted_sequence)+1))

print(consecutiveSequence(sys.argv[0], sys.argv[1]))