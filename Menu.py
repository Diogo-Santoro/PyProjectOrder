import sqlite3
from Create import create_order
from Read import read_orders
from Update import update_order
from Delete import delete_order

def authenticate():
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

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return user[0]
    else:
        print("Usuário ou senha incorretos.")
        return None

def register():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        role TEXT
                    )''')

    username = input("Escolha um nome de usuário: ")
    password = input("Escolha uma senha: ")
    role = input("Escolha o cargo (admin/user/cliente): ").lower()

    if role not in ('admin', 'user', 'cliente'):
        print("Cargo inválido. Tente novamente.")
        return

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        print("Usuário registrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Nome de usuário já existe. Tente novamente.")

    conn.close()

def menu():
    while True:
        print("\nSistema de Gerenciamento de Pedidos")
        print("1. Login")
        print("2. Registrar")
        print("3. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            role = authenticate()
            if role:
                user_menu(role)
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

def user_menu(role):
    while True:
        print("\nMenu de Opções")
        print("1. Criar Pedido" if role == 'admin' or role == 'user' else "1. Listar Pedidos")
        if role == 'admin' or role == 'user':
            print("2. Listar Pedidos")
            print("3. Atualizar Pedido")
            print("4. Deletar Pedido")
        elif role == 'user' or role == 'cliente':
            print("2. Sair")

        choice = input("Escolha uma opção: ")

        if role == 'admin' or role == 'user':
            if choice == '1':
                create_order()
            elif choice == '2':
                read_orders()
            elif choice == '3':
                update_order()
            elif choice == '4':
                delete_order()
            elif choice == '5':
                break
            else:
                print("Opção inválida. Tente novamente.")
        elif role == 'user' or role == 'cliente':
            if choice == '1':
                read_orders()
            elif choice == '2':
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
