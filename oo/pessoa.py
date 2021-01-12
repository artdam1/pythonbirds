class Pessoa:
    olhos = 2   #atributo de classe, esse atributo é algo comum a todos, por isso faz mais sentido ser
                # criado fora do __init__, já idade, nome e filhos tbm é comum porém ainda varia de acordo com cada
                #pessoa, diferente dos olhos que em situações muito especificas podem varias.

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade           # exemplos de boas praticas
        self.nome = nome             # ok
        self.filhos = list(filhos)   # ok

    def cumprimentar(self):
        return f'olá {id(self)}'

    @staticmethod
    def metodo_estatico():    # independe do objeto.
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):   # é utilizado quando se quer acessar dados da propria classe.
        return f'{cls} - olhos {cls.olhos}'


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
    luciano.sobrenome = 'ramalho'    # usualmente não é uma boa pratica, é um atributo de instância pois so pertence ao
                                     # objeto luciano.
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)          # o __dict__ mostra os atributos de instância presente nos atributos dinamicos
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())






