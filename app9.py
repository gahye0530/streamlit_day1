### 여러 파일을 업로드 하는 app ###
import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import date, datetime

# 파일 업로드하는 함수
def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))


# 여러파일 업로드
# accept_multiple_files=True


def main() :
    st.title('여러 파일들을 업로드 하는 앱')

    #사이드바용 메뉴
    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox("메뉴", menu)

    if choice == 'Image':
        uploaded_files = st.file_uploader('이미지 파일 업로드',type = ['png','jpg','jpeg'], accept_multiple_files=True)
        print(uploaded_files)

        if uploaded_files is not None :
            for file in uploaded_files :
                save_uploaded_file('temp_files',file)

                img = Image.open(file)
                st.image(img)

    ### CSV 파일 여러개 올리는 코드를 아래 작성하시오.
    ### CSV 파일명은 시간.csv 조합된 파일명으로 저장하시오.
    elif choice == 'CSV':
        csv_uploaded_files = st.file_uploader('CSV 파일 업로드', type=['CSV'],accept_multiple_files=True)
        print(csv_uploaded_files)

        if csv_uploaded_files is not None :
            for file in csv_uploaded_files :
                current_time = datetime.now()
                print(current_time)
                print(current_time.isoformat().replace(':', '_'))
                current_time = current_time.isoformat().replace(':', '_')
                csv_uploaded_files.name = current_time + '.csv'

                # file.name = current_time + '.csv'
                save_uploaded_file('csv_files_2',file)
                


if __name__=='__main__':
    main()
