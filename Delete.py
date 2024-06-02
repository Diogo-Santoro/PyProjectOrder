import sqlite3
from tkinter import simpledialog, messagebox
from Notify import notify_users_about_delete

def delete_order():
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
        
        order_id = simpledialog.askstring("Deletar Pedido", "Digite o ID do pedido que deseja excluir:")
        
        cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
        order = cursor.fetchone()
        
        if order:
            cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
            conn.commit()
            
            messagebox.showinfo("Sucesso", "Pedido excluído com sucesso.")
            notify_users_about_delete(order_id)
        else:
            messagebox.showerror("Erro", "Pedido não encontrado.")
    
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao acessar o banco de dados: {e}")
    
    conn.close()
