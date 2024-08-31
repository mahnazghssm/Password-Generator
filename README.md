# Password Generator

This Python project implements various password generators using different strategies. The generators are designed to create secure passwords for different use cases, such as numeric PINs, random passwords with optional symbols, and memorable passwords using words. 

## Project Structure
```
password-generator/
|
|– game.py         # The main script implementing the password generators
|
|– README.md       # This file
```
## Requirements

- Python 3.7 or higher
- NLTK library (Natural Language Toolkit)

You can install the required library using:

```bash
pip install nltk
```
## How to Run
python game.py

Password Generators

1. PinGeneratorPassword
```

Generates numeric PINs of a specified length.

Usage:

p = PinGeneratorPassword(length=10)
print(p.generator())

Constructor Parameters:

- length (int): The length of the numeric PIN.

Method:

- generator() -> str: Returns a numeric PIN of the specified length.

 ```

2. RandomPasswordGenerator
```

Generates random passwords with optional inclusion of numbers and symbols.

Usage: 

p = RandomPasswordGenerator(include_numbers=True, include_symbols=True, length=12)
print(p.generator())

Constructor Parameters:

- include_numbers (bool): Whether to include numbers in the password.
- include_symbols (bool): Whether to include symbols in the password.
- length (int): The length of the password.

Method:

- generator() -> str: Returns a random password based on the specified criteria.
``` 
3. MemorablePasswordGenerator
```

Generates memorable passwords using a list of words.
p = MemorablePasswordGenerator(number_of_words=4, separator='-', capitalization=True)
print(p.generator())

Constructor Parameters:

- number_of_words (int): Number of words to include in the password.
- separator (str): Separator between words.
- capitalization (bool): Whether to randomly capitalize words.
- vocabulary (list): List of words to use for generating the password. Uses NLTK words by default.

Method:

- generator() -> str: Returns a memorable password based on the specified criteria.
```

## example 

# Example usage of PinGeneratorPassword
```
p = PinGeneratorPassword(length=10)
print(p.generator())  # Outputs a 10-digit PIN
```

# Example usage of RandomPasswordGenerator
```
p = RandomPasswordGenerator(include_numbers=True, include_symbols=True, length=12)
print(p.generator())  # Outputs a random password of length 12 with numbers and symbols
```

# Example usage of MemorablePasswordGenerator
```
p = MemorablePasswordGenerator(number_of_words=4, separator='-', capitalization=True)
print(p.generator())  # Outputs a memorable password with 4 words, separated by hyphens, with random capitalization
```
