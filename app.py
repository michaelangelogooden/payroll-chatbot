import openai
import streamlit as st
import pandas as pd

# Replace with your OpenAI API key
openai.api_key = "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"

st.title("Payroll Assistant Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
st.subheader("Chat with the AI")
user_input = st.text_input("Type your message here:")

if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Call OpenAI API for response
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a payroll assistant."}] + st.session_state.messages
        )
        # Get the AI response
        ai_message = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": ai_message})
        st.experimental_rerun()

# Display the conversation
st.write("### Conversation")
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("**You:**", msg["content"])
    else:
        st.write("**AI:**", msg["content"])

st.markdown("---")

# File upload section
st.subheader("Upload Files")
procare_file = st.file_uploader("Upload ProCare File (Excel)", type=["xlsx"])
frankcrum_file = st.file_uploader("Upload FrankCrum Template (Excel)", type=["xlsx"])

if procare_file and frankcrum_file:
    procare_df = pd.read_excel(procare_file)
    frankcrum_df = pd.read_excel(frankcrum_file)

    # Example processing: map hours from ProCare to FrankCrum
    frankcrum_df["REGH"] = procare_df["Total Regular Hours"]
    frankcrum_df["OTX"] = procare_df["Total Overtime Hours"]

    st.write("Files processed. Use the chat above for any payroll queries.")

    st.download_button(
        label="Download Updated Payroll File",
        data=frankcrum_df.to_csv(index=False),
        file_name="Updated_Payroll.csv",
        mime="text/csv"
    )
