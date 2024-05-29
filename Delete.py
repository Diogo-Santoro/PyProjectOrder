import sqlite3
from Notify import notify_users_about_delete

def delete_order():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    order_id = input("Digite o ID do pedido que deseja excluir: ")
    
    cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
    order = cursor.fetchone()
    
    if order:
        cursor.execute('DELETE FROM orders WHERE id = ?', (order_id,))
        conn.commit()
        
        print("Pedido excluído com sucesso.")
        notify_users_about_delete(order_id)
    else:
        print("Pedido não encontrado.")
    
    conn.close()
