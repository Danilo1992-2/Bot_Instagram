from mysql.connector import connect
from json import load

class conexao:
    def __init__(self):
            jsonLido = load(open('./dependencias.json','r'))
            self.conexao = connect(
                user = jsonLido['login'],
                password = jsonLido['senha'],
                host= jsonLido['host'],
                database = jsonLido['banco']
                )
            self.cursor = self.conexao.cursor()
    
    def executar(self,query):
        self.query = query
        self.cursor.execute(self.query)
        self.resultado = self.cursor.fetchall()
        self.conexao.close()
        return self.resultado
