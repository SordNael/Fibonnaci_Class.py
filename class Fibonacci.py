class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def primeiro_metodo(self):
        FibDict = {0:0, 1:1, 2:1}

        if self.n in FibDict:
            return FibDict[self.n]
    
        else:
            for S in range (2,self.n + 1):
                if S not in FibDict:
                    FibDict[S] = FibDict[S-2] + FibDict[S-1]
        
        return FibDict[self.n]

    def segundo_metodo(self):
        fib = [0, 1, 1]
  
        any(map(lambda _: fib.append(sum(fib[-2:])), range(2, self.n)))
  
        return fib[self.n]
    
    def check(self):
        def quadrado(x):
            y = x**0.5
            return y*y == x

        def esta_em_Fibonacci(x):
            return quadrado(5*x*x + 4) or quadrado(5*x*x - 4)

        if (esta_em_Fibonacci(self.n) == True):       
            return ("É um número em Fibonacci")

'''
os metodos criam uma forma de memoizar os números da sequência de Fibonacci, 
enquanto o check confere se é verdadeira a condição que o número dado é um quadrado perfeito,
caso seja, pela forma de binet, é possível saber se o número pertence à sequência Fibonacci


Exemplo de execução abaixo
'''
onze = Fibonacci(11)

doze = Fibonacci(12)

resultado = onze.primeiro_metodo(),doze.segundo_metodo(), doze.segundo_metodo()

numero = Fibonacci(832040)

checagem = numero.check()

print('{}, {}'.format(resultado, checagem))
