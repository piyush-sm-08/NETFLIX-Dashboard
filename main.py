# pandas==2.0.3
# numpy==1.24.3
# matplotlib==3.7.1
# seaborn==0.12.2
# plotly==5.14.1
# streamlit==1.23.1
# python-dotenv==1.0.0

import pandas as pd
import numpy
import matplotlib
import seaborn
import plotly
import streamlit
import dotenv

print("pandas:", pd.__version__)
print("numpy:", numpy.__version__)
print("matplotlib:", matplotlib.__version__)
print("seaborn:", seaborn.__version__)
print("plotly:", plotly.__version__)
print("streamlit:", streamlit.__version__)

# dotenv version workaround
try:
    import importlib.metadata
    print("python-dotenv:", importlib.metadata.version("python-dotenv"))
except ImportError:
    # For older Python versions
    import pkg_resources
    print("python-dotenv:", pkg_resources.get_distribution("python-dotenv").version)
