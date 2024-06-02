def send_notification(message):
    # Esta função simula o envio de notificações por e-mail ou mensagens internas
    print(f"Enviando notificação por e-mail: {message}")

def notify_users_about_update(order_id):
    message = f"O pedido com ID {order_id} foi atualizado."
    send_notification(message)

def notify_users_about_delete(order_id):
    message = f"O pedido com ID {order_id} foi excluído."
    send_notification(message)
