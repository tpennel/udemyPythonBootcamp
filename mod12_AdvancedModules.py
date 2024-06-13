# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp/blob/master/12-Advanced%20Python%20Modules/00-Collections-Module.ipynb

from collections import Counter, defaultdict, namedtuple
my_list = [1,1,1,1,1,1,1,1,1,2,2,3,3,3,1,1]
print(Counter(my_list))

senetence = "How many times does each word show up in this senetence with a word"
print(Counter(senetence.split()))

letters = "aaaaaaabbbbcccccccccdddddddd"
count = Counter(letters)
print(count.most_common())
# This is a test. More testing. Hopefully this is the last round. Maybe this worked?