from decimal import Decimal

class Funcionario:
    def __init__(self, nome, idade, cargo, salario, empresa):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        self.empresa = empresa

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setCargo(self, cargo):
        self.cargo = cargo

    def setSalario(self, salario):
        self.salario = salario

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCargo(self):
        return self.cargo

    def getSalario(self):
        return format(self.salario, '.2f')

    def getEmpresa(self):
        return self.empresa

    def apresentacao(self):
        return f'Olá! Eu sou o {self.getNome()} da {self.getEmpresa()}, tenho {self.getIdade()} anos, sou o novo {self.getCargo()} e recebo {self.getSalario()} reais por mês.'

    def decimoTerceiro(self):
        return (self.salario * 2)

    def bonus(self, avaliacao):
        if avaliacao == 0:
            return format(0, '.2f')
        elif 1 <= avaliacao < 2:
            return format(self.salario, '.2f')
        elif 2 <= avaliacao < 3:
            return format(self.salario * 2, '.2f')
        elif 3 <= avaliacao < 4:
            return format(self.salario * 3, '.2f')
        elif 4 <= avaliacao < 5:
            return format(self.salario * 4, '.2f')
        elif avaliacao == 5:
            return format(self.salario * 5, '.2f')
        else:
            return 'Pontuação inválida.'