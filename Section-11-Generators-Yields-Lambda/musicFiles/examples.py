text = "what have the romans done for us?"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)