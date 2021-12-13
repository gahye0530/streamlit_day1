import streamlit as st
import pandas as pd
def main() :

    df = pd.read_csv('data/iris.csv')
    if st.button('데이터보기') : st.dataframe(df)

if __name__ == '__main__' : main()