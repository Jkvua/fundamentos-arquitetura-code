from mini_orion.checkout import Carrinho, Cliente, ItemCarrinho, ServicoCheckout

cliente1 = Cliente(
    nome="Eduardo", email="eduardo.silva@ifc.edu.br", cartao="44454444444"
)
carrinho_cliente1 = Carrinho(
    itens=[
        ItemCarrinho(sku="1", preco_unitario=10.0, quantidade=2),
        ItemCarrinho(sku="2", preco_unitario=20.0, quantidade=3),
    ]
)

print("Valor total do carrinho")
total = sum(item.subtotal for item in carrinho_cliente1.itens)
print(total)
checkout = ServicoCheckout()
resultado = checkout.fechar_pedido(carrinho_cliente1, cliente1)
print(f"Resultado do checkout: {resultado}")
