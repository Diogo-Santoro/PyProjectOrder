import sqlite3

def read_orders():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT id FROM orders')
    orders = cursor.fetchall()
    
    if not orders:
        print("Nenhum pedido encontrado.")
    else:
        print("IDs dos Pedidos:")
        for order in orders:
            print(f"ID: {order[0]}")
        
        while True:
            selected_id = input("Digite o ID do pedido que deseja ver os detalhes (ou 'sair' para voltar): ")
            
            if selected_id.lower() == 'sair':
                break
            
            cursor.execute('SELECT * FROM orders WHERE id = ?', (selected_id,))
            order = cursor.fetchone()
            
            if order:
                print(f"ID: {order[0]}, Cliente: {order[1]}, Produto: {order[2]}, Quantidade: {order[3]}, Preço: {order[4]}")
            else:
                print("Pedido não encontrado.")
    
    conn.close()