# Trabalho2_LabProgII

A aplicação padroniza que a comunicação se dê atráves de um servidor Python que computa simultaneamente os dados de dois clientes, um cliente Java e um cliente Python.
Para organizar tal comunicação é esperado que a comunicação comece por o Cliente Python e logo após o Cliente Java. A Heurística utilizada no cliente Python é voltada para priorizar aquelas jogadas que ainda não foram feitas, e dado que todas tenham sido executadas pelo menos uma vez então a Heurística passa a escolher aquele que teve mais sucessos de vitórias no passado. A Heurística do Cliente Java utiliza uma análise randômica para escolher cada jogada.


**Cliente Python** 

![image](https://user-images.githubusercontent.com/89489900/205523263-bcfc989c-2760-414b-874f-b939f758106f.png)

**Servidor Python**

![image](https://user-images.githubusercontent.com/89489900/205523281-057c0f27-5fc9-4d29-aae4-c23401ef2ee8.png)

**Cliente Java**

![image](https://user-images.githubusercontent.com/89489900/205523296-8dbbfebf-b970-4b5d-baca-7b49db88dfe6.png)
