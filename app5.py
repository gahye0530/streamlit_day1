import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    ## 넘파이이다.
    img =Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    
    st.image(img, use_column_width= True)
    video_file = open('data/video1.mp4', 'rb')
    st.video(video_file)
    
    # audio_file 도 동일하게
    # st.audio(audio_file.read(), format='audio/mp3')

if __name__ == '__main__' :
    main()