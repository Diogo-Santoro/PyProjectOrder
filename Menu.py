import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from Create import create_order
from Read import read_orders
from Update import update_order
from Delete import delete_order

class OrderManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento de Pedidos")

        self.main_menu = tk.Frame(root)
        self.main_menu.pack()

        self.login_menu()

    def login_menu(self):
        self.clear_frame()

        tk.Label(self.main_menu, text="Sistema de Gerenciamento de Pedidos", font=('Helvetica', 16, 'bold')).pack(pady=20)
        tk.Button(self.main_menu, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.main_menu, text="Registrar", command=self.register).pack(pady=10)
        tk.Button(self.main_menu, text="Sair", command=self.root.quit).pack(pady=10)

    def clear_frame(self):
        for widget in self.main_menu.winfo_children():
            widget.destroy()

    def login(self):
        username = simpledialog.askstring("Login", "Username:")
        password = simpledialog.askstring("Login", "Password:", show='*')

        role = self.authenticate(username, password)
        if role:
            self.user_menu(role)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def authenticate(self, username, password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY,
                            password TEXT,
                            role TEXT
                        )''')

        cursor.execute("SELECT * FROM users WHERE username='admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'admin', 'admin')")

        conn.commit()

        cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            return user[0]
        else:
            return None

    def register(self):
        username = simpledialog.askstring("Registrar", "Escolha um nome de usuário:")
        password = simpledialog.askstring("Registrar", "Escolha uma senha:", show='*')
        role = simpledialog.askstring("Registrar", "Escolha o cargo (admin/user/cliente):").lower()

        if role not in ('admin', 'user', 'cliente'):
            messagebox.showerror("Erro", "Cargo inválido. Tente novamente.")
            return

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            username TEXT PRIMARY KEY,
                            password TEXT,
                            role TEXT
                        )''')

        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Nome de usuário já existe. Tente novamente.")

        conn.close()

    def user_menu(self, role):
        self.clear_frame()

        tk.Label(self.main_menu, text="Menu de Opções", font=('Helvetica', 16, 'bold')).pack(pady=20)
        if role == 'admin' or role == 'user':
            tk.Button(self.main_menu, text="Criar Pedido", command=create_order).pack(pady=10)
            tk.Button(self.main_menu, text="Listar Pedidos", command=read_orders).pack(pady=10)
            tk.Button(self.main_menu, text="Atualizar Pedido", command=update_order).pack(pady=10)
            tk.Button(self.main_menu, text="Deletar Pedido", command=delete_order).pack(pady=10)
        elif role == 'cliente':
            tk.Button(self.main_menu, text="Listar Pedidos", command=read_orders).pack(pady=10)

        tk.Button(self.main_menu, text="Sair", command=self.login_menu).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManagementApp(root)
    root.mainloop()
