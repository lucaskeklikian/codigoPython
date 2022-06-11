def concatenate(*args):
   
    delim = "-"
  
    # para unir se usa delim

    res = delim.join(map(str, args))
    
    return str (res)

print(concatenate("I", "love", "Python", "!"))