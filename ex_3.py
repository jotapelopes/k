class Pessoa:
  def __init__(self, nome, peso, altura):
      self.nome = nome
      self.peso = peso
      self.altura = altura

  def imc(self):
      imc = self.peso / self.altura ** 2
      print(f"O IMC da pessoa {self.nome} é {imc:.2f}")

i = 1

while i < 4:
  nome = input(f"Informe o nome {i}: ")
  peso = float(input(f"Informe o peso do/da {nome}: "))
  altura = float(input(f"Informe a altura do/da {nome}: "))
  pessoa = Pessoa(nome, peso, altura)
  pessoa.imc()
  i = i + 1