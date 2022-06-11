
text = input("Ingresar texto:")
letter = input("Ingresar letra:")

num = text.count(letter)

porc = int((num/(len(text)))*100)

print("Porcentaje de la letra respecto del texto:",porc,"%")