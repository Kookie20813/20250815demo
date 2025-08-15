import numpy as np
import pandas as pd
import streamlit as st

st.title("Demo Test App")
st.write("This is a simple demo app to test Streamlit functionality.")
st.write("## MDFK")

df1=pd.DataFrame([[1, 2, 3], [4, 5, 6]])
st.write(df1)
st.table(df1)

C1 = st.checkbox("Check me!")
if C1:
    st.write("HAHA!PY TON!")
else:
    st.write("PY MI!")

checks = st.columns(3)
txt =" "
with checks[0]:
    r11=st.checkbox("A")
    if r11:
        txt += "AAAAA"
with checks[1]:
    r12=st.checkbox("B")
    if r12:
        txt += "B群就是B群!!"
with checks[2]:
    r13=st.checkbox("C")
    if r13:
        txt += "C格馬男人"
st.info(txt)

st.write("## 選項啦")
b1= st.radio("飲料", ["coffee", "tea", "ME"])
if b1 == "ME":
    st.info("Come on,BABY!")
else: 
    st.info(b1)

b2= st.radio("飲料", ["coffee", "tea", "ME"], index=1)
if b2 == "ME":
    st.info("Come on,BABY!")
else: 
    st.info(b2)

st.write("## 拉進垃圾車")
num = st.slider("選擇距離:",0.0,20.0,10.0,step=0.5)
st.info(num)

st.write("## 下拉選單")
city = st.sidebar.selectbox("居住地", ["台北", "台中", "高雄"])
if city == "台北":
    st.sidebar.info("A")
elif city == "台中":
    st.sidebar.info("B")
else:
    st.sidebar.info("C")

st.write("## 按鈕")
a=st.number_input("num...")
b=st.number_input("num2...",key='b')
if st.button("相加"):
    st.write("### ", a + b)