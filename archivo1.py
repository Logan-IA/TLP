import socket

target_host = "www.google.com"
target_port = 80

# Crear un objeto socket
# El bloque 'with' asegura que el socket se cierre automáticamente al terminar
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    
    # Conectar el cliente
    client.connect((target_host, target_port))

    # ENVIAR DATOS:
    # En Python 3, debes enviar bytes, no strings. 
    # El prefijo b"..." convierte el texto en bytes.
    request = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
    client.send(request)

    # RECIBIR DATOS:
    response = client.recv(4096)

    # IMPRIMIR:
    # Usamos paréntesis (obligatorio en Python 3) y decodificamos 
    # los bytes a texto para que se vea correctamente.
    print(response.decode('utf-8', errors='ignore'))
