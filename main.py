# 1. Escreva um algoritmo recursivo para cada uma das alternativas (1,75).
a) ShapeS(1) = 10 
S(n) = S(n – 1) + 10,  para n ³ 2 
def ShapeS(n):
  if n == 1:
      return 10
  else:
      return ShapeS(n - 1) + 10


b) ShapeA(1) = 2 
A(n) = A(n – 1)-1 ,  para n ³ 2 
def ShapeA(n):
  if n == 1:
      return 2
  else:
      return ShapeA(n - 1) - 1


c) ShapeB(1) = 1 
B(n) = B(n – 1) + n2,  para n ³ 2 
def ShapeB(n):
  if n == 1:
      return 1
  else:
      return ShapeB(n - 1) + n**2


d) ShapeP(1) = 1 
P(n) = n2*P(n – 1) + n - 1,  para n ³ 2 
def ShapeP(n):
  if n == 1:
      return 1
  else:
      return n**2 * ShapeP(n - 1) + n - 1


e) ShapeD(1) = 3 
D(2) = 5 
D(n) = (n – 1)*D(n – 1) + (n – 2)*D(n – 2), para n > 2 
def ShapeD(n):
  if n == 1:
      return 3
  elif n == 2:
      return 5
  else:
      return (n - 1) * ShapeD(n - 1) + (n - 2) * ShapeD(n - 2)


f) ShapeW(1) = 2 
W(2) = 5 
W(n) = W(n – 1)*W(n – 2), para n > 2 
def ShapeW(n):
  if n == 1:
      return 2
  elif n == 2:
      return 5
  else:
      return ShapeW(n - 1) * ShapeW(n - 2)


g) ShapeT(1) = 1 
T(2) = 2 
T(3) = 3 
T(n) = T(n – 1) + 2*T(n – 2) + 3*T(n – 3),   para n > 3 
def ShapeT(n):
  if n == 1:
      return 1
  elif n == 2:
      return 2
  elif n == 3:
      return 3
  else:
      return ShapeT(n - 1) + 2 * ShapeT(n - 2) + 3 * ShapeT(n - 3)

# 2. Escreva uma definição recursiva para uma progressão geométrica com termo inicial a e razão r. (0,25)
P(n)={ a,         se n>1
     { r⋅P(n−1),  se n=1

# 3. Uma coleção T de números é definida recursivamente por: 
# Shape2 Î T 
# Se X Î T, então 	X+3 Î T 	e 	2*X Î T  
# Quais dos seguintes números pertencem a T? 6 , 7 , 19 , 12.
def pertence_a_T(numero):
  if numero == 2:
      return True
  elif numero < 2:
      return False
  else:
      return pertence_a_T(numero + 3) or pertence_a_T(2 * numero)

numeros = [6, 7, 19, 12]

for numero in numeros:
  if pertence_a_T(numero):
      print(f'{numero} pertencem a T')
  else:
      print(f'{numero} não pertencem a T')
R: 6 e 12

# 4. Uma coleção M de números é definida recursivamente por: 
# Shape2 Î M 	e 3 Î M 
# Se X Î M 	e 	Y Î M, então		X*Y Î M . 
# Quais dos seguintes números pertencem a M? 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218. 
def pertence_a_M(numero):
  if numero == 2 or numero == 3:
      return True
  elif numero < 2:
      return False
  else:
      for i in range(2, numero):
          if pertence_a_M(i) and pertence_a_M(numero // i):
              return True
      return False
    
numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for numero in numeros:
  if pertence_a_M(numero):
      print(f'{numero} pertencem a M')
  else:
      print(f'{numero} não pertencem a M')
R: 6, 9, 16, 21, 54, e 72.

  # 5. Uma coleção S de cadeias de caracteres é definida recursivamente por:  
  # Shapea Î S 	e 	b Î S 
  # Se X Î S, então 	Xb Î S. 
  # Quais das seguintes cadeias pertencem a S? a , ab , aba , aaab , bbbbb 
  def pertence_a_S(cadeia):
  
    if cadeia == 'Shapea' or cadeia == 'b':
        return True
    elif len(cadeia) > 1:
        return pertence_a_S(cadeia[:-1])
    else:
        return False

  cadeias = ['a', 'ab', 'aba', 'aaab', 'bbbbb']

  for cadeia in cadeias:
    if pertence_a_S(cadeia):
        print(f'A cadeia "{cadeia}" pertence a S')
    else:
        print(f'A cadeia "{cadeia}" não pertence a S')
  R: todas pertemcem a S

# 6. Uma coleção W de cadeias de símbolos é definida recursivamente por:  
# Shapea Î W, 	b Î W 		e 	c Î W  
# Se X Î W, então	 a(X)c Î W. 
# Quais das seguintes cadeias pertencem a S? a(b)c , a(a(b)c)c , a(abc)c , a(a(a(a)c)c)c , a(aacc)c 
def pertence_a_W(cadeia):
  if cadeia == 'Shapea' or cadeia == 'b' or cadeia == 'c':
      return True
  elif len(cadeia) > 2 and cadeia[0] == 'a' and cadeia[-1] == 'c':
      return pertence_a_W(cadeia[1:-1])
  else:
      return False

cadeias = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']

for cadeia in cadeias:
  if pertence_a_W(cadeia):
      print(f'A cadeia "{cadeia}" pertence a W')
  else:
      print(f'A cadeia "{cadeia}" não pertence a W')

R: Todas as cadeias dadas pertencem à coleção W.
  
# 7. Forneça uma definição recursiva para todas as cadeias binárias (cadeias formadas com os caracteres 0 e 1) contendo um número ímpar de zeros.
R: A cadeia vazia não pertence à coleção.
Se X é uma cadeia com um número ímpar de zeros, então X0 e X1 também têm um número ímpar de zeros.

# 8. Escreva o corpo da função recursiva para computar S(n) para uma dada seqüência S
# a) 1,3,9,27,...
def sequencia_a(n):
  if n == 1:
      return 1
  else:
      return 3 * sequencia_a(n - 1)
# b) 2, 1, 1/2, 1/4, ...
def sequencia_b(n):
  if n == 1:
      return 2
  else:
      return sequencia_b(n - 1) / 2
# c) a, b, a + b, a + 2b, 2a + 3b, ...
def sequencia_c(n, a, b):
  if n == 1:
      return a
  elif n == 2:
      return b
  else:
      return sequencia_c(n - 1, a, b) + sequencia_c(n - 2, a, b)
# d) p, p - q, p + q, p - 2q, p + 2q, p -3q, ...
def sequencia_d(n, p, q):
  if n % 2 == 1:
      return p - ((n - 1) // 2) * q
  else:
      return p + (n // 2) * q
# 9. Membros antigos da Sociedade de Pitágoras definiram números figurados como sendo o número de pontos em uma certa configuração geométrica. Os primeiros números triangulares são 1, 3, 6 e 10.
# Encontre a fórmula para o n-ésimo número triangular e escreva um programa recursivo.
def numero_triangular(n):
  if n == 1:
      return 1
  else:
      return numero_triangular(n - 1) + n

n = 10
resultado = numero_triangular(n)
print(f'O {n}-ésimo número triangular é: {resultado}')

# 10. Em um experimento, certa colônia de bactérias tem inicialmente uma população igual a 50.000. Uma leitura é feita a cada hora e, no final deste intervalo, há três vezes mais bactérias que antes. (a) Escreva a definição recursiva para A(n), o número de bactérias presentes no início do n-ésimo período de tempo. (0,25)(b) Em quantas leituras a população excederá 200.000 bactérias?
def numero_bacterias(n, populacao):
  if populacao > 200000:
      return n
  else:
      return numero_bacterias(n + 1, 3 * populacao)

populacao_inicial = 50000
resultado = numero_bacterias(0, populacao_inicial)

print(f"A população excederá 200.000 bactérias em {resultado} leituras.")
R: Duas Leituras.

  # 11.

Chamada inicial: L=[3,7,4,2,6]

A função encontra o maior item da lista entre 1 e 5 (i=2), troca [2] com L[5].
Lista após a troca: [3,6,4,2,7]
Chama Rotina(L,4)
Chamada recursiva 
Rotina Rotina(L,4):

A função encontra o maior item da lista entre 1 e 4 (i=2), troca L[2] com L[4].
Lista após a troca: [3,2,4,6,7]
Chama Rotina(L,3)
Chamada recursiva 
Rotina(L,3):

A função encontra o maior item da lista entre 1 e 3 (i=3), troca L[3] com L[3] (nenhuma troca).
Lista permanece a mesma: [3,2,4,6,7]
Chama Rotina(L,2)
Chamada recursiva 
Rotina(L,2):

A função encontra o maior item da lista entre 1 e 2 (i=1), troca L[1] com L[2].
Lista após a troca: [2,3,4,6,7]
Chama Rotina(L,1)
Chamada recursiva 
Rotina(L,1):

j é igual a 1, então a função retorna a lista.
Lista final: [2,3,4,6,7]
Total de chamadas realizadas à Rotina: 5

Portanto, a lista final após a chamada 
Rotina(L,5) é [2,3,4,6,7], e o total de chamadas realizadas é 5.
