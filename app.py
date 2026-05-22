import streamlit as st 
st.title("Velvet Lane's  - Aluguel de carros")                                                                           
st.subheader("Dirija sua essência!")
st.sidebar.title("Escolha um modelo")
st.sidebar.image("logo.png")


carros =["Porsche", "BMW", "Audi", "ferrari", "lamborghini"]

opcao = st.sidebar.selectbox("Selecione o modelo alugado", carros)


st.image(f"{opcao}.png")
st.markdown(f"Você escolheu o modelo: {opcao}!")
st.markdown("---")