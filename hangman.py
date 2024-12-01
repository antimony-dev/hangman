# import mysql.connector as sb
# import turtle
# import random
# import sys
# window= turtle.Screen().setup(300,400)
# t = turtle.Turtle()
# print('Welcome To The Classic Game Of Hangman!')
# global name
# name=input('Enter Your Name : ')
# con=sb.connect(host='localhost',username='root',passwd='sbchad',database='hangman')
# cur=con.cursor(buffered=True)
# global wg
# wg=''
# global guessed
# guessed=''
# global wrong
# wrong=0
# global correct
# correct=0
# def fruits():
#     print('\nHint ! Word Is Name Of A Fruit.\n')
#     sample=('''apple banana grape strawberry orange pineapple mango watermelon kiwi lemon pear pomegranate guava papaya cherry peach''')
#     return(random.choice(sample.split(' ')))
# def flowers():
#     print('\nHint ! Word Is Name Of A Flower.\n')
#     sample=('''rose lily hibiscus marigold lotus jasmine tulip daffodil sunflower''')
#     return(random.choice(sample.split(' ')))
# def vegetables():
#     print('\nHint ! Word Is Name Of A Vegetable.\n')
#     sample=('''cucumber onion carrot cabbage eggplant broccoli cauliflower potato pumpkin radish beetroot capsicum''')
#     return(random.choice(sample.split(' ')))
# def movies():
#     print('\nHint ! Word Is Name Of A Movie.\n')
#     sample=('''stree drishyam shershaah kesari sultan dangal krrish pk don bhootnath kick dhoom''')
#     return(random.choice(sample.split(' ')))
# def instruments():
#     print('\nHint ! Word Is Name Of A Musical Instrument.\n')
#     sample=('''flute guitar sitar violin piano tabla dholak harmonium veena''')
#     return(random.choice(sample.split(' ')))
# genre=[fruits,flowers,vegetables,movies,instruments]
# word = random.choice(genre)()
# for i in range(len(word)):
#     print('_', end=' ')

# def end():
#         sys.exit()

# def disprecords():
#     cur.execute("select* from player")
#     final=cur.fetchall()
#     con.commit()
#     for i in final:
#         print(i)
#     end()

# def records(r):
#     global name
#     q1="insert into player (Name,Result) values ('{}','{}')".format(name,r)
#     cur.execute(q1)
#     con.commit()
#     n=input("\nPress <y> to see the previous records\nPress any other key to exit:")
#     print("\n")
#     if n.lower()=='y':
#         disprecords()
#     else:
#         end()

# def won():
#     print('\nThe Word Was :',word)
#     print('''                  
#                                  You won 👍👍👍
#                                HANGMAN Survived 😁.
#                               Thanks For Playing''')
#     records("won")

# def lost():
#     print('\nThe Word Was :',word)
   
    
#     print('''                     
#                                   You Lost 👎👎👎
#                           HANGMAN Was Hanged To Death 😟.
#                                Thanks For Playing''')
#     records("lost")

# def guess(g):
#     global wrong
#     global correct
#     if (g in word):
#         c=word.count(g)
#         for _ in range(c):
#             global guessed
#             guessed+=g
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                     correct+=1
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#             break
#     else:
#         global wg
#         wg+=g
#         if (wrong==0):
#             t.circle(50)
#             t.rt(90)
#             wrong += 1
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#         elif(wrong==1):
#             t.fd(120)
#             t.bk(90)
#             wrong += 1
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#         elif(wrong==2):
#             t.lt(50)
#             t.fd(60)
#             t.bk(60)
#             t.rt(50)
#             wrong += 1
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#         elif(wrong==3):
#             t.rt(50)
#             t.fd(60)
#             t.bk(60)
#             t.lt(50)
#             t.fd(90)
#             wrong+=1
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#         elif(wrong==4):
#             t.lt(50)
#             t.fd(60)
#             t.bk(60)
#             t.rt(50)
#             wrong += 1
#             for char in word:
#                 if (char in list(guessed)):
#                     print(char, end=' ')
#                 else:
#                     print('_', end=' ')
#             guessing(guessed)
#         else:
#             t.rt(50)
#             t.fd(60)
#             t.bk(60)
#             t.lt(50)
#             lost()
# def guessing(guessed):
#     if (len(guessed)==len(set(word))):
#         won()
#     else:
#         g = input('\n\nGuess a Word :')
#         g.lower()
#         if (g.isalpha() and len(g)==1 and g not in list(guessed) and g not in list(wg)):
#             guess(g)
#         elif(g in list(guessed)or g in list(wg)):
#             print('Letter already guessed')
#             guessing(guessed)
#         else:
#             print('Enter only 1 letter')
#             guessing(guessed)
# guessing(guessed)









#mport mysql.connector as sb
# import tkinter as tk
# from tkinter import messagebox, PhotoImage
# import random

# # Connect to the database
# con = sb.connect(host='localhost', username='root', passwd='sbchad', database='hangman')
# cur = con.cursor(buffered=True)

# # Global variables
# guessed = ""
# wrong = 0
# word = ""
# name = ""

# # Start tkinter window
# window = tk.Tk()
# window.title("Hangman - The Ultimate Challenge")
# window.geometry("600x700")
# window.config(bg="#2b2b2b")  # Dark background

# # Canvas for drawing the hangman
# canvas = tk.Canvas(window, width=300, height=300, bg="#2b2b2b", highlightthickness=0)
# canvas.pack(pady=20)

# # Hangman images
# hangman_images = [
#     PhotoImage(file="assets/hangman0.png"),
#     PhotoImage(file="hangman1.png"),
#     PhotoImage(file="hangman2.png"),
#     PhotoImage(file="hangman3.png"),
#     PhotoImage(file="hangman4.png"),
#     PhotoImage(file="hangman5.png"),
#     PhotoImage(file="hangman6.png"),
# ]

# # Display hangman image
# hangman_label = tk.Label(window, bg="#2b2b2b")
# hangman_label.pack()

# # Name input
# name_label = tk.Label(window, text="Enter Your Name:", font=("Helvetica", 16), fg="#ffcc00", bg="#2b2b2b")
# name_label.pack()
# name_entry = tk.Entry(window, font=("Helvetica", 14), width=20)
# name_entry.pack()

# # Word display
# word_display = tk.Label(window, text="", font=("Courier", 36), fg="#ffffff", bg="#2b2b2b")
# word_display.pack(pady=20)

# # Status messages
# status_label = tk.Label(window, text="", font=("Helvetica", 14), fg="#ffcc00", bg="#2b2b2b")
# status_label.pack(pady=10)

# # Guess entry
# guess_label = tk.Label(window, text="Guess a letter:", font=("Helvetica", 16), fg="#ffcc00", bg="#2b2b2b")
# guess_label.pack()
# guess_entry = tk.Entry(window, font=("Helvetica", 14), width=5)
# guess_entry.pack()

# # Game functions
# def fruits():
#     return random.choice("apple banana grape strawberry orange pineapple watermelon kiwi lemon".split())

# def flowers():
#     return random.choice("rose lily hibiscus marigold lotus jasmine tulip daffodil sunflower".split())

# def vegetables():
#     return random.choice("cucumber onion carrot cabbage eggplant broccoli cauliflower potato pumpkin".split())

# def movies():
#     return random.choice("stree drishyam shershaah kesari sultan dangal krrish pk don bhootnath kick".split())

# def instruments():
#     return random.choice("flute guitar sitar violin piano tabla dholak harmonium veena".split())

# # List of genres
# genre = [fruits, flowers, vegetables, movies, instruments]

# # Choose a random word
# def choose_word():
#     global word
#     word = random.choice(genre)()
#     display_word()

# # Display the current word with underscores
# def display_word():
#     global word
#     display = " ".join([char if char in guessed else "_" for char in word])
#     word_display.config(text=display)
#     if "_" not in display:
#         game_won()

# # Game over scenarios
# def game_won():
#     messagebox.showinfo("Game Over", f"Congratulations {name_entry.get()}, you won!")
#     record_result("won")

# def game_lost():
#     messagebox.showinfo("Game Over", f"Sorry {name_entry.get()}, you lost! The word was {word}")
#     record_result("lost")

# # Handle guess input
# def handle_guess():
#     global guessed, wrong
#     letter = guess_entry.get().lower()
    
#     if letter in guessed or len(letter) != 1 or not letter.isalpha():
#         status_label.config(text="Invalid input or already guessed", fg="red")
#         return
    
#     guessed += letter
#     if letter in word:
#         display_word()
#     else:
#         wrong += 1
#         update_hangman_image()
#         if wrong >= 6:
#             game_lost()
#     guess_entry.delete(0, tk.END)

# # Update hangman image
# def update_hangman_image():
#     hangman_label.config(image=hangman_images[wrong])

# # Record result in the database
# def record_result(result):
#     global name
#     name = name_entry.get()
#     q1 = "INSERT INTO player (Name, Result) VALUES (%s, %s)"
#     cur.execute(q1, (name, result))
#     con.commit()
#     if messagebox.askyesno("View Records", "Do you want to see previous records?"):
#         display_records()

# # Display previous records
# def display_records():
#     cur.execute("SELECT * FROM player")
#     records = cur.fetchall()
#     record_window = tk.Toplevel(window)
#     record_window.title("Previous Records")
#     record_window.geometry("300x400")
#     record_window.config(bg="#2b2b2b")
#     records_label = tk.Label(record_window, text="Records:", font=("Helvetica", 16), fg="#ffcc00", bg="#2b2b2b")
#     records_label.pack(pady=10)
#     for record in records:
#         record_label = tk.Label(record_window, text=str(record), font=("Helvetica", 12), fg="#ffffff", bg="#2b2b2b")
#         record_label.pack()

# # Start a new game
# def start_game():
#     global guessed, wrong
#     guessed = ""
#     wrong = 0
#     update_hangman_image()
#     choose_word()
#     status_label.config(text="")
#     guess_entry.delete(0, tk.END)

# # Start game button
# start_button = tk.Button(window, text="Start Game", font=("Helvetica", 16), fg="#ffffff", bg="#4CAF50", command=start_game)
# start_button.pack(pady=10)

# # Guess button
# guess_button = tk.Button(window, text="Submit Guess", font=("Helvetica", 16), fg="#ffffff", bg="#FF5722", command=handle_guess)
# guess_button.pack(pady=10)

# # Run the tkinter main loop
# window.mainloop()




# import pygame
# import random
# import sys

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Hangman Game")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 36)

# # List of words
# words = ["apple", "banana", "grape", "strawberry", "orange", "pineapple", "mango", "watermelon"]
# word = random.choice(words)
# guessed_letters = []
# wrong_guesses = 0
# max_wrong_guesses = 6

# def draw_hangman(wrong_guesses):
#     if wrong_guesses == 1:
#         pygame.draw.circle(screen, BLACK, (400, 200), 30)  # Head
#     elif wrong_guesses == 2:
#         pygame.draw.line(screen, BLACK, (400, 230), (400, 350), 5)  # Body
#     elif wrong_guesses == 3:
#         pygame.draw.line(screen, BLACK, (400, 250), (350, 300), 5)  # Left Arm
#     elif wrong_guesses == 4:
#         pygame.draw.line(screen, BLACK, (400, 250), (450, 300), 5)  # Right Arm
#     elif wrong_guesses == 5:
#         pygame.draw.line(screen, BLACK, (400, 350), (350, 400), 5)  # Left Leg
#     elif wrong_guesses == 6:
#         pygame.draw.line(screen, BLACK, (400, 350), (450, 400), 5)  # Right Leg

# def display_word():
#     display_text = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display_text += letter + " "
#         else:
#             display_text += "_ "
#     return display_text.strip()

# def main():
#     global wrong_guesses
#     clock = pygame.time.Clock()
#     game_over = False

#     while True:
#         screen.fill(WHITE)

#         # Draw the hangman
#         draw_hangman(wrong_guesses)

#         # Display the word
#         word_display = display_word()
#         word_surface = font.render(word_display, True, BLACK)
#         screen.blit(word_surface, (350, 500))

#         # Check for game over
#         if wrong_guesses >= max_wrong_guesses:
#             game_over = True
#             message_surface = font.render("You Lost!", True, RED)
#             screen.blit(message_surface, (300, 100))
#             message_surface = small_font.render(f"The word was: {word}", True, BLACK)
#             screen.blit(message_surface, (250, 200))

#         if set(word) <= set(guessed_letters):
#             game_over = True
#             message_surface = font.render("You Won!", True, RED)
#             screen.blit(message_surface, (300, 100))

#         if game_over:
#             pygame.display.flip()
#             pygame.time.wait(2000)
#             break

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.unicode.isalpha() and len(event.unicode) == 1:
#                     letter = event.unicode.lower()
#                     if letter not in guessed_letters:
#                         guessed_letters.append(letter)
#                         if letter not in word:
#                             wrong_guesses += 1

#         pygame.display.flip()
#         clock.tick(30)

# if __name__ == "__main__":
#     main()






# import pygame
# import numpy as np
# import random
# import mysql.connector as sb
# import sys

# # Database Connection
# con = sb.connect(host='localhost', username='root', passwd='sbchad', database='hangman')
# cur = con.cursor(buffered=True)

# # Initialize Pygame
# pygame.init()

# # Screen Dimensions and Colors
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# GRAY = (200, 200, 200)

# # Set up the game window
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Hangman Game")

# # Load Hangman Images
# HANGMAN_IMAGES = [pygame.image.load(f"assets/hangman{i}.png") for i in range(7)]

# # Fonts
# FONT_LARGE = pygame.font.Font(None, 60)
# FONT_MEDIUM = pygame.font.Font(None, 40)
# FONT_SMALL = pygame.font.Font(None, 30)

# # Word Categories
# CATEGORIES = {
#     "Fruits": ["apple", "banana", "grape", "orange", "kiwi"],
#     "Flowers": ["rose", "lily", "tulip", "daisy", "orchid"],
#     "Movies": ["inception", "titanic", "avatar", "joker", "matrix"],
#     "Instruments": ["guitar", "violin", "flute", "piano", "tabla"]
# }

# # Game Variables
# word = ""
# guessed = []
# wrong_guesses = 0
# MAX_WRONG = 6
# player_name = ""

# # Functions
# def choose_word():
#     """Randomly select a word from categories."""
#     category = random.choice(list(CATEGORIES.keys()))
#     return random.choice(CATEGORIES[category])

# def draw_hangman():
#     """Draw the current state of the hangman."""
#     screen.blit(HANGMAN_IMAGES[wrong_guesses], (WIDTH // 2 - 150, 100))

# def draw_word():
#     """Display the word with guessed letters or underscores."""
#     display_word = [letter if letter in guessed else "_" for letter in word]
#     text = FONT_LARGE.render(" ".join(display_word), True, BLACK)
#     screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 400))

# def draw_status(message, color=RED):
#     """Display the status message on the screen."""
#     text = FONT_MEDIUM.render(message, True, color)
#     screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 500))

# def game_over(won):
#     """Handle game over state."""
#     screen.fill(WHITE)
#     if won:
#         text = FONT_LARGE.render(f"Congratulations {player_name}, You Won!", True, GREEN)
#     else:
#         text = FONT_LARGE.render(f"Game Over! The word was {word}.", True, RED)
#     screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
#     pygame.display.flip()
#     pygame.time.wait(3000)
#     record_result("won" if won else "lost")
#     reset_game()

# def record_result(result):
#     """Record the player's result in the database."""
#     query = "INSERT INTO player (Name, Result) VALUES (%s, %s)"
#     cur.execute(query, (player_name, result))
#     con.commit()

# def reset_game():
#     """Reset the game state."""
#     global word, guessed, wrong_guesses
#     word = choose_word()
#     guessed = []
#     wrong_guesses = 0

# def draw_guess_letters():
#     """Draw guessed letters on the screen."""
#     guessed_text = FONT_SMALL.render(f"Guessed Letters: {' '.join(guessed)}", True, BLACK)
#     screen.blit(guessed_text, (10, HEIGHT - 50))

# # Main Game Loop
# def main():
#     global word, guessed, wrong_guesses, player_name

#     # Input Player's Name
#     player_name = input("Enter your name: ").strip()

#     # Choose a word
#     word = choose_word()

#     # Pygame Clock
#     clock = pygame.time.Clock()
#     running = True
#     status_message = ""

#     while running:
#         screen.fill(WHITE)
#         draw_hangman()
#         draw_word()
#         draw_guess_letters()

#         if wrong_guesses >= MAX_WRONG:
#             game_over(False)
#         elif "_" not in [char if char in guessed else "_" for char in word]:
#             game_over(True)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#                 sys.exit()

#             if event.type == pygame.KEYDOWN:
#                 if event.unicode.isalpha() and len(event.unicode) == 1:
#                     guess = event.unicode.lower()
#                     if guess in guessed:
#                         status_message = "Letter already guessed!"
#                     elif guess in word:
#                         guessed.append(guess)
#                         status_message = "Correct guess!"
#                     else:
#                         guessed.append(guess)
#                         wrong_guesses += 1
#                         status_message = "Wrong guess!"

#         draw_status(status_message)
#         pygame.display.flip()
#         clock.tick(30)

# if __name__ == "__main__":
#     main()





# import pygame
# import random
# import sys
# import mysql.connector as sb
# from datetime import datetime

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Hangman Game")

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (200, 200, 200)
# RED = (255, 50, 50)
# GREEN = (50, 255, 50)
# YELLOW = (255, 255, 50)

# # Fonts
# FONT_LARGE = pygame.font.SysFont("comicsans", 50)
# FONT_MEDIUM = pygame.font.SysFont("comicsans", 40)
# FONT_SMALL = pygame.font.SysFont("comicsans", 30)

# # Database connection
# con = sb.connect(
#     host="localhost",
#     username="root",  # Your username
#     passwd="sbchad",  # Your password
#     database="hangman"
# )
# cur = con.cursor(buffered=True)

# # Fetching words and categories
# def fetch_words():
#     cur.execute("SELECT category, word FROM words")
#     rows = cur.fetchall()
#     words = {}
#     for category, word in rows:
#         if category not in words:
#             words[category] = []
#         words[category].append(word)
#     return words

# # Log player result
# def log_result(player_name, result):
#     played_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     cur.execute(
#         "INSERT INTO player (name, played_on, result) VALUES (%s, %s, %s)",
#         (player_name, played_on, result)
#     )
#     con.commit()

# # Game variables
# WORDS = fetch_words()
# CATEGORIES = list(WORDS.keys())
# selected_category = random.choice(CATEGORIES)
# selected_word = random.choice(WORDS[selected_category])
# guessed_letters = []
# wrong_guesses = 0
# MAX_WRONG_GUESSES = 6

# # Hangman positions
# HANGMAN_PIECES = [
#     (450, 260, 30, 0),  # Head
#     (450, 290, 450, 400),  # Body
#     (450, 320, 410, 360),  # Left arm
#     (450, 320, 490, 360),  # Right arm
#     (450, 400, 420, 460),  # Left leg
#     (450, 400, 480, 460),  # Right leg
# ]

# def draw_scaffold():
#     """Draws the hangman scaffold."""
#     pygame.draw.line(screen, GRAY, (300, 600), (500, 600), 5)  # Base
#     pygame.draw.line(screen, GRAY, (400, 600), (400, 200), 5)  # Vertical pole
#     pygame.draw.line(screen, GRAY, (400, 200), (450, 200), 5)  # Horizontal pole
#     pygame.draw.line(screen, GRAY, (450, 200), (450, 230), 5)  # Rope

# def draw_hangman(wrong_guesses):
#     """Draws the hangman figure based on the number of wrong guesses."""
#     for i in range(wrong_guesses):
#         piece = HANGMAN_PIECES[i]
#         if i == 0:  # Draw head
#             pygame.draw.circle(screen, RED, (piece[0], piece[1]), piece[2], 5)
#         else:  # Draw limbs
#             pygame.draw.line(screen, RED, (piece[0], piece[1]), (piece[2], piece[3]), 5)

# def draw_word():
#     """Displays the word with blanks and correct guesses."""
#     display_word = ""
#     for letter in selected_word:
#         if letter in guessed_letters:
#             display_word += f"{letter} "
#         else:
#             display_word += "_ "
#     word_surface = FONT_LARGE.render(display_word.strip(), True, YELLOW)
#     screen.blit(word_surface, (50, 450))

# def draw_message(message, color, y_offset=0):
#     """Displays a message at the center of the screen."""
#     msg_surface = FONT_MEDIUM.render(message, True, color)
#     msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
#     screen.blit(msg_surface, msg_rect)

# def display_category():
#     """Displays the selected category."""
#     category_surface = FONT_SMALL.render(f"Category: {selected_category.title()}", True, GREEN)
#     screen.blit(category_surface, (50, 50))

# def reset_game():
#     """Resets the game variables for a new round."""
#     global selected_category, selected_word, guessed_letters, wrong_guesses
#     selected_category = random.choice(CATEGORIES)
#     selected_word = random.choice(WORDS[selected_category])
#     guessed_letters = []
#     wrong_guesses = 0

# # Main game loop
# def game_loop(player_name):
#     global wrong_guesses
#     clock = pygame.time.Clock()
#     running = True

#     while running:
#         screen.fill(BLACK)  # Set background to black
#         draw_scaffold()
#         draw_hangman(wrong_guesses)
#         draw_word()
#         display_category()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.unicode.isalpha() and len(event.unicode) == 1:
#                     guess = event.unicode.lower()
#                     if guess in guessed_letters:
#                         continue
#                     guessed_letters.append(guess)
#                     if guess not in selected_word:
#                         wrong_guesses += 1

#         # Check game over conditions
#         if wrong_guesses == MAX_WRONG_GUESSES:
#             draw_message("You Lost! Press R to Retry", RED)
#             pygame.display.flip()
#             log_result(player_name, "Lost")
#             wait_for_retry()
#             reset_game()
#         elif all(letter in guessed_letters for letter in selected_word):
#             draw_message("You Won! Press R to Retry", GREEN)
#             pygame.display.flip()
#             log_result(player_name, "Won")
#             wait_for_retry()
#             reset_game()

#         pygame.display.flip()
#         clock.tick(30)

# def wait_for_retry():
#     """Waits for the user to press R to retry."""
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#                 return

# # Get player name and run the game
# print("Welcome to Hangman!")
# player_name = input("Enter your name: ")
# game_loop(player_name)








import socket
import threading
import random
import pygame
import sys

# Game Variables
HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024
WORDS = ["python", "network", "socket", "programming", "hangman"]
MAX_WRONG_GUESSES = 6

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
FONT_LARGE = pygame.font.SysFont("comicsans", 50)
FONT_SMALL = pygame.font.SysFont("comicsans", 30)

# Pygame screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Hangman")

# Hangman scaffold positions
HANGMAN_PIECES = [
    (400, 150, 30, 0),  # Head
    (400, 180, 400, 300),  # Body
    (400, 210, 370, 250),  # Left arm
    (400, 210, 430, 250),  # Right arm
    (400, 300, 370, 360),  # Left leg
    (400, 300, 430, 360),  # Right leg
]

# Helper functions
def draw_scaffold():
    """Draws the hangman scaffold."""
    pygame.draw.line(screen, WHITE, (300, 500), (500, 500), 5)  # Base
    pygame.draw.line(screen, WHITE, (400, 500), (400, 150), 5)  # Vertical pole
    pygame.draw.line(screen, WHITE, (400, 150), (450, 150), 5)  # Horizontal pole
    pygame.draw.line(screen, WHITE, (450, 150), (450, 180), 5)  # Rope

def draw_hangman(wrong_guesses):
    """Draws the hangman figure based on wrong guesses."""
    for i in range(wrong_guesses):
        piece = HANGMAN_PIECES[i]
        if i == 0:  # Head
            pygame.draw.circle(screen, RED, (piece[0], piece[1]), piece[2], 5)
        else:  # Body parts
            pygame.draw.line(screen, RED, (piece[0], piece[1]), (piece[2], piece[3]), 5)

def draw_word(word, guessed_letters):
    """Displays the word with blanks and correct guesses."""
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    word_surface = FONT_LARGE.render(display_word, True, YELLOW)
    screen.blit(word_surface, (50, 400))

def draw_message(message, color, y_offset=0):
    """Displays a message at the center of the screen."""
    msg_surface = FONT_SMALL.render(message, True, color)
    msg_rect = msg_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(msg_surface, msg_rect)

def run_server():
    """Server code to handle multiplayer logic."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Server started, waiting for players...")
    
    clients = []
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    def client_handler(conn, addr):
        nonlocal word, guessed_letters, wrong_guesses
        print(f"Player connected: {addr}")
        conn.send(f"Welcome to Hangman! The word has {len(word)} letters.".encode())

        while True:
            data = conn.recv(BUFFER_SIZE).decode()
            if not data:
                break
            print(f"Player {addr} guessed: {data}")

            if data in guessed_letters:
                conn.send("You already guessed that letter.".encode())
            elif data in word:
                guessed_letters.append(data)
                conn.send("Correct guess!".encode())
            else:
                guessed_letters.append(data)
                wrong_guesses += 1
                conn.send("Wrong guess.".encode())

            if all(letter in guessed_letters for letter in word):
                conn.send("You Won!".encode())
                break
            if wrong_guesses >= MAX_WRONG_GUESSES:
                conn.send("You Lost!".encode())
                break

        conn.close()
        print(f"Player {addr} disconnected.")

    while len(clients) < 2:
        conn, addr = server.accept()
        clients.append(conn)
        threading.Thread(target=client_handler, args=(conn, addr)).start()

def run_client():
    """Client code to interact with the server."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connected to the server.")
    
    def listen_to_server():
        while True:
            message = client.recv(BUFFER_SIZE).decode()
            print(f"Server: {message}")
            if "You Won!" in message or "You Lost!" in message:
                break

    threading.Thread(target=listen_to_server).start()

    while True:
        guess = input("Enter your guess: ")
        client.send(guess.encode())

# Main loop
def main():
    """Game initialization and multiplayer choice."""
    print("Welcome to Multiplayer Hangman!")
    choice = input("Type 'server' to start a server or 'client' to join a game: ").lower()
    
    if choice == "server":
        run_server()
    elif choice == "client":
        run_client()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
