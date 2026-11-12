import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from dateline import date

st.title("pertemuan10: Interaksi Streamlit dan Yahoo Finance")

kamus_ticker = [
    "GOOGL": 'Google',
    'AAPL': 'Apple Inc',
    'SBUX': 'Starbucks',
    'MCD': "McDonald's Corp",
    'META': 'Meta Platforms Inc',
    'TLKM.JK': 'Telkom Indonesia (Persero) Tbk PT',
    'BBNI.JK': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted(kamus_ticker.keys())
)