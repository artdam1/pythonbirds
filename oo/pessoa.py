class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade           # exemplos de boas praticas
        self.nome = nome             # ok
        self.filhos = list(filhos)   # ok

    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    luciano = Pessoa(renzo, nome='luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome = 'ramalho'  # usualmente não é uma boa pratica
    del luciano.filhos
    print(luciano.__dict__)  # o __dict__ mostra os atributos de instancias presente nos atributos dinamicos
    print(renzo.__dict__)







