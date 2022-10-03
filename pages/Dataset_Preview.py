import streamlit as st
import seaborn as sns
import pandas as pd

df = pd.read_csv("diamonds.csv")

st.set_page_config(page_title="Dataset", page_icon="📊",layout="wide")
st.header("Diamond Dataset Preview")

dt= st.radio('Show in dataset (Head/Tail)',('Head','Tail'))
if dt=='Head':
    st.dataframe(df.head(10))
else:
    st.dataframe(df.tail(10))

ds= st.checkbox('Show the whole dataset')
if ds:
    st.dataframe(df)

sh= st.selectbox('Check',('Select','Shape','Columns','Statistical Description'))
if sh=='Shape':
    st.write(df.shape)
elif sh=='Columns':
    st.write(df.columns)
elif sh=='Select':
    " "
elif sh=='Statistical Description':
    st.write(df.describe())

st.header('Data Visualisation')
viz= st.radio('Feature Analysis',('Cut','Color','Clarity','Carat'))
if viz=='Cut':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    sns.displot(data=df, x='cut')
    st.pyplot()
elif viz=='Color':
    sns.displot(data=df, x='color')
    st.pyplot()
elif viz=='Clarity':
    sns.displot(data=df, x='clarity')
    st.pyplot()
elif viz=='Carat':
    st.line_chart(data=df, x='carat', y='price')

page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1599707367072-cd6ada2bc375?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8&w=1000&q=80");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)