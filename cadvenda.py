import streamlit as st
from datetime import datetime
class Venda:
    def __init__(self, data, produto, quantidade, valor_total, cliente_cpf):
        self.data = data
        self.produto = produto
        self.quantidade = int(quantidade)
        self.valor_total = float(valor_total)
        self.cliente_cpf = cliente_cpf
    def to_line(self):
        return f"{self.data},{self.produto},{self.quantidade},{self.valor_total},{self.cliente_cpf}\n"
def carregar_produtos():
    produtos = []
    with open("produtos.txt", "r") as f:
        for line in f:
            nome, preco, quantidade = line.strip().split(",")
            produtos.append({
                "nome": nome,
                "preco": float(preco),
                "quantidade": int(quantidade)
            })
    return produtos
def carregar_clientes():
    clientes = []
    with open("cliente.txt", "r") as f:
        for line in f:
            cpf, nome, *_ = line.strip().split(",")
            clientes.append({"cpf": cpf, "nome": nome})
    return clientes
def salvar_venda(venda):
    with open("vendas.txt", "a") as f:
        f.write(venda.to_line())
def atualizar_estoque(produtos):
    with open("produtos.txt", "w") as f:
        for p in produtos:
            f.write(f"{p['nome']},{p['preco']},{p['quantidade']}\n")
def run():
    st.header("Registrar Venda")
    produtos = carregar_produtos()
    clientes = carregar_clientes()
    if not produtos:
        st.warning("Não há produtos cadastrados para venda.")
        return
    if not clientes:
        st.warning("Nenhum cliente cadastrado.")
        return
    nomes_produtos = [p["nome"] for p in produtos]
    produto_escolhido = st.selectbox("Escolha o produto", nomes_produtos)
    cliente_nomes = [f"{c['nome']} ({c['cpf']})" for c in clientes]
    cliente_escolhido = st.selectbox("Escolha o cliente", cliente_nomes)
    quantidade_vendida = st.number_input("Quantidade", min_value=1, format="%d")
    if st.button("Registrar Venda"):
        for p in produtos:
            if p["nome"] == produto_escolhido:
                if quantidade_vendida > p["quantidade"]:
                    st.error("Estoque insuficiente.")
                else:
                    p["quantidade"] -= quantidade_vendida
                    total = quantidade_vendida * p["preco"]
                    cliente_cpf = cliente_escolhido.split("(")[-1].replace(")", "")
                    venda = Venda(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), p["nome"], quantidade_vendida, total, cliente_cpf)
                    salvar_venda(venda)
                    atualizar_estoque(produtos)
                    st.success(f"Venda registrada! Total: R$ {total:.2f}")
                break