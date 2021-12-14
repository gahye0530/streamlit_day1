import streamlit as st
import pandas as pd

def main() :
    name = st.text_input('이름을 입력하세요!')
    st.title(name)

    name2 = st.text_input('이름일 입력하세요!', max_chars=5)
    st.title(name2)

    message = st.text_area('메시지를 입력하세요')
    st.text(message)

    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)
    print(my_date)

    my_time = st.time_input('시간 선택')
    st.write(my_time)

    my_pw = st.text_input('패스워드 입력', type = 'password')

if __name__ == '__main__' : main()