import tkinter as tk
from tkinter import messagebox

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Tik-Tak-Toe")

# Oyun tahtası ve değişkenler
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Butonları tutacak liste
buttons = []

# Butonları oluştur ve yerleştir
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Buton tıklama olayı
def on_button_click(index):
    global current_player, game_over

    if board[index] == " " and not game_over:
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner(current_player):
            messagebox.showinfo("Oyun Bitti", f"{current_player} kazandı!")
            game_over = True
        elif " " not in board:
            messagebox.showinfo("Oyun Bitti", "Berabere!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

# Kazananı kontrol et
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Yatay
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Dikey
        [0, 4, 8], [2, 4, 6]              # Çapraz
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Ana döngüyü başlat
root.mainloop()