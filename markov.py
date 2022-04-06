import random

# This file implements a Markov text bot capable of generating
# somewhat intelligible text. While many other, modern languge
# models are much better and produece very good output
# (for example, GPT-3), the basic principles underlying this model
# are not completely different.

# Producing output text is a 2-step process:
#   1. Perform a Markov analysis on a corpus
#      (i.e., determine what what words frequently occur
#       after other words).
#   2. Use the analysis to produce random textual output.

# Things you can try to do with this model:
#   - Use a book other than Jane Eyre to see how it affects output, or
#     try with multiple books
#   - Experiment with the n-gram size. Try 1-grams, 2-grams (as coded here),
#     3-grams, or more.

infile = open('jane_eyre.txt')

# First, collect a list of every word in the book in order.
words = []
for line in infile:
    # Clean-up step: Remove extraneous whitespace and lowercase.
    # Try removing punctuation here for better output!
    line = line.strip().lower()

    # Split the line into individual words, assuming a space is
    # good enough to do this
    for word in line.split(' '):
        # Append each word in the line to the words list
        words.append(word)


# Create a dictionary mapping prefixes to list of possible
# next words. In this example, the prefixes are bigrams -
# tuples of two words. The `mapping` dictionary will eventually look
# something like this:
#
# {
#   ("it", "was"): ['a', 'her', 'the', 'out', ...],
#   ("was", "a"): ['loud', 'terrible', 'cat', ...],
#   ...    
# }
#
# How to interpret this is that the tuple represents a series of two words
# in a sentence (the bigram), and the list contains all words that were found
# to follow that bigram. So in the example above, our analysis found sentences containing
# "it was a...", "it was her...", "it was the...", "was a loud", "was a terrible", and so on.
mapping = dict()

# Here, we iterate through the word list. We use slicing to offset the words list by one and two.
# For example, if the word list contains:
#
# words = ["it", "was", "a", "dark", "and", "stormy", "night"]
#
# using slicing to offset the words list and zipping to combine them into a tuple results in the
# following iterations:
#
#   ("it", "was", "a")
#   ("was", "a", "dark")
#   ("a", "dark", "and")
#   ("dark", "and", "stormy")
#   ("and", "stormy", "night")
#
# This allows us to select bigrams (elements 0 and 1 in the tuple) and an associated
# next candidate word (element 2 in the tuple). We use these to populate the dictionary:
for prefix_a, prefix_b, candidate in zip(words, words[1:], words[2:]):
    prefix = (prefix_a, prefix_b)
    if prefix not in mapping:
        mapping[prefix] = []
    mapping[prefix].append(candidate)


#Finally, choose a starting bigram at random:
prefix = random.choice(list(mapping.keys()))
output = [prefix[0], prefix[1]]

# Generate 100 words:
for i in range(100):
    # Given a prefix, choose a random candidate word
    next = random.choice(mapping[prefix])

    # Save the candidate word in the output
    output.append(next)

    # Assemble a new prefix bigram and continue
    prefix = (prefix[1], next)

# Join the final output list on a blank space to print it
print(' '.join(output))