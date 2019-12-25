text = str(input ("Enter your text:"))
sentence = text [::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print (sentence_rev)
