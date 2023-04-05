from typing import List

# Importação das bibliotecas

class MyClass1:
    __var1: List[int]
    __var2: str
    # Criação das classes, definindo que __var1 é uma lista de números inteiros e __var2 é uma string.
    # Uso de "__" antes das váriaveis significa que são váriaveis privadas da classe, e só podem ser acessadas dentro dela.
    # Técnica de encapsulamento.

    def __init__(self, var1: List[int], var2: str):
        self.__var1 = var1
        self.__var2 = var2
    # Definição do método __init__ para uma classe, recebe como parâmetro as duas variáveis criadas anteriormente.
    # Dentro do método, é atribuido os valores dos parâmetros às duas váriaveis de instância.

    def get_var1(self) -> List[int]: #Indica que o método retorna uma lista de inteiros.
        return self._var1
    # Método que retorna o valor da variável privada __var1.

    def set_var1(self, var1: list[int]) -> None: #para indicar que o método não retorna nada.
        self.__var1 = var1
    # Define o valor da variável privada __var1 para o valor passado como argumento: "var1", que é a lista de números inteiros.

    def get_var2(self):
        return self.__var2
    # Método que retorna o valor da variável privada __var2.

    def set_var2(self, var2: str):
        self.__var2 = var2
    # Define o valor da variável privada __var2 para o valor passado como argumento: "var12", que é uma string.

    def method1(self) -> bool:  # bool -> variável booleana
        aux = self.__var1.copy()  # Copia a lista que está em __var1 e o chama de aux
        aux.sort()  # ordena a lista aux
        # usa um loop for para iterar a lista do índice 1 ao comprimento total da lista
        for i in range(1, len(aux)):
            if aux[i] == aux[i-1]:  # verifica se o elemento anterior é igual ao atual, se encontrar um valor duplicado, retorna True
                return True
        # Se o loop for concluído sem retornar True, retornará False.
        return False

    # Método que retorna um valor booleano(true/false).

    # Método recebe argumento target como número inteiro e retorna uma lista de números inteiros.
    def method2(self, target: int) -> List[int]:
        seen = {}  # Cria um dicionário vazio chamado seen
        # Itera a lista __var1 em um loop com a função enumerate, que vai retornar o índice e o valor do elemento
        for i, value in enumerate(self.__var1):
            # cada iteração, subtrai o valor atual "self.__var" de "target" para ver a quantidade restante que precisa encontrar na fila
            remaining = target - self.__var1[i]

            if remaining in seen:  # verifica a quantidade restante, se ela está no dicionário seen. se for vista, retornara o índice "i", e o índice da palavra com a quantidade restante
                return [i, seen[remaining]]
            else:
                # se a quantidade restante não for vista, adiciona o valor atual 'value' e o índice 'i' ao dicionário
                seen[value] = i

    def method3(self, k: int) -> List[int]:
        nums = self.__var1.copy()
        k = k % len(nums)
        n = len(nums)
        i = 0
        count = 0
        while count < n:
            pos = (i + k) % len(nums)
            curr = nums[pos]
            nums[pos] = nums[i]
            count += 1
            j = pos
            while j != i and count < n:
                pos = (j + k) % len(nums)
                nums[pos], curr = curr, nums[pos]
                j = pos
                count += 1
            i += 1
        return nums

    def method4(self) -> str:
        return self.__var2[::-1]
        # Retorna a string inversa que está armazenada na variável __var2

    @staticmethod
    def method5(x: List[int], y: List[int]) -> int:

        z = [*x, *y]
        z.sort()
        if len(z) % 2 == 0:
            result = (z[len(z)//2] + z[len(z)//2-1])/2

        else:
            result = z[len(z)//2]

        return result

    # recebe duas listas de inteiros como argumentos, x e y. O método combina as duas listas usando o operador "*" e ordena a lista resultante z usando o método sort().
    # verifica se o comprimento da lista z é par ou ímpar. Se for par, ele calcula a média dos dois elementos do meio da lista usando a divisão inteira //. Se for ímpar, ele retorna simplesmente o elemento do meio.
    # o resultado final será um número inteiro.
