Digital Library System for Distinct Keyword Search and Indexing
A Python-based digital library tool designed to manage text and book data, enabling efficient keyword indexing and retrieval. This system uses custom-built hash tables for handling keywords, providing collision resolution through chaining, linear probing, and double hashing.

Project Overview
The Digital Library System is designed to create a unique, compressed dictionary of keywords from any given book or text, facilitating fast and efficient searches. By implementing core data structures 
(HashMap and HashSet) from scratch, this project allows for fine-tuned control over collision handling, load factor thresholds, and dynamic resizing. The project serves as a practical application of 
hash table theory, avoiding reliance on built-in Python libraries.

Features
Distinct Keyword Indexing: Generates a unique set of keywords from input text for efficient retrieval.
Custom Hash Functions: Implements polynomial accumulation and other custom hash functions.
Collision Handling Techniques:
Chaining: Uses linked lists to manage collisions in the hash table.
Linear Probing: Resolves collisions by finding the next available slot.
Double Hashing: Uses secondary hash functions for efficient conflict resolution.
Dynamic Resizing: Resizes hash tables based on load factors to maintain efficiency.
Memory Optimization: Only rehashes elements when load thresholds are exceeded.


Technologies Used
Python: Core language used for development.
Data Structures: Custom HashMap and HashSet with advanced collision-handling techniques.

Usage
Adding Text/Books: Load text files into the system using the provided upload functionality in main.py.
Indexing: The program parses the input text and indexes keywords in the custom hash tables.
Keyword Search: Use the search function to retrieve pages, sections, or passages containing specific keywords.
Dynamic Resizing: The system will automatically resize the hash table when a predefined load factor is exceeded.

Example
python

# Example of adding a book and searching for keywords
# find =JGBLibrary("Bezos",(5,4,4,50))
# text=["Harry", "Potter", "is", "about", "a", "young", "wizard", "facing", "adventures", "with", "his", "friends", "against", "dark", "forces"]
# find.add_book("HarryPotter",text)
# print(find.distinct_words("HarryPotter"))
# print(find.count_distinct_words("HarryPotter"))
# print(find.search_keyword("is"))
# find.print_books()
