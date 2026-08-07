# freeCodeCamp Studies
Exercises and Projects developed on freeCodeCamp

This repository is being developed as my first "actual" project for my portfolio. Also, I've decided to use this README.md document as a notebook where I can register contet that seems worth taking notes of.

## Module 1 - Python Basics

Since I'm looking into becoming some what of a Data Analyst, I find it important to state register that Pandas and NumPy are two important libraries commonly used on this specific area.

The isinstance( ) function is useful when it is necessary to verify that a particular variable is a specific type before performing operations on it.

In order to be able to write quotation marks inside a string we have to use a backslash right before these characters. Like this: 'This is how it's done \'That's whats she said\''. Although it is easier to just alternate between both types of quotation marks, wich also works.

Always remember the F-strings print(f' { } ')

Common string methods:
- .upper()
- .lower()
- .strip()
- .replace(old, new)
- .find(substring)
- .count()
- .capitalize()
- .tittle()

Augmented Assignments:
- +=
- -=
- *=
- /=
- //=
- %=
- **=

### Now I'm seeing conditional and logical operators:

- IF, ELIF, ELSE
- ==. !=, <, >, <=, >=, and, or

### I've reached Functions and Scope

To correctly determine scope, Python follows the LEGB rule, which stands for the following:

Local scope (L): Variables defined in functions or classes.

Enclosing scope (E): Variables defined in enclosing or nested functions.

Global scope (G): Variables defined at the top level of the module or file.

Built-in scope (B): Reserved names in Python for predefined functions, modules, keywords, and objects.

## Exercise 5 description

\# Declaring the caesar encriptation function
def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if not if not 0 <= shift <= 25:
        return 'Shift must be an integer between 0 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

# This is a rotating function string. It takes the shift value and reorganizes the order of the letters, thus, making the caesar cipher work.
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    encrypted_text = text.translate(translation_table)
    return encrypted_text

# This functions applies the caesar cipher to the text
def encrypt(text, shift):
    return caesar(text, shift)

# This function deciphers the text
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# Decription example
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

decrypted_text = decrypt(encrypted_text, 13)

print(decrypted_text)\n
