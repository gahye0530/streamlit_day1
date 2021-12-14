### 파일 업로드 하는 방법 ###

import streamlit as st
from PIL import Image
import pandas as pd
import os

# 디렉토리 정보와 파일을 알려주면 해당 디렉토리에 파일을 저장하는 함수를 만들겁니다. 
def save_upload_file(directory, file) :
    # 1. 디렉토리가 있는지 확인 후 없으면 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success('Save file : {} in {}' .format(file.name, directory))

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
            # 파일명을 현재시간의 조합으로 해서 만들어 보세요.


            # 파일을 저장할 수 있도록 위의 함수를 호출하자.
            save_upload_file('temp', image_file)
            # 파일을 화면에 나오게
            img = Image.open(image_file)
    elif choice == 'CSV' :
        st.subheader('CSV 파일 업로드')
        data_file = st.file_uploader('CSV', type = ['csv'])
        if data_file is not None :
            print(data_file.name)
            print(data_file.size)
            print(data_file.type)
            # 파일명을 내가 마음대로 바꿔서 업로드 하는 코드
            # 예) test.csv

            # 파일명을 현재시간을 활용해서 이름을
            save_upload_file('csv_files', data_file)
            df = pd.read_csv(data_file)
            st.dataframe(df)
            
    elif choice == 'About' :
        st.subheader('파일 업로드 프로젝트 입니다.')
if __name__ == '__main__' : main()
