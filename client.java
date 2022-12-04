package org.example;
import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
//Classe utilizada para armazenar o histórico das rodadas
class Historico{
    public List<String> jogada;
    public List<String> resultado;

    public Historico(){
        jogada = new ArrayList<>();
        resultado = new ArrayList<>();
    }
    public void print(){
        for(int i=0;i<this.resultado.size();i++){
        System.out.print("["+this.jogada.get(i)+","+this.resultado.get(i)+"]"+"\n");}
    }
}

public class client {
    public static String[] jogadas = {"pedra","spock","papel","lagarto","tesoura"};
    public static void main(String[] args) {
        try {
            int wins=0,losts=0;
            Historico historico = new Historico();
            //Inicializa o socket
            Socket socket = new Socket("127.0.0.1",50000);
            InputStreamReader inputReader = new InputStreamReader(socket.getInputStream());
            PrintStream pIn = new PrintStream(socket.getOutputStream());


            int n_rodada =0;
            while (true) {
                if (n_rodada<15) {
                    Random random = new Random();
                    int index = random.nextInt(5);
                    //Envia jogada
                    pIn.print(jogadas[index]);
                    pIn.flush();
                    historico.jogada.add(jogadas[index]);
                    System.out.println(jogadas[index]);
                    System.out.println("Esperando resposta do servidor");
                    //Recebe resultado da rodada
                    BufferedReader dOut = new BufferedReader(inputReader);
                    String x;
                    x = dOut.readLine();
                    historico.resultado.add(x);
                    System.out.println(x);

                    //Armazena o resultado da rodada
                    if(x.contains("Perdeu"))
                        losts++;
                    if(x.contains("Ganhou"))
                        wins++;

                    n_rodada++;
                    //Imprime o histórico das últimas rodadas
                    System.out.println("\n\nO historico das partidas é:");
                    historico.print();
                }
                if(n_rodada==15){
                    BufferedReader dOut = new BufferedReader(inputReader);
                    String x;
                    x = dOut.readLine();
                    if (x.contains("FIN")) {
                        pIn.print("FIN");
                        socket.close();
                        break;
                    }
                }




            }
            System.out.println("\n\nFim da partida\n");
            if(wins>losts)
                System.out.println("Você venceu!!!");
            if (losts>wins)
                System.out.println("Você perdeu!!!");
            if (losts==wins)
                System.out.println("Foi empate!!!");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }


}
