import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Visualisation de données")
    df = pd.read_csv("festivals.csv", delimiter=";")
    st.write(df.head())