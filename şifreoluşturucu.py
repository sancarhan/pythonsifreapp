import tkinter as tk
import random
import string

def generate_password():
    password_length = 16
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)

# Tkinter penceresini oluştur
root = tk.Tk()
root.title("Şifre Oluşturucu")

# Şifre oluşturma butonu
generate_button = tk.Button(root, text="Yeni Şifre Oluştur", command=generate_password)
generate_button.pack(pady=20)

# Şifre gösterme etiketi
password_label = tk.Label(root, text="", font=("Helvetica", 16))
password_label.pack()

# Uygulamayı çalıştır
root.mainloop()
