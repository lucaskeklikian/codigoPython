text = "texto de prueba"
words = text.split()
cantWords=len(words)
letters = len(text)- text.count(" ")
prom = letters/cantWords
print(prom)