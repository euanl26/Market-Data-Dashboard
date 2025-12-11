import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime, date, timedelta
from massive import RESTClient
from dotenv import load_dotenv

load_dotenv()

MASSIVE_API_KEY = os.getenv('MASSIVE_API_KEY')
TICKER = "GOOGL"

client = RESTClient(api_key=MASSIVE_API_KEY)

def request_data():
    today = date.today()
    start_date = today - timedelta(weeks=4)
    end_date = today - timedelta(days=1)
    aggs = client.list_aggs(
        TICKER,
        1,
        "day",
        start_date,
        end_date,
        sort='asc',
    )
    data = [{"open": agg.open, "close": agg.close, "high": agg.high, "low": agg.low} for agg in aggs]
    data = json.dumps(data)
    df = pd.read_json(data)
    return(df)

def sma():
    data = request_data()
    close_vals = data['close'].to_list()
    
    total = 0
    for val in close_vals:
        total += val
    
    sma = total / len(close_vals)

    return(sma)

def st_app():
    data = request_data()
    st.write(TICKER)
    st.write("Simple Moving Average: ", sma())
    st.write(data)

st_app()