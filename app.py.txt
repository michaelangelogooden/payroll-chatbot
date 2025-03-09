import openai
import streamlit as st
import pandas as pd

# Replace with your OpenAI API key
openai.api_key = "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"

st.title("Payroll Processing Chatbot")

# File upload widgets
procare_file = st.file_uploader("Upload ProCare File (Excel)", type=["xlsx"])
frankcrum_file = st.file_uploader("Upload FrankCrum Template (Excel)", type=["xlsx"])

if procare_file and frankcrum_file:
    # Read Excel files into pandas DataFrames
    procare_df = pd.read_excel(procare_file)
    frankcrum_df = pd.read_excel(frankcrum_file)

    # Example processing: Map ProCare hours to FrankCrum template
    frankcrum_df["REGH"] = procare_df["Total Regular Hours"]
    frankcrum_df["OTX"] = procare_df["Total Overtime Hours"]

    # Use OpenAI to generate a payroll summary
    payroll_summary = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a payroll assistant."},
            {"role": "user", "content": f"Summarize payroll issues:\n{procare_df.to_string()}"}
        ]
    )

    st.write("Payroll Issues:")
    st.write(payroll_summary["choices"][0]["message"]["content"])

    # Provide a download button for the updated payroll file
    st.download_button(
        label="Download Updated Payroll File",
        data=frankcrum_df.to_csv(index=False),
        file_name="Updated_Payroll.csv",
        mime="text/csv"
    )
