class Aluno:
  def __init__(self, nome, nota1, nota2, nota3):
      self.nome = nome
      self.nota1 = nota1
      self.nota2 = nota2
      self.nota3 = nota3

  def media(self):
      media = (self.nota1 + self.nota2 + self.nota3) / 3
      print(f'A média do aluno {self.nome} é {media:.2f}')
      if media < 7:
          print(f'Aluno reprovado')

i = 0

while i < 3:
  nome = input('Insira o nome do aluno: ')
  nota1 = float(input('Insira a nota 1 do aluno: '))
  nota2 = float(input('Insira a nota 2 do aluno: '))
  nota3 = float(input('Insira a nota 3 do aluno: '))
  aluno = Aluno(nome, nota1, nota2, nota3)
  aluno.media()
  i = i + 1