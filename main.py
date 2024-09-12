import tkinter as tk
from tkinter import messagebox

def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    
    if not name or not age or not address:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    # Hiển thị thông tin đã nhập
    messagebox.showinfo("Thông tin người dùng", f"Thông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùngThông tin người dùng")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhập Thông Tin Người Dùng")

# Tạo nhãn và ô nhập cho Tên
tk.Label(root, text="Tên:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Tạo nhãn và ô nhập cho Tuổi
tk.Label(root, text="Tuổi:").grid(row=1, column=0, padx=10, pady=10)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=10)

# Tạo nhãn và ô nhập cho Địa chỉ
tk.Label(root, text="Địa chỉ:").grid(row=2, column=0, padx=10, pady=10)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1, padx=10, pady=10)

# Nút gửi
submit_button = tk.Button(root, text="Gửi", command=submit_data)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

# Chạy vòng lặp chính
root.mainloop()
