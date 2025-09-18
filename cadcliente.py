import streamlit as st
import requests
class Cliente:
    def __init__(self, cpf, nome_completo, data_nascimento, cep, endereco, telefone):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.cep = cep
        self.endereco = endereco
        self.telefone = telefone
    def to_line(self):
        return f"{self.cpf},{self.nome_completo},{self.data_nascimento},{self.cep},{self.endereco},{self.telefone}\n"
def salvar_cliente(cliente):
    with open("cliente.txt", "a") as arquivo:
        arquivo.write(cliente.to_line())
def buscar_endereco_por_cep(cep):
    resposta = requests.get(f"https://brasilapi.com.br/api/cep/v1/{cep}")
    dados = resposta.json()
    if all(chave in dados for chave in ["street", "neighborhood", "city", "state"]):
        rua = dados["street"]
        bairro = dados["neighborhood"]
        cidade = dados["city"]
        estado = dados["state"]
        return f"{rua}, {bairro}, {cidade}-{estado}"
    else:
        return None
def run():
    st.header("Cadastro de Cliente")
    cpf = st.text_input("CPF")
    nome_completo = st.text_input("Nome completo")
    data_nascimento = st.date_input("Data de nascimento")
    cep = st.text_input("CEP")
    endereco = ""
    if cep and len(cep) == 8 and cep.isdigit():
        endereco_api = buscar_endereco_por_cep(cep)
        if endereco_api:
            endereco = endereco_api
            st.success(f"Endereço encontrado: {endereco}")
        else:
            st.error("CEP não encontrado ou inválido.")
    elif cep:
        st.warning("CEP deve conter 8 dígitos numéricos.")
    telefone = st.text_input("Telefone")
    if st.button("Cadastrar Cliente"):
        if cpf and nome_completo and endereco and telefone:
            cliente = Cliente(
                cpf,
                nome_completo,
                data_nascimento.strftime("%Y-%m-%d"),
                cep,
                endereco,
                telefone
            )
            salvar_cliente(cliente)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.error("Preencha todos os campos corretamente.")