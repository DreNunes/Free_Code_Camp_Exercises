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

## Loops

### Lists
Lists []: mutable
list(x)
.append
.pop
.sort
.extend
.insert
.remove
.clear
.sort
.reverse
.index

### Tuples
Tuples(): immutable
tuple(x)
If you need to collect any remaining elements from a tuple, you can use the asterisk (*)
.count
.index

for
while

The range function is used to generate a sequence of integers. Stop is the only required argument.

range(start, stop, setp)

Enumerate(x, 1): creates a tuple as index

The zip() function combines lists into pairs of elements and returns an iterator of tuples

List comprehension allows us to create new lists is a single line by combining a loop and a condition directly with []

filter functio: filter() checks a condition

map function: map() takes an iterable and applies a function to each of its elements

sum function: sum() gives us the sum of the elements on an iterable, can take start positions

lmbda :Lambda functions are anonymous functions that can be called in a single line and cannot be called again later. The're ideal for cases such as higher order functions

### Dictionaries

Dictionaries are built-in data structures that store collections of key-value pairs. They work very similarly to real dictionaries, where you search for a word to find its corresponding meaning.

dictionary = {
    key1: value1,
    key2: value2
}

dictionary[key]

The .get() method retrieves the value associated with a key

The .clear() method removes all the key-value pairs from the dictionary

The .pop() method removes the key-value pair with the key specified as the first argument and returns its value

The .update() method updates the key-value pairs with the key-value pairs of another dictionary

### Sets

stes = mutable, unordered {}

| = union operator

& = intersection operator

- = difference operator

^ = symmetric difference operator

### Modules

Some examples of popular built-in modules are math, random, re (short for "regular expressions"), and datetime.

The math module has helpful functions for performing more complex mathematical operations.

The random module is helpful for generating random numbers.

The re module is used for working with regular expressions.

And the datetime module is helpful for working with dates and times in Python.

import module_name

module_name.function_name()

import as

from module_name import name1, name2

__name__ is a special built-in variable in Python

When a Python file is executed directly, Python sets the value of this variable to the string "__main__"
