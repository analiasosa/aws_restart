frase = input ("Colocar una frase")   
letra = input ("Colocar una letra")
count = 0 
for i in frase:
    if i == letra:
        count = count + 1
print(count)