from collections import Counter

def word_frequency(input_text):
    # Split the input text into words
    words = input_text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Sort the results alphanumerically based on the words
    sorted_word_counts = dict(sorted(word_counts.items()))

    return sorted_word_counts

# Example usage:
input_text = "the quick brown fox jumps over the lazy dog the dog barks loudly"
result = word_frequency(input_text)

# Print the sorted word frequencies
for word, count in result.items():
    print(f"{word}: {count}")
