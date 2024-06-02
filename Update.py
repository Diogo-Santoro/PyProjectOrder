import sqlite3
from tkinter import simpledialog, messagebox
from Notify import notify_users_about_update

def update_order():
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
    
    try:
        cursor.execute('SELECT id FROM orders')
        orders = cursor.fetchall()
        
        if not orders:
            messagebox.showinfo("Informação", "Nenhum pedido encontrado.")
            conn.close()
            return
        
        order_ids = "\n".join([f"ID: {order[0]}" for order in orders])
        messagebox.showinfo("IDs dos Pedidos", order_ids)
        
        order_id = simpledialog.askstring("Atualizar Pedido", "Digite o ID do pedido que deseja atualizar:")
        
        cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        order = cursor.fetchone()
        
        if order:
            new_client = simpledialog.askstring("Atualizar Pedido", "Digite o novo nome do cliente:")
            new_contact_info = simpledialog.askstring("Atualizar Pedido", "Digite as novas informações de contato do cliente:")
            new_delivery_address = simpledialog.askstring("Atualizar Pedido", "Digite o novo endereço de entrega:")
            new_product = simpledialog.askstring("Atualizar Pedido", "Digite o novo nome do produto:")
            new_quantity = simpledialog.askinteger("Atualizar Pedido", "Digite a nova quantidade:")
            new_price = simpledialog.askfloat("Atualizar Pedido", "Digite o novo preço:")
            new_status = simpledialog.askstring("Atualizar Pedido", "Digite a nova situação do pedido (E = Entregue, P = Pendente, C = Cancelado, A = Aberto):").upper()
            
            cursor.execute('''UPDATE orders
                              SET client = ?, contact_info = ?, delivery_address = ?, product = ?, quantity = ?, price = ?, status = ?
                              WHERE id = ?''', (new_client, new_contact_info, new_delivery_address, new_product, new_quantity, new_price, new_status, order_id))
            conn.commit()
            
            messagebox.showinfo("Sucesso", "Pedido atualizado com sucesso.")
            notify_users_about_update(order_id)
        else:
            messagebox.showerror("Erro", "Pedido não encontrado.")
    
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao acessar o banco de dados: {e}")
    
    conn.close()
