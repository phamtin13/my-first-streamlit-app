import streamlit as st
st.title("GIẢI PHƯƠNG TRÌNH BẬC NHẤT")
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a ==0:
    st.success('Phương trình vô nghiệm')
  else:
    result = (-b)/(2*a)
    st.success('Phương trình có 1 nghiệm',result)
