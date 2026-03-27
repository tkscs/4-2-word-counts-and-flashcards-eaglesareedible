import string
text = """
Belong
Kehillah commits to creating and holding a welcoming space for all students to
come as they are, express their diverse identities, build community, and forge
meaning relationships with faculty and peers. We understand that a sense of
belonging is the foundation for deep learning, risk-taking, and individuality.
As we create this space for each student, they can help create it for others.

Build

Learning at Kehillah is not a passive act --- it's a co-constructed cycle of
discovery, challenge, and growth. Our expert faculty, deeply attuned to
adolescent development and progressive education practices, partner with
students to build academic prowess, self-refleciton, agency, wellness,
character, and joy.

Become

Kehillah is a launchpad for purpose. Our graduates leave not just prepared for
top universities, but as compassionate individuals who define success through
achievement, contribution, and character. Grounded in curiosity and integrity,
they are ready to navigate complexity, think critically, and drive meaningful
change in their communities and beyond.
"""

# Make a dictionary where the keys are all the unique words in the string
# (Hint: use the `.split()` method to get a list of all the words) and the
# values are the number of times each word appears. Print the dicitonary.

# 1. Remove all new lines and punctuation, and convert to all lowercase.
newtext = ""
text.lower()
for i in text:
    if i in string.ascii_letters:
        newtext+=i
    elif i == " ":
        newtext+=i
    elif i == "\n":
        newtext += " "

# 2. Use the `.split()` method to split into a list of words.
#### YOUR CODE HERE
newtext = newtext.split(' ')

# 3. Initialize an empty dictionary to keep track of word counts.
#### YOUR CODE HERE
dictionary={}
# 4. loop through the list of words and update the dictionary. If the word is
# already a key in the dicitonary, increment the count. If not, add the new key
# with a count of 1.
#### YOUR CODE HERE
for b in newtext:
    if b in dictionary:
        dictionary[b] += 1
    else:
        dictionary[b] =1
print(dictionary)