import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

df = pd.read_csv('bank.csv')
st.set_page_config(page_title="Real Time Scene Dashboard", page_icon="✅", layout="wide")

#Dasboard Title
st.title("Real Time Data analystics")

# filtre sur JOB
job_filter = st.selectbox("Select a Job", pd.unique(df["job"].unique()))
df=df[df["job"] == job_filter]


# Creation d'indicateurs
avg_age = np.mean(df["age"])
count_married = int(df[df["marital"] == "married"]["marital"].count())
balance = np.mean(df["balance"])

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age))
kpi2.metric(label="Married Count", value=count_married, delta=round(count_married))
kpi3.metric(label="Average Balance", value=f"{balance:.2f}", delta=-round(balance/count_married)*100)

# Graphique
col1, col2 = st.columns(2)
with col1:
    st.markdown("### First Chart")
    fig1 = plt.figure()
    sns.barplot(data=df, y="age", x="marital", palette="muted")
    st.pyplot(fig1)
with col2:
    st.markdown("### Second Chart")
    fig2 = plt.figure()
    sns.histplot(data=df, x='age')
    st.pyplot(fig2)

st.markdown("### Detailed Data View")
st.dataframe(df)
time.sleep(1)
