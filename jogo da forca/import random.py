import random

def choose_word():
    words = {
        "linguagens_de_programacao": ["python", "java", "javascript", "ruby", "php"],
        "linguagens_web": ["html", "css", "javascript", "php"],
        "linguagens_mobile": ["swift", "java", "kotlin", "flutter", "reactnative"]
    }
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    return word, category

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word, category = choose_word()
    guessed_letters = []
    attempts = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra pertence à categoria:", category.replace("_", " ").title())
    print("Adivinhe a palavra:")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Digite uma letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Letra errada. Você tem {} tentativas restantes.".format(attempts))
            if attempts == 0:
                print("Você perdeu! A palavra era:", word)
                break
        else:
            print("Letra correta!")

        displayed = display_word(word, guessed_letters)
        print(displayed)

        if "_" not in displayed:
            print("Parabéns! Você ganhou!")
            break

if __name__ == "__main__":
    hangman()

