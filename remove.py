#Un script python qui permet de supprimer l'arrière-plan d'une image téléchargée par l'utilisateur via une interface web Streamlit.
import streamlit as st #Importation de la bibliothèque Streamlit
from PIL import Image #Importation de la bibliothèque PIL pour la manipulation d'images
from rembg import remove #Importation de la fonction remove de la bibliothèque rembg pour la suppression d'arrière-plan
from io import BytesIO #Importation de BytesIO pour la gestion des flux de données en mémoire


st.set_page_config(page_title="Image Removal Tool", page_icon="🖼️", layout="wide", ) #Configuration de la page Streamlit

st.write("# Image Removal Tool") #Titre de la page
st.write("Upload an image and remove its background easily!") #Description de la page   
st.sidebar.write("## Uploader") #Titre de la barre latérale   

col1, col2 = st.columns(2) #Création de deux colonnes pour l'interface utilisateur  


#Fonction pour convertir l'image en png
def convert_image(image):
    buf = BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

#Fonction pour afficher l'image originale et l'image sans arrière-plan
def fix_image(image):
    image = Image.open(image)
    col1.write("**Original Image**")
    col1.image(image)
    
    fixed = remove(image)
    col2.write("**Image without Background**")
    col2.image(fixed)

    st.sidebar.write("\n")
    st.sidebar.download_button("Download Image without Background", convert_image(fixed), "image_no_bg.png", "image/png")

#On charge l'image
image_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

#Si une image est téléchargée, on la traite
if image_upload is not None:
    fix_image(image_upload)
else:
    #st.sidebar.write("Please upload an image to remove its background.")
    fix_image("./images/ours.jpg")