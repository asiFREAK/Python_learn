# Write a function that takes a dictionary and returns a new dictionary containing only the key-value
# pairs where the key is a palindrome.

def palindrome_dict(d):
    new_dict = {}
    for key, value in d.items():
        if key.lower() == key[::-1].lower():
            new_dict[key] = value
    return new_dict

d = {'risir' : 1 , 'heleh' : 2 , 'hello' : 3}
print(palindrome_dict(d))