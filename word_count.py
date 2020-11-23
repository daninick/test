import re


filename = input('''
This program returns the words in a .txt file and their count in it.


Enter a .txt file name: ''')
f = open(filename, 'r')

# Read the file and convert it to a string
text = f.read()

# Ignore the empty lines
text = text.replace('\n', ' ')

# All words in the text are separated by space now.
# Make a list of all words in the text using regular expressions.
words = re.findall(r'\w+',text,re.I)

# Create an empty dictionary
d = {}

# For every word in the list of words check if the word exists in the dictionary.
# If it doesn't exist -> add it as a key and set a count of 1 as a value.
# If the word exists in the dictionary -> simply increase the count with 1.
for word in words:
    word = word.lower()

# finds the items that contain a digit and do not put them in the dictionary.
# I presume the words has only word characters and no numbers
    match = re.search(r'\d',word)
    if match:
        pass
    else:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] = d[word] + 1

# Prints on the terminal all words and their count even the count of the keywords, alphabetically sorted.
print('''

The words in the file are: ''')

for key in sorted(d.keys()):
    print(f"{key}: {d[key]}")
print(f'''
Total unique words used: {len(d)}''')