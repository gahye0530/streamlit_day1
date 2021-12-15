import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main() :
    st.title('Plotting with st.pyplot()')
    df = pd.read_csv('data/iris.csv')
    st.dataframe(df.head())

    fig = plt.figure()
    plt.scatter(data = df, x = 'sepal_length', y = 'sepal_width')
    plt.title('sepal length vs width')
    plt.xlabel('sepal length')
    plt.ylabel('sepal width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length', y = 'sepal_width')
    st.pyplot(fig2)

    # sepal_length로 히스토그램을 그려주세요.
    # bin의 갯수는 20개로 해주세요.

    fig3 = plt.figure(figsize = (10,4))
    plt.subplot(1,2,1)
    plt.hist(data = df, x = 'sepal_length', bins = 10, rwidth = 0.8)
    plt.subplot(1,2,2)
    plt.hist(data = df, x = 'sepal_length', bins = 20, rwidth = 0.8)
    st.pyplot(fig3)

    fig4 = plt.figure()
    sns.countplot(data = df, x = 'species')
    st.pyplot(fig4)

    fig5 = plt.figure()
    st.write(df['species'].value_counts())
    df['species'].value_counts().plot(kind = 'bar')
    st.pyplot(fig5)
    
    fig6 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig6)

if __name__ =='__main__' : main()