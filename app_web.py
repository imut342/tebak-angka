
import random
import tkinter as tk

# Variabel Global
target_number = 0
attempts = 0
max_attempts = 10


def reset_game():
    """Fungsi untuk memulai ulang permainan (reset data & UI)."""
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0

    # Reset tampilan UI
    lbl_attempts.config(text=f"Sisa Percobaan: {max_attempts}")
    lbl_result.config(text="", fg="#EEEEEE")
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    btn_guess.config(state=tk.NORMAL)
    btn_restart.pack_forget()  # Sembunyikan tombol 'Main Lagi' saat game dimulai


def check_guess():
    """Fungsi untuk mengecek tebakan pemain."""
    global attempts, target_number

    user_input = entry.get()

    # Validasi input angka
    try:
        guess = int(user_input)
    except ValueError:
        lbl_result.config(
            text="Masukkan angka bulat yang valid!", fg="#F05454"
        )
        return

    attempts += 1
    remaining = max_attempts - attempts

    # Logika Tebakan
    if guess < target_number:
        lbl_result.config(text="Terlalu Rendah! (Too low)", fg="#FFD369")
    elif guess > target_number:
        lbl_result.config(text="Terlalu Tinggi! (Too high)", fg="#FFD369")
    else:
        # Jika Berhasil Menebak
        lbl_result.config(
            text=f"Selamat! Kamu berhasil dalam {attempts} percobaan! 🎉",
            fg="#4E9F3D",
        )
        end_game()
        return

    # Jika Kesempatan Habis
    if remaining > 0:
        lbl_attempts.config(text=f"Sisa Percobaan: {remaining}")
    else:
        lbl_result.config(
            text=f"Game Over! Angkanya adalah {target_number}.", fg="#F05454"
        )
        lbl_attempts.config(text="Sisa Percobaan: 0")
        end_game()

    entry.delete(0, tk.END)


def end_game():
    """Fungsi untuk menghentikan permainan dan menampilkan tombol 'Main Lagi'."""
    btn_guess.config(state=tk.DISABLED)
    entry.config(state=tk.DISABLED)
    # Munculkan tombol 'Main Lagi' di layar
    btn_restart.pack(pady=5)


# 1. Buat Jendela Utama (GUI)
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x360")
root.configure(bg="#222831")

# 2. Komponen Tampilan (Widgets)
lbl_title = tk.Label(
    root,
    text="Tebak Angka (1 - 100)",
    font=("Helvetica", 14, "bold"),
    bg="#222831",
    fg="#EEEEEE",
)
lbl_title.pack(pady=15)

lbl_attempts = tk.Label(
    root,
    text="",
    font=("Helvetica", 10),
    bg="#222831",
    fg="#EEEEEE",
)
lbl_attempts.pack()

# Kolom Input
entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    justify="center",
    bd=5,
    relief=tk.FLAT,
    bg="#393E46",
    fg="#EEEEEE",
)
entry.pack(pady=15, ipadx=5, ipady=5)

# Tombol Tebak
btn_guess = tk.Button(
    root,
    text="Tebak!",
    font=("Helvetica", 11, "bold"),
    bg="#00ADB5",
    fg="#EEEEEE",
    bd=0,
    padx=15,
    pady=5,
    command=check_guess,
)
btn_guess.pack(pady=5)

# Tombol Main Lagi (Awalnya tersembunyi)
btn_restart = tk.Button(
    root,
    text="🔄 Main Lagi",
    font=("Helvetica", 10, "bold"),
    bg="#FFD369",
    fg="#222831",
    bd=0,
    padx=10,
    pady=5,
    command=reset_game,
)

# Label Hasil / Petunjuk
lbl_result = tk.Label(
    root,
    text="",
    font=("Helvetica", 10, "bold"),
    bg="#222831",
    fg="#EEEEEE",
    wraplength=300,
)
lbl_result.pack(pady=10)

# Memulai game pertama kali
reset_game()

# 3. Jalankan Layar GUI
root.mainloop()
