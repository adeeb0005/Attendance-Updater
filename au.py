import streamlit as st
import pandas as pd
import numpy as np
import os
from st_btn_select import st_btn_select


st.title("Attendance Update Process")
fileB = st.sidebar.file_uploader('Upload Main Attendance File', type = ['csv', 'xlsx'])
if fileB:
    dfB = pd.read_excel(fileB)
    dfB=dfB.dropna(axis=1,how='all')
    fileS = st.sidebar.file_uploader('Upload Regular Attendance File', type = ['csv', 'xlsx'])
    if fileS:
        dfS = pd.read_excel(fileS)
        dfLI = list(dfS.columns)
        with st.form(key='columns_in_form'):
            Date = st.text_input('Date:')
            sub = st.text_input('Course Code:')
            jjj = st.sidebar.selectbox('Make a Selection', dfLI)
            submitted = st.form_submit_button('Submit')
            if submitted:
                p = dfS[jjj]
                p = p.unique()
                mis = []
                for i in p:
                    k = i.strip()
                    if len(k) < 8:
                        mis.append(k)
                        zz = (np.where(p == i))
                        p = np.delete(p, zz[0][0])
                    elif len(k) != len(i):
                        zz = (np.where(p == i))
                        p[zz[0][0]] = k
                for i in p:
                    ss = ""
                    if (i[2] != 'C' or i[3] != 'S' or i[4] != 'E') and len(i) == 8:
                        ss += i[0]
                        ss += i[1]
                        ss += "CSE"
                        ss += i[5]
                        ss += i[6]
                        ss += i[7]
                        zz = (np.where(p == i))
                        p[zz[0][0]] = ss
                p = np.sort(p)
                p = np.unique(p)
                if Date:
                    li = []
                    for j in dfB["Roll No"]:
                        ch = True
                        for i in p:
                            if i == j:
                                li.append("Present")
                                ch = False
                        if(ch == True): li.append("")
                    dfB[Date] = li
                    pos = os.getcwd() +"\\" + sub + "\\" + fileB.name
                    dfB.to_excel(pos, index = False)
                    st.write("Done")
                    if len(mis) != 0 :
                        st.write("Unacceptable inputs: ")
                        st.write(str(mis))

