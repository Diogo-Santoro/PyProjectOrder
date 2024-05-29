import sqlite3

def send_notification(message):

    print(f"Enviando notificação: {message}")

def notify_users_about_update(order_id):
    message = f"O pedido com ID {order_id} foi atualizado."
    send_notification(message)

def notify_users_about_delete(order_id):
    message = f"O pedido com ID {order_id} foi excluído."
    send_notification(message)