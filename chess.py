import tkinter as tk

def create_chess_board():
    # Set up the main window
    root = tk.Tk()
    root.title("Chess Board")

    # Maximize window width and set a custom height
    screen_width = root.winfo_screenwidth()

    # Define colors
    white_color = "#FECE9D"  # light gray for white squares
    black_color = "#D38C45"  # dark gray for black squares

    # Create a frame with top and bottom padding
    board_frame = tk.Frame(root, padx=30, pady=30, bg="white")  # Black background for padding effect
    board_frame.pack(pady=(30, 30), expand=True)  # Top and bottom padding only

    # Create 8x8 board
    board_size = 8
    square_size = screen_width // board_size  # Calculate square size based on screen width

    for row in range(board_size):
        for col in range(board_size):
            color = white_color if (row + col) % 2 == 0 else black_color
            square = tk.Label(board_frame, bg=color, width=square_size // 15, height=square_size // 8, borderwidth=0, relief="solid")
            square.grid(row=row, column=col, sticky="nsew")
            

                
    # Configure grid to fill available space
    for i in range(board_size):
        board_frame.grid_rowconfigure(i, weight=1)
        board_frame.grid_columnconfigure(i, weight=1)

    root.mainloop()

create_chess_board()
