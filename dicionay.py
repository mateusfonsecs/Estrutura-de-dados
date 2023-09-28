from Queue import deque
import matplotlib.pyplot as plt
import numpy as np
class DictionaryWithQueue:

    def __init__(self, versao):
        self.keys = deque(versao)
        self.values = deque(versao)
        self.tamanho = 0

    def adicionar(self, key, value):

        self.keys.enfileirar(key)
        self.values.enfileirar(value)
        self.tamanho += 1

    def remover(self, key):

        for _ in range(self.tamanho):
            var_key = self.keys.desenfileirar()
            var_value = self.values.desenfileirar()
            if var_key == key:
                self.tamanho -= 1
                return
            self.keys.enfileirar(var_key)
            self.values.enfileirar(var_value)

            
    def busca(self, chave):

        for i in range(self.tamanho):
            var_key = self.keys.desenfileirar()
            var_value = self.values.desenfileirar()
            self.keys.enfileirar(var_key)
            self.values.enfileirar(var_value)
            if var_key == chave:
                return var_value
            
    def limpar(self):
        while self.tamanho != 0:
            self.keys.desenfileirar()
            self.values.desenfileirar()


if __name__ == '__main__':
    lista_total = []
    nomes = ['Contígua', 'Dinâmica V1', 'Dinâmica V2', 'Dinâmica V3', 'Dinâmica V4']
    for k in range(5):
        lista = []
        for j in range(1, 101):
            my_dict = DictionaryWithQueue(k)

            for i in range(j):  # Vai de 0 a 100
                chave = f"chave{i}"
                valor = f"valor{i}"
                my_dict.adicionar(chave, valor)

            chave_busca = f"chave{i}"
            valor_encontrado = my_dict.busca(chave_busca)
            l = 5 if k > 1 else 20 
            lista.append((my_dict.keys.queue.contador_remocao + k*50))
            print(f"Valor da chavee '{chave_busca}': {valor_encontrado}")
            lista_total.append(lista)
            valores_x = np.arange(1,101)

        plt.plot(valores_x, lista, label=nomes[k])
    plt.ylabel('número de repetições')
    plt.xlabel('n')
    plt.title('Ordem de Crescimento')
    plt.legend()
    plt.savefig('fig1.jpg')
    plt.show()






