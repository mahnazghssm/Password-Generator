"""
Author: Mahnaz Ghassemi
Date created: 14,07,2024
Description: Password Generator
"""


import random
import string
from abc import ABC, abstractmethod

import nltk  # type: ignore

# Download the list of words from the NLTK corpus
nltk.download("words")

class PasswordGenerator(ABC):
    """Abstract base class for password generators."""
    
    @abstractmethod
    def generator(self) -> str:
        """Method to generate a password. Must be implemented by subclasses."""
        pass

class PinGeneratorPassword(PasswordGenerator):
    """Password generator for numeric PINs."""
    
    def __init__(self, length: int):
        """
        Initialize the PIN generator with a specific length.
        
        :param length: Length of the PIN
        """
        self.length = length 

    def generator(self) -> str:
        """
        Generate a numeric PIN of the specified length.
        
        :return: A string representing the numeric PIN
        """
        return "".join([random.choice(string.digits) for _ in range(self.length)])

class RandomPasswordGenerator(PasswordGenerator):
    """Password generator that creates random passwords with optional numbers and symbols."""
    
    def __init__(
        self,
        include_numbers: bool = False,
        include_symbols: bool = False,
        length: int = 8
    ):
        """
        Initialize the random password generator with optional numbers and symbols.
        
        :param include_numbers: Whether to include numbers in the password
        :param include_symbols: Whether to include symbols in the password
        :param length: Length of the password
        """
        self.include_numbers = string.digits
        self.include_symbols = string.punctuation
        self.length = length
        self.characters = string.ascii_letters

        if include_numbers:
            self.characters += self.include_numbers
        if include_symbols:
            self.characters += self.include_symbols

    def generator(self) -> str:
        """
        Generate a random password based on the specified criteria.
        
        :return: A string representing the random password
        """
        return "".join([random.choice(self.characters) for _ in range(self.length)])
        

class MemorablePasswordGenerator(PasswordGenerator):
    """Password generator for memorable passwords using words."""
    
    def __init__(
        self,
        number_of_words: int = 4,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: list = None
    ):
        """
        Initialize the memorable password generator with a list of words.
        
        :param number_of_words: Number of words to include in the password
        :param separator: Separator between words in the password
        :param capitalization: Whether to capitalize words randomly
        :param vocabulary: List of words to use for the password. If None, use NLTK words.
        """
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalization = capitalization
        self.vocabulary = vocabulary

    def generator(self) -> str:
        """
        Generate a memorable password based on the specified criteria.
        
        :return: A string representing the memorable password
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.number_of_words)]
        if self.capitalization:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]

        return self.separator.join(password_words)

if __name__ == "__main__":
    # Create an instance of PinGeneratorPassword with a PIN length of 10
    p = PinGeneratorPassword(length=10)
    # Generate and print the PIN
    print(p.generator())