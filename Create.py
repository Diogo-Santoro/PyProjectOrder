import sqlite3

def create_order():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        cliente TEXT,
                        produto TEXT,
                        quantidade INTEGER,
                        preco REAL
                    )''')
    
    cliente = input("Nome do Cliente: ")
    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    
    cursor.execute('INSERT INTO orders (cliente, produto, quantidade, preco) VALUES (?, ?, ?, ?)',
                   (cliente, produto, quantidade, preco))
    
    conn.commit()
    conn.close()
    
    print("Pedido criado com sucesso!")
