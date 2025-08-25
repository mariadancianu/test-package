"""
My First Python Package - A simple example library
"""

__version__ = "0.1.0"
__author__ = "Maria Dancianu"
__email__ = "mariadanci1994@gmail.com"

# Import main functions so users can access them directly
from .core import add_numbers, multiply_numbers, greet_user

__all__ = ['add_numbers', 'multiply_numbers', 'greet_user']