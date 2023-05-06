class Socio:
  def __init__(self, socio, porcent):
      self.socio = socio
      self.porcent = porcent

  def valor_socio(self, valor_empresa) -> None:
      valor_socio = valor_empresa * (self.porcent / 100) 
      print(f"O sócio {self.socio}, que tem a seguinte porcentagem da empresa: {self.porcent}, tem o seguinte valor: {valor_socio}")

i = 0

valor_empresa = float(input('Insira o valor da empresa: '))

while i < 3:
  socio = input('Insira o nome do sócio: ')
  porcent = float(input('Insira a porcentagem do sócio: '))
  socio = Socio(socio, porcent)
  socio.valor_socio(valor_empresa)
  i += 1