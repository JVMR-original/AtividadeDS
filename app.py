import streamlit as st
import cadproduto
import cadvenda
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
def carregar_vendas():
    vendas = []
    with open("vendas.txt", "r") as f:
        for line in f:
            data, produto, quantidade, valor_total = line.strip().split(",")
            vendas.append({
                "data": data,
                "produto": produto,
                "quantidade": int(quantidade),
                "valor_total": float(valor_total)
            })
    return vendas
st.title("Controle de Estoque")
menu = st.sidebar.selectbox("Menu", ["Visualizar Dados", "Cadastrar Produto", "Registrar Venda"])
if menu == "Visualizar Dados":
    st.header("Produtos Cadastrados")
    produtos = carregar_produtos()
    if produtos:
        for p in produtos:
            st.text(f"{p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['quantidade']}")
    else:
        st.info("Nenhum produto cadastrado.")
    st.header("Histórico de Vendas")
    vendas = carregar_vendas()
    if vendas:
        for v in vendas:
            st.text(f"{v['data']} - {v['produto']} - {v['quantidade']} un. - R$ {v['valor_total']:.2f}")
    else:
        st.info("Nenhuma venda registrada.")
elif menu == "Cadastrar Produto":
    cadproduto.run()
elif menu == "Registrar Venda":
    cadvenda.run()