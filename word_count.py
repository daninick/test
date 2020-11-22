filename = input('''
This program returns the words in a .txt file and their count in it.


Enter a .txt file name: ''')
f = open(filename, 'r')

text = f.read()
text = text.replace('\n', ' ')
words = sorted(text.split(' '))
d = {}
for word in words:
    if word not in d.keys():
        d[word] = 1
    else:
        d[word] = d[word] + 1
print('''

The words in the file are: ''')
for key in d.keys():
    print(f"{key}: {d[key]}")
print(f'''
Total unique words used: {len(d)}''')