import nltk
import numpy as np
import random
import string

# NLTK modules for text processing
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Preprocessing for tokenization and lemmatization
lemmatizer = WordNetLemmatizer()

# Reading and preprocessing the corpus data
file_path = 'chat_corpus.txt'
corpus = open(file_path, 'r', errors='ignore').read().lower()
sentences = nltk.sent_tokenize(corpus)
word_freq = {}
word_tokens = [word_tokenize(sentence) for sentence in sentences]

# Tokenization and Lemmatization
for tokens in word_tokens:
    for token in tokens:
        token = lemmatizer.lemmatize(token)
        if token not in string.punctuation:
            if token not in word_freq:
                word_freq[token] = 1
            else:
                word_freq[token] += 1

# Function to get bag of words
def get_bag_of_words(sentence, word_tokens):
    bag = np.zeros(len(word_tokens))
    for idx, word in enumerate(word_tokens):
        if word in sentence:
            bag[idx] = 1
    return bag

# Generating response
def generate_response(user_input):
    user_input = user_input.lower()
    response = ''
    user_bag = get_bag_of_words(user_input, word_tokens)
    similarity_scores = {}
    for i in range(len(sentences)):
        similarity_scores[i] = nltk.jaccard_distance(set(word_tokens[i]), set(user_input.split()))

    sorted_idx = sorted(similarity_scores.items(), key=lambda item: item[1])
    closest_match_idx = sorted_idx[0][0]
    response = sentences[closest_match_idx]
    return response

# Main function to run the chatbot
def chat():
    print("Welcome! I'm here to chat with you. You can start typing. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("Bot:", response)

if __name__ == "__main__":
    chat()
