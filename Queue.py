from list_class import ListaContigua, ListaDinamicaV1, ListaDinamicaV2, ListaDinamicaV3, ListaDinamicaV4

class deque:
    def __init__(self, type_list = 0, tamanho=1000000):
        
        self.size = 0
        self.type_list = type_list
        self.tamanho = tamanho

        if self.type_list  == 0:
            self.queue = ListaContigua(tamanho)
            self.queue = ListaContigua(tamanho)
        elif self.type_list  == 1:
            self.queue = ListaDinamicaV1()
            self.queue = ListaDinamicaV1()
        elif self.type_list  == 2:
            self.queue = ListaDinamicaV2()
            self.queue = ListaDinamicaV2()
        elif self.type_list  == 3:
            self.queue = ListaDinamicaV3()
            self.queue = ListaDinamicaV3()
        elif self.type_list  == 4:
            self.queue = ListaDinamicaV4()
            self.queue = ListaDinamicaV4()

    def controla(self):
        if self.type_list == 0:
            self.enf = self.size 
            self.des = 0
        elif self.type_list == 1:
            self.enf = 0
            self.des = self.size - 1
        elif self.type_list == 2 or self.type_list == 3:
            self.enf = self.size 
            self.des = 0
        elif self.type_list == 4:
            self.enf = 0
            self.des = self.size - 1


    def enfileirar(self, data):
        self.controla()
        # Verifique se a fila ainda não atingiu o tamanho máximo
        if self.size < self.tamanho:
            self.queue.inserir(self.enf, data)
            self.size += 1
        else:
            raise IndexError("A fila está cheia")

    def desenfileirar(self):

        self.controla()
        if self.size > 0:
            info = self.queue.acessar(self.des)
            self.queue.remover(self.des)
            self.size -= 1
            return info
        else:
            raise IndexError("A fila está vazia")

    def frente(self):
        # Verifique se a fila não está vazia
        if self.size > 0:
            return self.queue.acessar(0)

    def limpar(self):
        while self.size != 0:
            self.desenfileirar()

    def __len__(self):
        return self.size

if __name__ == "__main__":
    fila = deque()