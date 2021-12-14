# 텍스트 인풋, 에어리어
# 숫자입력, 날짜입력
# 프린트문은 디버깅용이고 터미널에 출력된다.
import streamlit as st
import pandas as pd


def main() :
    name = st.text_input('First name')

    my_data = st.date_input('날짜 입력')
    st.write(my_data)
    my_time = st.time_input('시간 선택')
    st.write(my_time)


    # 비밀번호 입력
    password = st.text_input('비밀번호 입력', type = 'password')

    # 색깔 입력
    color = st.color_picker('색을 선택하세요')
    st.write(color)



    import streamlit as st


def main() :
    name = st.text_input('이름을 입력하세요!')
    st.title(name)

    name2 = st.text_input('이름을 입력하세요!',max_chars=5)
    st.title(name2)

    message = st.text_area('메세지를 입력하세요')
    st.text(message)

    #숫자 입력
    number = st.number_input('숫자를입력하세요~',1, 100)
    st.text(number)

    number2 = st.number_input('숫자를입력하세요~',0.0, 20.0)
    st.text(number2)

    #날짜
    my_date = st.date_input('약속 날짜 입력')
    st.write(my_date)
    print(my_date)  #print 는 디버깅용이고, 터미널에 출력된다.

    #시간
    my_time = st.time_input('시간 선택')
    st.write(my_time)

    #비밀번호 입력
    password = st.text_input('비번입력',type='password',max_chars=12)
    st.write(password)

if __name__=='__main__':
    main()





    
if __name__ == '__main__' :
    main()



