{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww28900\viewh15820\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import openai
\f1\fs24 \

\f0\fs29\fsmilli14667 import streamlit as st
\f1\fs24 \

\f0\fs29\fsmilli14667 import pandas as pd
\f1\fs24 \
\

\f0\fs29\fsmilli14667 # Replace with your OpenAI API key
\f1\fs24 \

\f0\fs29\fsmilli14667 openai.api_key = "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"
\f1\fs24 \
\

\f0\fs29\fsmilli14667 st.title("Payroll Processing Chatbot")
\f1\fs24 \
\

\f0\fs29\fsmilli14667 # File upload widgets
\f1\fs24 \

\f0\fs29\fsmilli14667 procare_file = st.file_uploader("Upload ProCare File (Excel)", type=["xlsx"])
\f1\fs24 \

\f0\fs29\fsmilli14667 frankcrum_file = st.file_uploader("Upload FrankCrum Template (Excel)", type=["xlsx"])
\f1\fs24 \
\

\f0\fs29\fsmilli14667 if procare_file and frankcrum_file:
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0# Read Excel files into pandas DataFrames
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0procare_df = pd.read_excel(procare_file)
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0frankcrum_df = pd.read_excel(frankcrum_file)
\f1\fs24 \
\

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0# Example processing: Map ProCare hours to FrankCrum template
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0frankcrum_df["REGH"] = procare_df["Total Regular Hours"]
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0frankcrum_df["OTX"] = procare_df["Total Overtime Hours"]
\f1\fs24 \
\

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0# Use OpenAI to generate a payroll summary
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0payroll_summary = openai.ChatCompletion.create(
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0model="gpt-4-turbo",
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0messages=[
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\{"role": "system", "content": "You are a payroll assistant."\},
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0\{"role": "user", "content": f"Summarize payroll issues:\\n\{procare_df.to_string()\}"\}
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0]
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0)
\f1\fs24 \
\

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0st.write("Payroll Issues:")
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0st.write(payroll_summary["choices"][0]["message"]["content"])
\f1\fs24 \
\

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0# Provide a download button for the updated payroll file
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0st.download_button(
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0label="Download Updated Payroll File",
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0data=frankcrum_df.to_csv(index=False),
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0file_name="Updated_Payroll.csv",
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0\'a0\'a0\'a0\'a0mime="text/csv"
\f1\fs24 \

\f0\fs29\fsmilli14667 \'a0\'a0\'a0\'a0)
\f1\fs24 \
}