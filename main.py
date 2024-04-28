## Mesmo projeto de quiz anterior, mas nesse esterei fazendo uma adaptação para português.
## Objetivos.
## 1. Adaptação do programa para a lingua portuguêsa.
## 2. Praticar escrita dos códigos.
## Programa originalmente construido no Pycharm64

## importando os dados dos outros files

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


## Criar lista para receber a data.

banco_de_questoes = []

## Criar For lop, para separa cada questão (text) e resposta (answer) e colocar na lista acima

for questao in question_data:

    q_pergunta = questao["text"]
    q_resposta = questao["answer"]
    banco_de_questoes.append(Question(q_pergunta, q_resposta))


quiz = QuizBrain(banco_de_questoes)


while quiz.ainda_tem_questoes():
    quiz.proxima_questao()