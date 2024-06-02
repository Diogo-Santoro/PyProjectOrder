import sqlite3
from tkinter import messagebox, simpledialog

def read_orders():
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
        else:
            order_ids = "\n".join([f"ID: {order[0]}" for order in orders])
            messagebox.showinfo("IDs dos Pedidos", order_ids)
            
            while True:
                selected_id = simpledialog.askstring("Listar Pedidos", "Digite o ID do pedido que deseja ver os detalhes (ou 'sair' para voltar):")
                
                if selected_id.lower() == 'sair':
                    break
                
                cursor.execute('SELECT * FROM orders WHERE id = ?', (selected_id,))
                order = cursor.fetchone()
                
                if order:
                    order_details = (f"ID: {order[0]}, Cliente: {order[1]}, Contato: {order[2]}, "
                                     f"Endereço de Entrega: {order[3]}, Produto: {order[4]}, "
                                     f"Quantidade: {order[5]}, Preço: {order[6]}, Situação: {order[7]}")
                    messagebox.showinfo("Detalhes do Pedido", order_details)
                else:
                    messagebox.showerror("Erro", "Pedido não encontrado.")
    except sqlite3.Error as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao acessar o banco de dados: {e}")
    
    conn.close()
