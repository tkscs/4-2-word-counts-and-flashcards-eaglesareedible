"""
INSTRUCTIONS:
The code below has a lot of repetition. Use a dictionary and a for loop to 
make the code more compact.
"""

def pad_word_count(essay):
    """
    Parameters:
    essay (str): the original essay

    Returns:
    str: a new essay with more words
    """
    # Initialize new essay to match the original.
    # We will update it and re-assign this variable later.
    new_essay = essay

    new_essay = new_essay.replace("n't", " not")
    new_essay = new_essay.replace("'s", " is")
    new_essay = new_essay.replace("'re", " are")
    new_essay = new_essay.replace("'ve", " have")
    #### STOP REPLACING CODE HERE

    return new_essay

# Here's the function call.
# Don't change this.
print(pad_word_count(
  """
  Cats are cute.
  They've been pets for thousands of years.
  They're playful and cuddly, but they don't need as much attention as dogs.
  It's clear that they're silly, and they love knocking things over.
  It isn't possible to see a cat and not want to cuddle it.
  That's all I have to say about cats."""
))