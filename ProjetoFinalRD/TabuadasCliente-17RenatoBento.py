import socket
HOST = "127.0.0.1" #LoopBack
PORT = 4321 #Port

def menu ():
    print("===================")
    print("CLIENTE DE TABUADAS")  
    print("===================")  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Criar O Socket")
    s.connect((HOST,PORT))
    print("A pedir ligação")
    while True:
        menu = menu()
        NumTab = input("Qual Tabuada que pretende [1-100]? ")
        NumAte = input("Até qunado quer a Tabuada [2-100]? ")
        if NumTab.isdigit() and int(NumTab) > 1 and int(NumTab) < 100:
            print(f"Como colucou a Tabuada invalída {NumTab}, vai terminar!")
            break
        if NumAte.isdigit() and int(NumAte) > 2 and int(NumAte) < 100:
            print("Como o limite e escolhido '1' é inválido, será até 10!")
        else:
            s.sendall(NumTab.encode())
            print(f"A pedir a Tabuada do {NumTab} até {NumAte} ...")
            data = s.recv(1024).decode()
            print(data)
            s.close()