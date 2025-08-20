"""Find palindromes in a dictionary file"""
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

def recursion(item):
    if len(item) <= 1:
        return True
    
    if item[0] != item[-1]:
        return False

    return recursion(item[1:-1])
            

# for word in word_list:
#     if len(word) > 1 and word == word[::-1]:
#         print(list(word))
#         # print(f"{word} + {word[::1]}")
#         pali_list.append(word)

for word in word_list:
    if recursion(word):
        pali_list.append(word)
    

print(f"\nNumber of palindromes found = {len(pali_list)}\n")
print(*pali_list, sep="\n")