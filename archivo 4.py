
import socket

target_host = "127.0.0.1"
target_port = 80

# Crear un objeto socket 
# AF_INET indica IPv4, SOCK_DGRAM indica que es UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ENVIAR DATOS:
# En Python 3, enviamos bytes. El prefijo b convierte el string a bytes.
client.sendto(b"AAABBBCCC", (target_host, target_port))

try:
    # Recibir datos y la dirección del remitente
    # Establecemos un timeout para que no se quede bloqueado si no hay respuesta
    client.settimeout(2)
    data, addr = client.recvfrom(4096)

    # IMPRIMIR:
    # Decodificamos los bytes a string para una lectura limpia
    print(data.decode('utf-8'))
    print(f"Recibido desde: {addr[0]}:{addr[1]}")

except socket.timeout:
    print("No se recibió respuesta (Timeout).")

finally:
    client.close()