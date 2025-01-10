import requests
import streamlit as st

def buscar_letra(banda,musica):
    endpoint=f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra= response.json()["lyrics"] if response.status_code==200 else""
    return letra

st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")


banda = st.text_input("digite o nome da banda: ",key="banda")
musica= st.text_input("digite o nome da musica",key="musica")
pesquisar = st.button("pesquisar")

if pesquisar:
    letra = buscar_letra(banda,musica)
    if letra:
        st.success("Encontramos a letra da musica")
        st.text(letra)
    else:
        st.error("Não achamos a letra da musica")