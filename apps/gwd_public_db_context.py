#!/usr/bin/env python
# coding: utf-8

# In[11]:


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly_express as px
import plotly.graph_objects as go

# Define a custom color mapping dictionary
unique_colors = ['rgb(164,164,213)','rgb(249,167,41)', 'rgb(145,220,234)', 'rgb(249,210,60)','rgb(95,187,104)',
'rgb(187,201,229)','rgb(100,205,204)','rgb(253,111,48)','rgb(235,30,44)','rgb(252,113,158)','rgb(206,105,190)',
'rgb(120,115,192)','rgb(213,187,33)','rgb(87,163,55)','rgb(27,163,198)','rgb(255,190,209)','rgb(128,116,168)',
'rgb(196,100,135)','rgb(158,61,34)']

def app():
    
    
    ## pull in dataset11allmonth if needed

    homedir = os.path.expanduser("~")
    basedir = os.path.join(homedir,'Dropbox (MFO)','MFO_Partners','M Project','Data Management')
    
    
    st.title('Information Hub')
    st.markdown("""
    Welcome to the GWD Dashboard! <br />
    To access the specific dashboard you've paid for, please click on the corresponding option in the sidebar and enter the provided password.<br />
    If you need more information about a specific variable, click on the "Data Dictionary" below. If a variable you're interested in is missing, feel free to submit a request for its addition.<br />
    Feel free to contact us with any inquiries or if you need assistance. <br />
    Happy analyzing!
    """, unsafe_allow_html=True)



        
    
        
    