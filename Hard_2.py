def shortest(s):
    def palindrome(word):
        return word == word[::-1]
    n = len(s)
    i = n - 1
    while i >= 0 and not palindrome(s[:i + 1]):
        i -= 1
    return s[i + 1:][::-1] + s
s = input("s=")
output = shortest(s)
print(output)
