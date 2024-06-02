import sqlite3
from tkinter import simpledialog, messagebox

def create_order():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        client TEXT,
                        contact_info TEXT,
                        delivery_address TEXT,
                        product TEXT,
                        quantity INTEGER,
                        price REAL,
                        status TEXT
                    )''')
    
    client = simpledialog.askstring("Criar Pedido", "Digite o nome do cliente:")
    contact_info = simpledialog.askstring("Criar Pedido", "Digite as informações de contato do cliente:")
    delivery_address = simpledialog.askstring("Criar Pedido", "Digite o endereço de entrega:")
    product = simpledialog.askstring("Criar Pedido", "Digite o nome do produto:")
    quantity = simpledialog.askinteger("Criar Pedido", "Digite a quantidade:")
    price = simpledialog.askfloat("Criar Pedido", "Digite o preço:")
    status = simpledialog.askstring("Criar Pedido", "Digite a situação do pedido (E = Entregue, P = Pendente, C = Cancelado, A = Aberto):").upper()
    
    cursor.execute('''INSERT INTO orders (client, contact_info, delivery_address, product, quantity, price, status)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (client, contact_info, delivery_address, product, quantity, price, status))
    conn.commit()
    
    messagebox.showinfo("Sucesso", "Pedido criado com sucesso.")
    conn.close()
