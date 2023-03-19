# Monte-Carlo-Method-of-breaking_Ciphertext
 Implementation of the Monte Carlo method of breaking substitution cipher

This Python code is designed to decode a given ciphertext by utilizing a technique called brute force attack. This method involves trying out every possible combination of keys until the correct one is found. The program is written using the Python programming language, and it utilizes libraries like "random", "IPython.display", and "json".

# How to Use:
To use this program, you need to follow the steps mentioned below:

1. Clone the repository on your local machine.
2. Make sure you have Python installed on your machine. If not, install it from https://www.python.org/downloads/
3. Install required libraries, i.e., "random", "IPython.display", and "json".
4. Update the file paths for the bigram file, input file, and final bigram frequency file. You can update the file paths in the if name == 'main': block.
5. Run the code using the command "python Monte-Carlo.py" from the command line.
6. The program will load the given ciphertext, and then it will try every possible combination of keys until it finds the correct one. After the program finishes, it will output the final plaintext and the number of iterations it took to find the correct key.
# Functions:

This program contains the following functions:

search(cipherText, iters): This function takes the ciphertext and the number of iterations as input and returns the key, the best score, and the number of iterations it took to find the correct key.

- swap(key): This function takes a key as input and switches the values of two random values.

- load(filename): This function takes a filename as input and returns the text in the file.

- transform(cipherText, key): This function takes the ciphertext and the key as input and returns the plaintext.

- to_percentage(dictionary): This function takes a dictionary as input and returns the percentage values of the keys in the dictionary.

- all_bigrams(text): This function takes text as input and returns all bigrams in the text.

- score(key, cipherText): This function takes a key and the ciphertext as input and returns the score of the key.

- save_as_json(file): This function takes a file as input and saves the dictionary as a JSON file.

# Conclusion:
This Python program can be used to decode a given ciphertext by utilizing the brute force attack technique. It is a powerful tool for decoding text encrypted using a simple substitution cipher. With the help of this program, you can easily decrypt any ciphertext that uses a simple substitution cipher.
