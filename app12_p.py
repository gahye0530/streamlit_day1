import streamlit as st
import numpy as np
import pandas as pd

import altair as alt
import plotly.express as px

def main() :
    df1 = pd.read_csv('data/lang_data.csv')
    st.dataframe(df1)
    print(df1.columns[1:])
    lang_list = df1.columns[1:]
    choice_list = st.multiselect('언어를 선택하세요', lang_list)
    print(choice_list)
    if len(choice_list) != 0 :
        df_selected = df1[choice_list]
        st.line_chart(df_selected)
        st.area_chart(df_selected)

    df2 = pd.read_csv('data/iris.csv')
    df_selected2 = df2[['sepal_length', 'petal_length']]
    st.bar_chart(df_selected2)

    chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )
    st.altair_chart(chart)


    df3 = pd.read_csv('data/location.csv', index_col=0)
    st.write(df3)
    st.map(data = df3)

    df4 = pd.read_csv('data/prog_languages_data.csv', index_col = 0)
    st.dataframe(df4)

    fig1 = px.pie(df4,'lang','Sum',title = '각 언어별 파이차트')
    st.plotly_chart(fig1)

    df4_sorted = df4.sort_values('Sum', ascending = False)
    fig2 = px.bar(df4_sorted, x = 'lang', y = 'Sum')
    st.plotly_chart(fig2)
if __name__ == '__main__' : main()