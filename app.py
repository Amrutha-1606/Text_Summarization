import re
from collections import Counter

# Get paragraph from the user
text = input("Enter a paragraph: ")

# Check if input is empty
if not text.strip():
    print("Please enter some text.")
    exit()

# Split paragraph into sentences
sentences = re.split(r'(?<=[.!?])\s+', text.strip())

# Convert text into words
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# Common words that are ignored
stop_words = {
    "the", "is", "a", "an", "and", "or",
    "of", "to", "in", "on", "for", "are",
    "was", "were", "this", "that", "with"
}

# Count important words
word_frequency = Counter(
    word for word in words
    if word not in stop_words
)

# Calculate score for every sentence
sentence_scores = []

for sentence in sentences:

    sentence_words = re.findall(
        r'\b[a-zA-Z]+\b',
        sentence.lower()
    )

    score = sum(
        word_frequency[word]
        for word in sentence_words
    )

    sentence_scores.append(score)

# Find the highest-scoring sentence
best_index = sentence_scores.index(
    max(sentence_scores)
)

summary = sentences[best_index]

# Display result
print("\nOriginal Text:")
print(text)

print("\nSummary:")
print(summary)