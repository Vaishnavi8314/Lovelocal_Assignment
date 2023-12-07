def last_word(sentence):
   word = sentence.split()
   if not word:
        return 0
   return len(word[-1])
a = input()
word_length = last_word(a)
print(word_length)
