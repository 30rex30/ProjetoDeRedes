import socket
import datetime
import os


HOST = "127.0.0.1" # LoopBack !!!
PORT = 4321 # uma porta entre 1024 e 65535, neste caso será 42069 !!!

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Criar O Socket")
    s.bind((HOST, PORT)) # defini o endereço e porta !!!
    print(f"A defenir  o endereceço {HOST} e a porta {PORT}")
    while True:
        s.listen() # ficar a espera de ligações 
        print("A espera de ligações...")
        ligacao, endereco = s.accept() # guarda ligação/endereco cliente
        print(f"Ligação recebida! Connectado a {endereco}")
        with ligacao
            NumTab = ligacao.recv(1024).decode()

