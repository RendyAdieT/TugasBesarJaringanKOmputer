import socket
import os

# inisialisasi alamat IP dan port
HOST = 'localhost'
PORT = 8080

# membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# mengaitkan socket dengan alamat IP dan port tertentu
server_socket.bind((HOST, PORT))

# membuat HTTP response message
def create_http_response(file_content, content_type, status_code):
    if status_code == 200:
        response_status = b'HTTP/1.1 200 OK\r\n'
    elif status_code == 404:
        response_status = b'HTTP/1.1 404 Not Found\r\n'

    response_headers = 'Content-Type: {}\r\nContent-Length: {}\r\n\r\n'.format(content_type, len(file_content)).encode()
    response_body = file_content
    response = response_status + response_headers + response_body

    return response
