import tkinter as tk
import random


class WordleGame:
    """
    This class represents a Wordle game. It includes methods for creating the game's GUI, handling user input,
    validating the user's guesses, and managing the game's state.
    """

    def __init__(self, master):
        """
        Initializes a new instance of the WordleGame class.

        Args:
            master (tk.Tk): The root window of the game.
        """
        self.master = master
        self.master.title("Wordle")
        self.correct_word = ""
        self.remaining_guesses = 5
        self.current_line = 0
        self.step_labels = []
        self.history_label = None

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the game's GUI.
        """
        self.label = tk.Label(self.master, text="Tahmin etmek istediğiniz kelimeyi girin (5 harfli):")
        self.label.pack()

        self.entry_frame = tk.Frame(self.master)
        self.entry_frame.pack()

        self.entries = []
        for _ in range(5):
            entry_row = []
            for _ in range(5):
                vcmd = (self.master.register(self.validate_entry), '%P')
                entry = tk.Entry(self.entry_frame, width=3, font=('Helvetica', 14), validate='key',
                                 validatecommand=vcmd)
                entry_row.append(entry)
                entry.grid(row=self.current_line, column=len(entry_row) - 1, padx=5, pady=5)
            self.entries.append(entry_row)

            self.current_line += 1

        self.create_keyboard()

        self.submit_button = tk.Button(self.master,
                                       text="Tahmin Et",
                                       command=self.check_guess,
                                       bg="white",
                                       fg="black",
                                       activebackground="red",
                                       activeforeground="white",
                                       font=('Helvetica', 12))
        self.submit_button.pack()

        self.play_again_button = tk.Button(self.master,
                                           text="Yeniden Oyna",
                                           command=self.play_again,
                                           font=('Helvetica', 12))
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)

        self.start_game()

        self.master.bind("<Key>", self.on_key_press)

    def validate_entry(self, P):
        """
        Validates the user's input in the entry fields.

        Args:
            P (str): The proposed new value of the entry field.

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if P.isdigit() or len(P) > 1:
            return False
        return True

    def on_key_press(self, event):
        """
        Handles key press events.

        Args:
            event (tkinter.Event): The event information.
        """
        if event.char.isalpha():
            for entry in self.entries[self.current_line]:
                if not entry.get():
                    entry.insert(tk.END, event.char.lower())
                    entry.focus_set()
                    return
            if self.current_line < 4:
                self.current_line += 1
                self.entries[self.current_line][0].focus_set()
        elif event.keysym == "Return":
            self.check_guess()
        elif event.keysym == "BackSpace":
            self.delete_character()

    def create_keyboard(self):
        """
        Creates the keyboard for the game's GUI.
        """
        self.keyboard_frame = tk.Frame(self.master)
        self.keyboard_frame.pack()

        self.turkish_layout = [
            ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h"],
            ["ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p"],
            ["r", "s", "ş", "t", "u", "ü", "v", "y", "z", "Sil"]
        ]

        self.keyboard_buttons = {}

        for i, row in enumerate(self.turkish_layout):
            row_frame = tk.Frame(self.keyboard_frame)
            row_frame.pack()
            for j, char in enumerate(row):
                if char == 'Sil':
                    button = tk.Button(row_frame, text=char, command=self.delete_character, font=('Helvetica', 12),
                                       width=3, height=2)
                else:
                    button = tk.Button(row_frame, text=char.upper(), command=lambda c=char: self.insert_character(c),
                                       font=('Helvetica', 12), width=3, height=2)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.keyboard_buttons[char] = button

    def delete_character(self):
        """
        Deletes the last character entered by the user.
        """
        for row in reversed(self.entries):
            for entry in reversed(row):
                if entry == self.master.focus_get():
                    if entry.get():
                        entry.delete(len(entry.get()) - 1)
                        next_entry_index = row.index(entry) + 1
                        if next_entry_index < len(row):
                            row[next_entry_index].focus_set()  # İmleci bir sonraki giriş kutusuna getir
                    else:
                        prev_entry_index = row.index(entry) - 1
                        if prev_entry_index >= 0:
                            row[prev_entry_index].focus_set()
                    return

    def insert_character(self, char):
        """
        Inserts a character into the current entry field.

        Args:
            char (str): The character to insert.
        """
        for row_index, row in enumerate(self.entries):
            for entry_index, entry in enumerate(row):
                if entry == self.master.focus_get():
                    if not entry.get():
                        entry.insert(tk.END, char.lower())
                    else:
                        if entry_index < 4:
                            next_entry = row[entry_index + 1]
                            next_entry.focus_set()
                            next_entry.insert(tk.END, char.lower())
                        elif row_index < 4:
                            next_row = self.entries[row_index + 1]
                            next_row[0].focus_set()
                            next_row[0].insert(tk.END, char.lower())
                    return

    def start_game(self):
        """
        Starts a new game.
        """
        self.correct_word = self.get_random_word()
        print("Doğru kelime:", self.correct_word)
        self.remaining_guesses = 5
        self.current_line = 0
        for row in self.entries:
            for entry in row:
                entry.config(state=tk.NORMAL)
                entry.config(bg="white")
        self.submit_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)

        for label in self.step_labels:
            label.destroy()
        self.step_labels = []

        if self.history_label:
            self.history_label.destroy()
            self.history_label = None

        self.label.config(text="Tahmin etmek istediğiniz kelimeyi girin (5 harfli):", fg="black")

        for button in self.keyboard_buttons.values():
            button.config(bg="SystemButtonFace")

        self.master.unbind("<Key>")
        self.master.bind("<Key>", self.on_key_press)

    def get_random_word(self, word_to_check=None):
        """
        Gets a random word from the word list.

        Args:
            word_to_check (str, optional): A specific word to check in the word list.

        Returns:
            str: A random word from the word list.
        """
        with open('kelimeler.txt', 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if len(line) == 6]
        if word_to_check:
            if word_to_check in words:
                return word_to_check
            else:
                print("Böyle bir kelime yoktur. Lütfen tekrar deneyin.")
                return None
        return random.choice(words)

    def check_guess(self):
        """
        Checks the user's guess against the correct word.
        """
        guess = ''
        for row in self.entries[self.current_line]:
            guess += row.get().lower()
        if len(guess) != 5 or not guess.isalpha():
            self.label.config(text="Lütfen 5 harfli bir kelime girin.", fg="red")
            return
        with open('kelimeler.txt', 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if len(line) == 6]
        if guess not in words:
            self.label.config(text="Böyle bir kelime yok. Lütfen tekrar deneyin.", fg="red")
            # Tahmin girişini sıfırla
            for entry in self.entries[self.current_line]:
                entry.delete(0, tk.END)
            self.entries[self.current_line][0].focus_set()  # İmleci ilk giriş kutusuna getir
            return

        self.remaining_guesses -= 1
        self.label.config(text=f"Kalan Tahmin Hakkı: {self.remaining_guesses}")

        new_word = ""
        correct_positions = set()
        for i in range(len(guess)):
            if guess[i] == self.correct_word[i]:
                new_word += guess[i]
                correct_positions.add(i)
            elif guess[i] in self.correct_word:
                new_word += guess[i].upper()
            else:
                new_word += guess[i]
        self.step_labels.append(tk.Label(self.master, text=new_word, font=('Helvetica', 16)))
        self.step_labels[-1].pack()

        self.color_entries(correct_positions, guess)

        if new_word.lower() == self.correct_word:
            self.end_game(True)
        elif self.remaining_guesses == 0:
            self.end_game(False)
        else:
            self.current_line += 1
            if self.current_line == 5:
                self.end_game(False)

    def color_entries(self, correct_positions, guess):
        """
        Colors the entry fields based on the user's guess.

        Args:
            correct_positions (set): A set of indices representing the correct positions in the guess.
            guess (str): The user's guess.
        """
        for i, char in enumerate(guess):
            if char in self.correct_word:
                if i in correct_positions:
                    bg_color = "green"
                else:
                    bg_color = "yellow"
            else:
                bg_color = "gray"

            self.entries[self.current_line][i].config(bg=bg_color)

            if char in self.correct_word:
                if char == guess[self.correct_word.index(char)]:
                    self.keyboard_buttons[char].config(bg="green")
                else:
                    self.keyboard_buttons[char].config(bg="yellow")
            elif char in guess:
                self.keyboard_buttons[char].config(bg="gray")
            else:
                self.keyboard_buttons[char].config(bg="SystemButtonFace")

        for i in range(5):
            for j in range(5):
                if self.entries[self.current_line][j].get() == '':
                    if i in correct_positions:
                        bg_color = "green" if i == correct_positions.intersection(set(range(5)))[0] else "yellow"
                    else:
                        bg_color = "gray"

                    self.entries[self.current_line][j].config(bg=bg_color)

    def end_game(self, is_winner):
        """
        Ends the game.

        Args:
            is_winner (bool): True if the user won the game, False otherwise.
        """
        if is_winner:
            self.label.config(text="Tebrikler! Doğru kelimeyi buldunuz: " + self.correct_word, fg="green")
        else:
            self.label.config(text="Deneme hakkınız kalmadı. Doğru kelime: " + self.correct_word, fg="red")

        self.submit_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL)

    def play_again(self):
        """
        Resets the game to its initial state.
        """
        self.start_game()
        for row in self.entries:
            for entry in row:
                entry.delete(0, tk.END)  # Giriş kutularını temizle
                entry.config(state=tk.NORMAL)  # Giriş kutusunun durumunu NORMAL olarak ayarla
                entry.config(bg="white")  # Giriş kutusunun arka plan rengini beyaz olarak ayarla
        self.master.focus_set()  # İmleci ana pencereye getir


def main():
    def main():
        """
        The main function of the program. It creates a new instance of the WordleGame class and starts the game.
        """
    root = tk.Tk()
    game = WordleGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
