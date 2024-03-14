import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_fails = 10
# Lista para almacenar las letras adivinadas
guessed_letters = []
vocales=["a","e","i","o","u"]

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
dificultad=int(input("elija dificiltad: \n ingrese 1. Facil, 2. Media, 3. Dificil "))
while not((dificultad >=1) and (dificultad <=3)):
    print("ingrese un numer de dificiltad entre 1 y 3.")
    dificultad=int(input("elija dificiltad: \n ingrese 1. Facil, 2. Media, 3. Dificil "))
if dificultad==1:
    word_displayed=""
    for letter in secret_word:
        if letter in vocales:
            word_displayed=word_displayed+(letter)
        else :
            word_displayed=word_displayed+("_")
    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")
elif dificultad==2:
    word_displayed=""
    for letter in secret_word:
        if letter is secret_word[0]:
            word_displayed=word_displayed+(letter)
        elif letter is secret_word[-1]:
            word_displayed=word_displayed+(letter)
        else :
            word_displayed=word_displayed+("_")
    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")
elif dificultad==3:
    word_displayed = "_" * len(secret_word)
    # Mostrarla palabra parcialmente adivinada
    print(f"Palabra: {word_displayed}")
i=0
while i<max_fails:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter=="":
        print("Error. Ingrese una letra")
        continue
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    #Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique el cambio.
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        i=i+1
 
    # Mostrar la palabra parcialmente adivinada
    letters = []
    if dificultad==1:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            elif letter in vocales:
                letters.append(letter)
            else:
                letters.append("_")
    elif dificultad==2:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            elif letter is secret_word[0] :
                letters.append(letter)
            elif letter is secret_word[-1]:
                letters.append(letter)
            else:
                letters.append("_")
    elif dificultad==3:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
    
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break
else:
    print(f"¡Oh no! Has alcanzado el numero de fallos permitidos.")
    print(f"La palabra secreta era: {secret_word}")
