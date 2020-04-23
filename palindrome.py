def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def isPalindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif first(word) == last(word):
        print(first(word), last(word))
        return isPalindrome(middle(word))
    else:
        return False


word = input("digite a palavra : ").upper()
key = isPalindrome(word)
if key:
    print("Esta palavra e um PALINDROME (teste1)")
else:
    print("Esta palavra NAO e um PALINDROME")

if word == word[::-1]:
    print("Esta palavra e um PALINDROME (teste2)")
