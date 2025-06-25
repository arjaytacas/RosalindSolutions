# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.

# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b] and s[d] in our slice.

# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102
# Sample Output
# Humpty Dumpty

# To solve first we declare the dataset and the indices
dataset = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
a, b, c, d = 22, 27, 97, 102

# print and cut it we add +1 to b and d because the problem states that the cut should include s[b] and s[d].
print(f'{dataset[a:b+1]} {dataset[c:d+1]}')
