import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False 
while isGuessRight != True: # si el usuario no ha adivinado la respuesta, entra en el  bucle while. 
          guess = input("Guess a number between 1 and 10: ") # pidele al usuario que adivine un numero del 1 al 10. 
          if int(guess) == number: # la suposicion es correcta ? 
            print("You guessed {}. That is correct! You win!".format(guess)) # si es correta y adivino el numero, sale del ciclo. 
            isGuessRight = True
          else:
            print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess)) # si no es correcta, digale que continue en el ciclo. 
