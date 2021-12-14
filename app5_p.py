import streamlit as st
import pandas as pd
from PIL import Image

def main() :

    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    st.image(img, use_column_width = True)
    vedio_file = open('data/video1.mp4', 'rb')
    st.video(vedio_file)
if __name__ == '__main__' : main()
