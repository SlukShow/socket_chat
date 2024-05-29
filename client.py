import tkinter as tk
import socket
import threading

# Функция для отправки сообщения на сервер
def send_to_socket(message='Nick: Test messages'):
    if message:
        server_socket.send(message.encode())
        entry.delete(0, tk.END)

# Функция для приема сообщений от сервера
def receive_messages():
    while True:
        try:
            message = server_socket.recv(1024).decode()
            if message:
                message_list.insert(tk.END, message)
        except ConnectionAbortedError:
            break

# Функция для отправки сообщения с никнеймом на сервер
def send_message():
    # Получить текст сообщения из entry
    message_text = entry.get()
    
    # Получить никнейм из entry
    nickname = entry_nickname.get()
    
    # Сформировать сообщение в формате "nickname: message"
    message = f"{nickname}: {message_text}"
    
    # Передать сообщение через функцию send_to_socket
    send_to_socket(message)

# Создание графического интерфейса
root = tk.Tk()
root.title("Chat 37KI")

# Создание списка сообщений
message_list = tk.Listbox(root, width=50, height=20)
message_list.pack(padx=10, pady=10)

# Создание поля для ввода текста сообщения
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=5)

# Добавление поля для ввода никнейма
entry_nickname = tk.Entry(root, width=50)
entry_nickname.pack(padx=10, pady=5)

# Создание кнопки для отправки сообщения
send_button = tk.Button(root, text="Надіслати", command=send_message)
send_button.pack(padx=10, pady=5)

# Подключение к серверу
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '151.115.78.136'
port = 9999
server_socket.connect((host, port))

# Создание потока для приема сообщений
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Запуск главного цикла обработки событий Tkinter
root.mainloop()

