import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import date, datetime

def save_uploaded_file(directory, file) :
    if not os.path.exists(directory) :
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    
    return st.success('Saved file : {} in {}' .format(file.name, directory))


def main() :
    st.title('파일 업로드 프로젝트')
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == 'Image' :
        st.subheader('이미지 파일 업로드')
        image_file = st.file_uploader('이미지를 업로드 하세요', type = ['png', 'jpg', 'jpeg'])
        if image_file is not None :
            print(type(image_file))
            print(image_file.name)
            print(image_file.size)
            print(image_file.type)
        save_uploaded_file('temp', image_file)
        img = Image.open(image_file)
        st.image(img, use_column_width=True)
    elif choice == 'CSV' :
        st.subheader('CSV 파일 업로드')
        csv_file = st.file_uploader('CSV파일을 업로드 하세요', type = 'csv')
        if csv_file is not None :
            print(csv_file.name)
            print(csv_file.size)
            print(csv_file.type)
        save_uploaded_file('csv_files', csv_file)
        df = pd.read_csv(csv_file)
        st.dataframe(df)


    elif choice == 'About' :
        st.subheader('파일 업로드 프로젝트 입니다.')


if __name__ == '__main__' : main()