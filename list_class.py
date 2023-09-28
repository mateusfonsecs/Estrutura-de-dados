class ListaContigua:
    contador_adicao, contador_remocao = 0, 0
    def __init__(self, memoria):
        self.tamanho = 0
        self.memoria = memoria
        self.lista = [None] * self.memoria 


    def inserir(self, indice, valor):
    
        if 0 <= indice <= self.tamanho and self.tamanho < self.memoria :
            self.contador_adicao += 1
            for i in range(self.tamanho  , indice, -1):
                self.contador_adicao += 1
                self.lista[i] = self.lista[i - 1]
            self.lista[indice] = valor
            self.tamanho += 1
        else:
            raise IndexError("Índice fora dos limites da lista contígua")

    def remover(self, indice) :
        if 0 <= indice <= self.tamanho and self.tamanho < self.memoria :
            self.contador_remocao += 1
            valor_removido = self.lista[indice]
            for i in range(indice, self.tamanho - 1):
                self.contador_remocao += 1
                self.lista[i] = self.lista[i + 1]
            self.lista[self.tamanho - 1] = None
            self.tamanho -= 1
            return valor_removido
        else:
            raise IndexError("Índice fora dos limites da lista contígua")

    def acessar(self, indice):
        if 0 <= indice <= self.tamanho:
            return self.lista[indice]
        else:
            raise IndexError("Índice fora dos limites da lista contígua")

    def __str__(self):
        return str(self.lista)

class element():
    def __init__(self,valor):
        self.proximo = None
        self.valor = valor

class element2():
    def __init__(self,valor):
        self.proximo = None
        self.valor = valor
        self.anterior = None

class ListaDinamicaV1:
    contador_adicao, contador_remocao = 0, 0
    
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0

    
    def inserir(self, indice, valor):
        if 0 <= indice <= self.tamanho:
            new_element = element(valor)
            self.tamanho += 1
            if indice == 0:
                new_element.proximo = self.primeiro
                self.primeiro = new_element
                self.contador_adicao += 1
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    self.contador_adicao += 1
                    if i == indice -1:
                        aux = atual.proximo
                        atual.proximo = new_element
                        new_element.proximo = aux
                        break
                    else:
                        atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")

    def remover(self, indice):
        if 0 <= indice <= self.tamanho:
            self.contador_remocao += 1
            self.tamanho -= 1
            if indice == 0:
                self.primeiro = self.primeiro.proximo
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    self.contador_remocao += 1
                    if i == indice -1:
                        aux = atual.proximo.proximo
                        atual.proximo = aux
                        break
                    else:
                        atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")
    
    def acessar(self, indice):
        if 0 <= indice <= self.tamanho:
            if indice == 0:
                return self.primeiro.valor
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    if i == indice:
                        return atual.valor
                    else:
                        atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")

class ListaDinamicaV2:
    contador_adicao, contador_remocao = 0, 0
    
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
        self.ultimo = None
    
    def inserir(self, indice, valor):
        if 0 <= indice <= self.tamanho:
            new_element = element(valor)
            self.ultimo = new_element if self.tamanho == 0 else self.ultimo
            if indice == 0:
                new_element.proximo = self.primeiro
                self.primeiro = new_element
                self.contador_adicao += 1
            elif indice == self.tamanho:
                self.ultimo.proximo = new_element
                self.ultimo  = new_element
                self.contador_adicao += 1
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    self.contador_adicao += 1
                    if i == indice -1:
                        aux = atual.proximo
                        atual.proximo = new_element
                        new_element.proximo = aux
                        break
                    else:
                        atual = atual.proximo
            self.tamanho += 1
        else:
            raise IndexError("Índice fora dos limites da lista")

    def remover(self, indice):
        if 0 <= indice <= self.tamanho:
            self.contador_remocao += 1
            self.ultimo = None if self.tamanho == 1 else self.ultimo
            if indice == 0:
                self.primeiro = self.primeiro.proximo
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    self.contador_remocao += 1
                    if i == indice -1:
                        aux = atual.proximo.proximo
                        atual.proximo = aux
                        if indice == self.tamanho - 1:
                            self.ultimo = atual 
                        break
                    else:
                        atual = atual.proximo
            self.tamanho -= 1
        else:
            raise IndexError("Índice fora dos limites da lista")
    
    def acessar(self, indice):
        if 0 <= indice <= self.tamanho:
            if indice == 0:
                return self.primeiro.valor
            else:
                atual = self.primeiro
                for i in range(self.tamanho):
                    if i == indice:
                        return atual.valor
                    else:
                        atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")
        
class ListaDinamicaV3:
    contador_adicao, contador_remocao = 0, 0
    
    def __init__(self):
    
        self.tamanho = 0
        self.cabeca = element(None)
        self.ultimo = self.cabeca
    
    def inserir(self, indice, valor):
        if 0 <= indice <= self.tamanho:
            new_element = element(valor)

            if indice == self.tamanho:
                self.ultimo.proximo = new_element
                self.ultimo  = new_element
                self.contador_adicao += 1
            else:
                atual = self.cabeca
                for i in range(self.tamanho):
                    self.contador_adicao += 1
                    if i  == indice:
                        aux = atual.proximo
                        atual.proximo = new_element
                        new_element.proximo = aux
                        break
                    else:
                        atual = atual.proximo

            self.tamanho += 1
        else:
            raise IndexError("Índice fora dos limites da lista")

    def remover(self, indice):
        if 0 <= indice <= self.tamanho:
            atual = self.cabeca
            for i in range(self.tamanho):
                self.contador_remocao += 1
                if i == indice:
                    aux = atual.proximo.proximo
                    atual.proximo = aux
                    if indice == self.tamanho -1:
                        self.ultimo = atual 
                    break
                else:
                    atual = atual.proximo
            self.tamanho -= 1
        else:
            raise IndexError("Índice fora dos limites da lista")
    
    def acessar(self, indice):
        if 0 <= indice <= self.tamanho:
            atual = self.cabeca.proximo
            for i in range(self.tamanho):
                if i == indice:
                    return atual.valor
                else:
                    atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")

class ListaDinamicaV4:
    contador_adicao, contador_remocao = 0, 0
    
    def __init__(self):
    
        self.tamanho = 0
        self.cabeca = element2(None)
        self.ultimo = self.cabeca
    
    def inserir(self, indice, valor):
        if 0 <= indice <= self.tamanho:
            new_element = element2(valor)

            if indice == self.tamanho:
                self.ultimo.proximo = new_element
                new_element.anterior = self.ultimo
                self.ultimo  = new_element
                self.contador_adicao += 1
            else:
                atual = self.cabeca
                self.contador_adicao += 1
                for i in range(self.tamanho):
                    self.contador_adicao += 1
                    if i  == indice:
                        aux = atual.proximo
                        atual.proximo.anterior = new_element
                        atual.proximo = new_element
                        new_element.anterior = atual
                        new_element.proximo = aux
                        break
                    else:
                        atual = atual.proximo

            self.tamanho += 1
        else:
            raise IndexError("Índice fora dos limites da lista")

    def remover(self, indice):
        if 0 <= indice <= self.tamanho:
            if indice == self.tamanho - 1:
                self.contador_remocao += 1
                last_node = self.ultimo
                self.ultimo = last_node.anterior
                self.ultimo.proximo = None
            self.tamanho -= 1
        else:
            raise IndexError("Índice fora dos limites da lista")
    
    def acessar(self, indice):
        if 0 <= indice <= self.tamanho:
            atual = self.cabeca.proximo
            for i in range(self.tamanho):
                if i == indice:
                    return atual.valor
                else:
                    atual = atual.proximo
        else:
            raise IndexError("Índice fora dos limites da lista")

if __name__ == "__main__":
    lista_c = ListaDinamicaV4()
    # lista_c = ListaContigua(5)
    lista_c.inserir(0, 10)
    lista_c.inserir(1, 20)
    lista_c.inserir(2, 30)
    lista_c.inserir(0, 1)
    lista_c.remover(4)
    lista_c.remover(0)
    print(lista_c.acessar(0))  

    lista_c.remover(0)


