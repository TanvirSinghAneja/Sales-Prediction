import streamlit as st
import pickle
import pandas as pd
import sklearn

r=pickle.load(open('rfor.pkl','rb'))
std=pickle.load(open('stdsc.pkl','rb'))

st.title('Sales Forecasting')

def input_feature():
  c1,c2,c3=st.columns([1,1,1])
  with c1:
    tv=st.number_input('Enter Expense on Television')
  with c2:
    rd=st.number_input('Enter Expense on Radio')
  with c3:
    np=st.number_input('Enter Expense on Newspaper')
  inp={'TV':tv,'Radio':rd,'Newspaper':np}
  d=pd.DataFrame([inp])
  d=std.transform(d)
  return d
st.divider()
df=input_feature()
c1,c2=st.columns([1,2])
pred=r.predict(df)
# act=std.inverse_transform([pred])
with c1:
  button=st.button('Predict Sales')
with c2:
  if button is True:
   st.subheader(f'Sales Prediction is = {round(pred,2)}')
