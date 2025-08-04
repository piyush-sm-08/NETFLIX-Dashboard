# import streamlit as slt
# import pandas as pd
# import plotly.express as px

# # LOAD DATA

# @slt.cache_data
# def load_data():
#     return pd.read_csv("data/netflix_titles.csv")
# data=load_data()

# # DASHBOARD
# slt.title("Netflix Content Analysis Dashboard")

# # Sidebar filters
# slt.sidebar.header("Filters")
# type_filter = slt.sidebar.selectbox("Content Type" , ["All"] + list(data["type"].unique()))
# year_filter = slt.sidebar.slider("Release Year",\
#                                 min_value = int(data["release_year"].min()),\
#                                 max_value = int(data["release_year"].max()),\ 
#                                 value = (int(data["release_year"].min(),int(data["release_year"].max())))
                            

import plotly as py
print(py.__version__)