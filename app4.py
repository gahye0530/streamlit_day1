import streamlit as st
import pandas as pd
def main() :

    df = pd.read_csv('data/iris.csv')
    if st.button('데이터보기') : st.dataframe(df)

    name = 'Mike'
    if st.button('대문자로') : st.write(name.upper())
    if st.button('소문자로') : st.write(name.lower())

if __name__ == '__main__' : main()