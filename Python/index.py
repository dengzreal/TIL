word = "Python"

print(word[0])
print(word[1])
print(word[-1])
print(word[-2])
print(word[0:2])
print(word[:2])
print(word[2:])

#is not operate
word[0] = 'j'

#correct grammer
word = 'j' + word[1:]