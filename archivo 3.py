import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

# Corrección: se escribe 'socket', no 'socekt'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Reutilizar el puerto (evita el error 'Address already in use' si reinicias rápido)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((bind_ip, bind_port))

# Escuchar con un máximo de 5 conexiones en cola
server.listen(5)

print(f"[*] Listening on {bind_ip}:{bind_port}")

# Este es nuestro hilo para manejar clientes
def handle_client(client_socket):
    with client_socket as sock:
        # Recibir datos (vienen como bytes en Python 3)
        request = sock.recv(1024)
        
        print(f"[*] Received: {request.decode('utf-8', errors='ignore')}")

        # Enviar de vuelta un paquete (debe ser bytes, por eso usamos b"")
        sock.send(b"ACK!")

while True:
    # Aceptar conexión
    client, addr = server.accept()

    print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

    # Crear el hilo para manejar los datos entrantes
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
