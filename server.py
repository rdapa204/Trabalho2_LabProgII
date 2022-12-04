import socket 
#Iniciliaza as variáveis 
HOST = '127.0.0.1'
PORT = 50000
addr = (HOST,PORT)
java_wins = 0
py_wins = 0
opcoes = ['pedra','spock','papel','lagarto','tesoura']
jogadas = [["tesoura","papel"],["papel","pedra"],
           ["pedra","lagarto"],["lagarto","spock"],
           ["spock","tesoura"],["tesoura","lagarto"],
           ["lagarto","papel"],["papel","spock"],
           ["spock","pedra"],["pedra","tesoura"]]

n_rodada = 0
#Inicializa o socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(5)

print("Aguardando conexão")
#Aceita as conexões
connPy,enderPy = sock.accept()
print("Conectado com", enderPy)
connJava,enderJava = sock.accept()
print("Conectado com",enderJava)


while True:
    #Fim da partida, computa resultado final
    #E inicia processo de fechar conexão
    if(n_rodada==15):
        print("\nPartida encerrada\n")
        if(java_wins>py_wins):
            print("O cliente Java ganhou com ",java_wins," vitórias e ",py_wins," derrotas.")
        if(java_wins<py_wins):
            print("O cliente Python ganhou com ",py_wins," vitórias e ",java_wins," derrotas.")
        if(java_wins==py_wins):
            print("Houve um Empate!")
        connPy.send(str.encode("FIN"))
        msgFIN = "FIN\n"
        connJava.send(bytes(str(msgFIN),'utf8'))
        FIN_Py = connPy.recv(1024).decode()
        FIN_Java = connJava.recv(1024).decode()
        if FIN_Java == FIN_Py:
            connPy.close()
            connJava.close()
        break

    #Recebe a jogada de cada jogador
    jogadaPy = str(connPy.recv(1024).decode())
    jogadaJava = str(connJava.recv(1024).decode())

    #Verifica se houve empate
    if jogadaJava == jogadaPy:
        print(n_rodada+1, ": Empate")
        resultadoJava="Empate\n"
        resultadoPy="Empate"
        connPy.send(resultadoPy.encode())
        connJava.send(bytes(str(resultadoJava),'utf8'))
        
    #Verifica se Java ganhou    
    if [jogadaJava,jogadaPy] in jogadas and jogadaPy != jogadaJava:
        print(n_rodada+1,": Java ganhou")
        java_wins = java_wins + 1
        resultadoJava = "Ganhou\n"
        resultadoPy = "Perdeu"
        connPy.send(resultadoPy.encode())
        connJava.send(bytes(str(resultadoJava),'utf8'))

    #Verifica de Python ganhou    
    if [jogadaJava,jogadaPy] not in jogadas and jogadaPy!=jogadaJava:
        print(n_rodada+1," : Python ganhou")
        py_wins = py_wins+1
        resultadoPy = "Ganhou"
        resultadoJava = "Perdeu\n"
        connPy.send(resultadoPy.encode())
        connJava.send(bytes(str(resultadoJava),'utf8'))
    
    n_rodada = n_rodada+1
