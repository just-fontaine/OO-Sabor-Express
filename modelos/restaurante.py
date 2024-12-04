from os import system
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


def linha():
    print('\033[33m-\033[m' * 81)


class Restaurante:
    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)


    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    

    @property
    def ativo(self):
        if self._ativo:
            return ' Ativo'
        else:
            return 'Inativo'
    
    
    @classmethod
    def listar_restaurantes(cls):
        system('cls')
        linha()
        print(f' {'Nome'.ljust(25)} {'Categoria'.ljust(25)} {'Avaliação'.ljust(20)} {'Status'}')
        linha()
        
        for restaurante in cls.restaurantes:
            print(f' {restaurante._nome.ljust(26)} {restaurante._categoria.ljust(27)} {str(restaurante.media_avaliacao).ljust(16)} {restaurante.ativo}')
        linha()
    

    def alternar_status(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        else:
            media = sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao)
            return media


    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
        else:
            raise ValueError('Não é possível adicionar esse item ao cardápio')


    def exibir_cardapio(self):
        print(f'\nCardápio restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'tamanho'):
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            elif hasattr(item, 'tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tipo: {item.tipo}'
                print(mensagem_sobremesa)
