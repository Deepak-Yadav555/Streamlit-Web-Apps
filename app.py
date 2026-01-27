import streamlit as st
import yfinance as yf
import pandas as pd

# 1. Title
st.title("📈 Stock Price & Data Table App")

# 2. Input
ticker_symbol = st.text_input("Stock Ticker (e.g. RELIANCE.NS, TATAMOTORS.NS, AAPL)", "RELIANCE.NS")

# 3. Button (Optional: Taaki baar baar refresh na ho)
if st.button("Get Data"):
    
    try:
        # Data download
        ticker_data = yf.Ticker(ticker_symbol)
        ticker_df = ticker_data.history(period='1y')

        if not ticker_df.empty:
            
            # --- PART 1: CHARTS ---
            st.header("1. Charts")
            st.line_chart(ticker_df['Close'])

            # --- PART 2: INTERACTIVE DATAFRAME ---
            st.header("2. Pura Data (Interactive DataFrame)")
            st.write("Is table ko aap scroll kar sakte hain aur maximize bhi kar sakte hain.")
            
            # Syntax: st.dataframe(data, width, height)
            st.dataframe(ticker_df) 

            # --- PART 3: STATIC TABLE (Summary) ---
            st.header("3. Aaj ki Summary (Static Table)")
            st.write("Yeh `st.table()` function hai jo data ko fix karke dikhata hai.")

            # Hum aaj ka latest data nikal kar ek chhota table banayenge
            last_day = ticker_df.iloc[-1] # Aakhiri row uthayi
            
            # Ek simple dictionary banayi display ke liye
            summary_data = {
                "Metric": ["Aaj ki Date", "Open Price", "Close Price", "High", "Low"],
                "Value": [
                    str(last_day.name.date()), 
                    round(last_day['Open'], 2),
                    round(last_day['Close'], 2),
                    round(last_day['High'], 2),
                    round(last_day['Low'], 2)
                ]
            }
            
            # Dictionary ko DataFrame mein convert kiya
            summary_df = pd.DataFrame(summary_data)

            # Syntax: st.table(data)
            st.table(summary_df)

        else:
            st.error("Data nahi mila. Ticker check karein.")

    except Exception as e:
        st.error(f"Error: {e}")