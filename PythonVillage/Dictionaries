# Sample Dataset
# We tried list and we tried dicts also we tried Zen

# Sample Output
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1

# declare string and word dictionary
string = 'We tried list and we tried dicts also we tried Zen'
worddic = {}

# split the text using " " and loop through it counting the words
for word in string.split(" "):
    if word in worddic:
        worddic[word] += 1
    else:
        worddic[word] = 1

# key and values are the word and the number it was counted during our loop.
for key, value in worddic.items():
    print(key, value)

# we and We will be counted separately on python unless we specified that lower and uppercase are the same.

