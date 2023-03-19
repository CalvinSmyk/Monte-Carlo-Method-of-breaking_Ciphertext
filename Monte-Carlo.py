from random import randrange, shuffle
from IPython.display import clear_output
import json
import random



def decode(filename, common, iters=10000):
    # Load the Ciphertext
    print("\n  * Loading file...\n")
    cipherText = load(filename)
    cipherText = cipherText.lower()
    key, S, I = search(cipherText, iters)
    plainText = transform(cipherText, key)
    clear_output(wait=True)
    print(f"Final plaintext with Score {S} at Iteration {I}:\n")
    print(plainText)


#   Randomly goes through all possible combinations of keys and selects the best one based on a score.
def search(cipherText, iters):
    key = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']  # Initial setup key
    bestScore = 0
    old_bestScore = 0
    newScore = 0
    iteration_done = 0
    shuffle(key)  # permute the key randomly for initialisation
    for i in range(1, iters + 1):
        newKey = swap(key[:])
        newScore = score(newKey, cipherText)
        if newScore > bestScore:
            key = newKey[:]
            bestScore = newScore
        elif newScore == bestScore:
            if randrange(0, 2) == 1:
                key = newKey[:]
        if bestScore > old_bestScore:
            old_bestScore = bestScore
            iteration_done = i
            clear_output(wait=True)
            print(f"Score: {bestScore} Iteration: {i}")
            plainText = transform(cipherText, key)
            print(plainText)
    return key, bestScore, iteration_done


######################    HELP FUNCTIONS   ##########################

#   take a specific key and switch the values of two random values

def swap(key):
    i = random.randint(0, 25)
    j = random.randint(0, 25)
    key[i], key[j] = key[j], key[i]
    return key


def load(filename):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    return text


#   Use key and english alphabet to recover encrypt the message

def transform(cipherText, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = str.maketrans("".join(key), alphabet)
    return cipherText.translate(mapping)


def to_percentage(dictionary):
    total = sum(dictionary.values())
    return {key: 100 * value / total for key, value in dictionary.items()}


def all_bigrams(text):
    bigrams = {}
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        if bigram in bigrams:
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1
    return bigrams


# calculate the score given a key and text

def score(key, cipherText):
    attempt = transform(cipherText, key)
    score = 0
    for item in common.keys():
        count = attempt.count(item)
        frequency = common[item]
        score += count * frequency
    return score


def save_as_json(file):
    with open("bigram.txt", "w") as file:
        json.dump(sorted_bigrams, file)


#############################################################################

if __name__ == '__main__':
    bigram_file_path = "/Users/calvinsmyk/PycharmProjects/Cryptography/supp/war-and-peace.txt"
    input_file_path = "/Users/calvinsmyk/PycharmProjects/Cryptography/supp/testInput.txt"
    final_bigram_path = "bigram.txt"
    save = 0
    create_new_bigram_freq_file = 0
    if create_new_bigram_freq_file == 1:
        text = load(bigram_file_path)
        bigrams = all_bigrams(text)
        bigrams_conv = to_percentage(bigrams)
        sorted_bigrams = dict(sorted(bigrams_conv.items(), key=lambda x: x[1], reverse=True))
    if save == 1:
        save_as_json(sorted_bigrams)
    sorted_bigrams_dict = load(final_bigram_path)
    decode(input_file_path, sorted_bigrams_dict)