import  streamlit as st
import util
import base64
from PIL import Image
st.markdown("<h1 style='text-align: center;'>Sports Celebrity Image Classification</h1>", unsafe_allow_html=True)
image=st.file_uploader("Please upload the image you want to classify",type=['jpg'])
if image:
    # img=Image.open(image)
    # width=4
    # height=6
    # img=img.resize(width,height)
    # resized_image = img.resize((1200,600))
    image_content=image.getvalue()
    encoded_image = base64.b64encode(image_content).decode('utf-8')
    # image_path=image.getbuffer()
    # st.write(image_path)
    st.image(image)
    util.load_saved_artifacts()
    result=util.classify_image(encoded_image)
    st.write(f"The image uploaded above is of {result}")



