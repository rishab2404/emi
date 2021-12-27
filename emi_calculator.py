import streamlit as st 
def calculate_emi(p, n, r):
  emi =  p * (r/100) * ((1 + r/100)**n) / (((1+r/100)**n) -1)
  st.write("EMI Calculated:",round(emi,3))

def calculate_outstanding_balance(p,n,r,m):
  balance= ((p*(1+(r/100))**n) - (1+(r/100))**m) / (((1+r/100)**n) -1)
  st.write("Balance calculated",round(balance,3))

st.title("EMI and balance Calculator")
principal=st.slider("Loan Amount", 1000,100000)
tenure=st.slider("Tenure in years",1,30)
roi=st.slider("Interest Rate (% P.A.)",1,15)
mp=st.slider("Period for balance",1,tenure*12)
n = tenure * 12
r = roi / 12

if st.button("Calculate emi"):
	calculate_emi(principal,n, r)
 
if st.button("Calculate Outstanding Loan Balance"):
	calculate_outstanding_balance(principal,n,r,mp)