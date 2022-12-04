import socket
import random
from scipy import stats

def EscolherJogada():
    if len(record) == 15:
        return "FIN"
    if record == [] or len(record) < 5:
        return random.choice(jogadas)
    else:
        win = []
        lose = []
        for x in record:
            if x[1].upper() == "GANHOU" or x[1].upper()=="EMPATE":
                win.append(x[0])
            else:
                lose.append(x[0])
            mensagemWin = stats.mode(win)
            mensagemLose = stats.mode(lose)
        set_win = set(win)
        set_lost = set(lose)
        temp = set_win - set_lost
        all = win + list(temp)
        if(set(all)==set(jogadas)):
            chooser = random.randint(0,1)
            if(chooser):
                return random.choice(list(mensagemWin[0]))
            else:
                return random.choice(list(mensagemLose[0]))
        else:
            return random.choice(list(set(jogadas)-set(all)))
            

HOST = 'localhost'
PORT = 50000
addr = (HOST,PORT)

record = []

jogadas = ['pedra','spock','papel','lagarto','tesoura']

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(addr)
wins = 0
losts = 0
while True:
    mensagem = EscolherJogada()
    sock.sendall(str.encode(mensagem))
    resposta = sock.recv(1024).decode()
    if(resposta=="Ganhou"):
        wins=wins+1
    if(resposta=="Perdeu"):
        losts=losts+1
    #Fim da partida, computa o resultado final    
    if(resposta=="FIN"):
        sock.sendall(str.encode("FIN"))
        sock.close()
        if(wins>losts):
            print("Você ganhou!!!")
        if(wins<losts):
            print("Você perdeu!!!")
        if(wins==losts):
            print("Foi empate!!!")
        break

    
    else:
        print("Jogada Escolhida: ",mensagem,"\tResultado: ", resposta,"\n")
        #Imprime histórico a cada rodado
        current = [mensagem,resposta]
        record.append(current)
        print("Historico:")
        print(*record, sep='\n')
        print('\n')
