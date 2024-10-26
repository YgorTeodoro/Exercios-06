class Vendedor : 
    def __init__(self, nome,sobrenome,idade,cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

    def informacaoSaida(self):
        print(f"Olá, meu nome é ",self.nome,self.sobrenome,"\nidade:", self.idade,"\nEu moro em",  self.cidade )


vendedor1 =  Vendedor(input('Nome: '), input('Sobrenome:  '), input('idade: '), input('cidade: '))
vendedor2 =  Vendedor(input('Nome: '), input('Sobrenome:  '), input('idade: '), input('cidade: '))
vendedor3 =  Vendedor(input('Nome: '), input('Sobrenome:  '), input('idade: '), input('cidade: '))

vendedor1.informacaoSaida()
vendedor2.informacaoSaida()
vendedor3.informacaoSaida()
