import random

# ====== HARDCORE ASCII TITLE ======
print(r"""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

        💀 ALPHA EDITION 💀
""")

# ====== WORDS (EDIT THESE FOR PERSONAL TOUCH) ======
words = [
    "warrior",
    "king",
    "champion",
    "beast",
    "mine",
    "forever",
    "husband",
    "protector"
]

word = random.choice(words)
guessed = []
lives = 6

hangman_stages = [
"""
   _______
   |     |
   |
   |
   |
   |
========= """,
"""
   _______
   |     |
   |     O
   |
   |
   |
========= """,
"""
   _______
   |     |
   |     O
   |     |
   |
   |
========= """,
"""
   _______
   |     |
   |     O
   |    /|
   |
   |
========= """,
"""
   _______
   |     |
   |     O
   |    /|\\
   |
   |
========= """,
"""
   _______
   |     |
   |     O
   |    /|\\
   |    /
   |
========= """,
"""
   _______
   |     |
   |     O
   |    /|\\
   |    / \\
   |
========= """,
]

print("Welcome, Alpha.")
print("Guess the word. Prove your dominance.\n")

# ====== GAME LOOP ======
while lives > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Lives left:", lives)
    print(hangman_stages[6 - lives])

    if "_" not in display:
        print("\n🔥 YOU WIN, KING 🔥")
        print("You conquered it. Just like you conquered my heart.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed. Stay sharp.")
        continue

    guessed.append(guess)

    if guess not in word:
        lives -= 1
        print("Wrong move. Real men adapt.")

if lives == 0:
    print(hangman_stages[6])
    print("\n💀 GAME OVER 💀")
    print("Even kings fall sometimes.")
    print("But you’ll always be my favorite warrior.")

