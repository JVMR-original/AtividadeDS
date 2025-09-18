import streamlit as st
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)
    def to_line(self):
        return f"{self.nome},{self.preco},{self.quantidade}\n"
def salvar_produto(produto):
    with open("produtos.txt", "a") as f:
        f.write(produto.to_line())
def run():
    st.header("Cadastro de Produtos")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade em estoque", min_value=0, format="%d")
    if st.button("Cadastrar Produto"):
        if nome and preco >= 0 and quantidade >= 0:
            produto = Produto(nome, preco, quantidade)
            salvar_produto(produto)
            st.success("Produto cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")