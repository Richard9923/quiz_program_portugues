## criar uma class chamada QuizBrain, para eu fazendo toda a lógica do quiz.


class QuizBrain:

    #receber o banco de questoes do file main
    def __init__(self, question_list):
        self.q_number = 0
        self.score = 0
        self.q_list = question_list


    # parametro para verificar se ainda tem questoes

    def ainda_tem_questoes(self):
        if self.q_number < len(self.q_list):
            return True
        else:
            return False

    #criar parametro na classe para receber a questao e converter em string

    def proxima_questao(self):
        pergunta = self.q_list[self.q_number]
        self.q_number += 1
        resposta_usuario = input(f"Q{self.q_number}: {pergunta.q_pergunta} True/False? ")
        self.check_answer(resposta_usuario, pergunta.q_resposta)


    ##criando parametro para verificar se a resposta esta correta
    def check_answer(self,reposta_usuario, resposta_correta):
        if reposta_usuario.lower() == resposta_correta.lower():
            print("Você acertou a resposta!")
            self.score += 1
        else:
            print("Você errou a resposta.")

        print(f"A resposta correta é essa: {resposta_correta}. ")
        print(f"Sua pontuação atual: {self.score}/ {self.q_number}.")
