import streamlit as st
import os
from massive import RESTClient
from dotenv import load_dotenv

load_dotenv()

MASSIVE_API_KEY = os.getenv('MASSIVE_API_KEY')

client = RESTClient(api_key=MASSIVE_API_KEY)

def request():
    ticker = input("Enter ticker: ")
    quote = client.get_previous_close_agg(
        ticker=ticker,
        adjusted=True
    )
    print(quote)

request()