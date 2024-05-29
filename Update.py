import sqlite3
from Notify import notify_users_about_update

def update_order():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    order_id = input("Digite o ID do pedido que deseja atualizar: ")
    
    cursor.execute('SELECT * FROM orders WHERE id = ?', (order_id,))
    order = cursor.fetchone()
    
    if order:
        new_client = input("Digite o novo nome do cliente: ")
        new_product = input("Digite o novo nome do produto: ")
        new_quantity = int(input("Digite a nova quantidade: "))
        new_price = float(input("Digite o novo preço: "))
        
        cursor.execute('''UPDATE orders
                          SET client = ?, product = ?, quantity = ?, price = ?
                          WHERE id = ?''', (new_client, new_product, new_quantity, new_price, order_id))
        conn.commit()
        
        print("Pedido atualizado com sucesso.")
        notify_users_about_update(order_id)
    else:
        print("Pedido não encontrado.")
    
    conn.close()
