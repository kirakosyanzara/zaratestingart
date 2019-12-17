text="barev bareeeev bareeeeev erkar barev u shaaaaaat ahavooooor shat erkarrrrrrrrrrrrrrrr bareeeeeeeeeeeeeev"
print(text)
words=text.split()
print(words)
number_of_words = len(words)
print(number_of_words)
print(words)
for word in words:
    print(word, len(word))
max_len = len(max(words, key=len))
print(max_len)
print(max(words, key=len))
