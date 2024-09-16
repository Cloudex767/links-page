#My linktr.ee
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout="centered", page_icon="✈️", page_title="Rian Vinícius")

# Função para carregar animações Lottie de uma URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    col1, col2, col3 = st.columns([1, 1, 1])
    
    # Carregar a imagem da foto
    image = Image.open("foto.png")  # Certifique-se que "foto.png" está na mesma pasta
    img = image.resize((280, 280))
    
    # Carregar animação Lottie de uma URL
    lottie_url = "https://assets2.lottiefiles.com/packages/lf20_x62chJ.json"  # URL de exemplo da animação
    lottie_animation = load_lottieurl(lottie_url)
    
    with col1:
        # Exibir a animação Lottie
        if lottie_animation:
            st_lottie(lottie_animation, height=200, width=200)
        else:
            st.error("Não foi possível carregar a animação Lottie.")
    with col2:
        st.image(img)
        st.header("RIAN VINÍCIUS")
    
    st.write("---")
    with st.expander("🖥 Desenvolvimento de software", expanded=True):
        col1, col2 = st.columns([2,1])
        with col1:
            st.write("Habilidades: \n"
                     "- Python;\n"
                     "- Web (HTML, CSS e JS)\n"
                     "- Desenvolvimento android;\n")
        with col2:
            img_sftwr = Image.open("img-sftwr.png")
            img_sftwr = img_sftwr.resize((200,200))
            st.image(img_sftwr)
        st.write("Desenvolvo aplicativos e páginas web para ajudar você a alcançar mais!")
        st.write("---")
        
        st.button("Mega pack de ferramentas - Em breve", use_container_width=True)
        st.link_button("Contato para serviços ...","https://api.whatsapp.com/send?phone=5532991458306&text=Ol%C3%A1,%20tenho%20interesse%20nos%20servi%C3%A7os%20de%20programação",use_container_width=True)
        st.link_button("Quero ter uma página como essa!", "https://api.whatsapp.com/send?phone=5532991458306&text=Ol%C3%A1,%20tenho%20interesse%20nos%20servi%C3%A7os%20de%20programação",use_container_width=True)
    with st.expander("✨ Designer",expanded=True):
        col1, col2 = st.columns([2,1])
        with col1:
            st.write("- 172h certificadas de: Coreldraw X6 , Photoshop CS6 , \n"
                     "Flash CS6 , Autocad , 3D Studio")
            st.write("- Designer oficial do aplicativo *14Bis Drive* de Santos Dumont - MG")
            st.link_button("14Bis drive", "https://play.google.com/store/apps/details?id=br.com.quatorzebisdrive.passenger.drivermachine&pli=1")
        with col2:
            img_designer = Image.open("img-designer.png")
            img_designer = img_designer.resize((300,300))
            st.image(img_designer)
        st.write("---")
        st.link_button("Acesse meu portifolio:","https://drive.google.com/drive/u/0/folders/131f4dQudYhQkrgGi0yJmOJtLCLNhuWcS", use_container_width=True)
        st.link_button("Contato para serviços ...","https://api.whatsapp.com/send?phone=5532991458306&text=Ol%C3%A1,%20tenho%20interesse%20nos%20servi%C3%A7os%20de%20designer", use_container_width=True)
    with st.expander("🗞 Artes", expanded=True):
        col1, col2 = st.columns([2,1])
        with col1:
            st.write("Sou artista especializado em desenho realista. Minha paixão é capturar a beleza e a complexidade do mundo com detalhes precisos e mensagens empolgantes. Através de cada linha e sombra, busco refletir a verdadeira essência dos meus sujeitos, seja em retratos, paisagens ou objetos cotidianos. Estou aberto a novos desafios e colaborações. Se desejar saber mais sobre meu trabalho, estou à disposição.")
        with col2:
            img_draw = Image.open("img-draw.png")
            img_draw = img_draw.resize((200,200))
            st.image(img_draw)
        st.write("---")
        #st.button("Veja minhas artes - Em breve", use_container_width=True)
        st.link_button("Instagram","https://www.instagram.com/rianvinicius_/", use_container_width=True)
    st.write("---")
    st.subheader("Links úteis")
    col7, col8, col9 = st.columns([1,1,1])
    with col7:
        st.write("Parceiros")
        st.link_button("Andressa Nassaralla", "https://www.instagram.com/andressa_nassaralla/", use_container_width=True)
        st.link_button("SXP Toque de Eros", "https://www.instagram.com/sxptoque_d_eros/", use_container_width=True)
     
    st.write("Acesse meu currículum")
    #file_path = 'curriculo-rian.pdf'
    #with open(file_path, 'rb') as file:
        #file_data = file.read()
    #st.download_button(label="Baixar PDF",data=file_data,file_name='curriculo-rian.pdf',mime='./', use_container_width=True)
    st.link_button("Contato direto","https://api.whatsapp.com/send?phone=5532991458306", use_container_width=True)
    st.write("")
    col4, col5, col6 = st.columns([1,1,1])
    with col5:
        st.write("A app by: Rian Vinícius | Todos os direitos reservados © 2024", use_container_width=True)
    
main()

        
    
