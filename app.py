from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

# restaurante praça
restaurante_praca = Restaurante('Praça', 'Gourmet')

# objetos do restaurante
prato_pao = Prato('Pão', 2.00, 'O melhor pão da cidade')
bebida_suco = Bebida('Suco de melancia', 5.00, 'Grande')
sobremesa_pudim = Sobremesa('Pudim de chocolate', 9.00, 'Gostosa')

bebida_suco.aplicar_desconto()
prato_pao.aplicar_desconto()
sobremesa_pudim.aplicar_desconto()

# metodos de instancia
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


def main():
    restaurante_praca.exibir_cardapio()


if __name__ == '__main__':
    main()
