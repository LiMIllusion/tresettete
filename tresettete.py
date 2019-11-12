import os
import platform
import socket


def clearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def setUserName():
    clearScreen()
    file = open("username.txt", "w")
    nome = input("Inserisci il tuo nickname: ")
    while len(nome)<1:
        nome = input("Nome troppo corto. Riprova: ")
    file.write(nome)
    file.close()
    clearScreen()


def hostGame():
    giocatori = {}
    print("Avvio il server...")
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((socket.gethostbyname(socket.gethostname()), 49565))
    print("Server avviato con l'identificativo: "+socket.gethostname())
    serv.listen(4)
    while 1:

        conn, addr = serv.accept()
        print("Giocatore connesso")
        print(addr)
        print(conn)
        stringa = ''
        while 1:
            data = conn.recv(4096)
            if not data:
                break
            stringa = data.decode("utf-8")

            print(stringa)
            conn.sendall(b"Sono il server\n")
        conn.close()
        print("Un giocatore ha abbandonato")


def joinGame():
    clearScreen()
    file = open("username.txt", 'r')
    username = file.readline()
    file.close()
    hostname = input("Inserisci il nome del server: ")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostbyname(hostname), 49565))
    client.sendall(username.encode('utf-8'))
    from_server = client.recv(4096).decode("utf-8")
    client.close()
    print(from_server)


def main():
    clearScreen()
    print("\t---Benvenuto in tresettete---")
    while 1:
        print("1) Ospita una partita")
        print("2) Entra in una partita")
        print("9) Nome utente")
        print("0) Esci")
        choice = eval(input("Scegli l'opzione: "))
        while choice!= 1 and choice!=2 and choice!=9 and choice!=0:
            choice = eval(input("Valore non valido. Riprova:"))
        if choice == 0:
            print("Ciao! E' stato un piacere!")
            exit(0)
        elif choice == 9:
            setUserName()
        elif choice == 1:
            if os.path.isfile("username.txt"):
                hostGame()
            else:
                clearScreen()
                print("Inserisci un nome utente (premendo 9) prima di cominciare.")
        elif choice == 2:
            if os.path.isfile("username.txt"):
                joinGame()
            else:
                clearScreen()
                print("Inserisci un nome utente (premendo 9) prima di cominciare.")



if __name__ == '__main__':
    main()