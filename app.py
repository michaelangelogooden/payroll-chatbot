import openai
import streamlit as st
import pandas as pd

# Replace with your OpenAI API key
openai.api_key = "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"

# Set page configuration for a nicer layout
st.set_page_config(page_title="Payroll Assistant Chatbot", layout="wide")

# Sidebar for file uploads
st.sidebar.header("Payroll Files")
procare_file = st.sidebar.file_uploader("Upload ProCare File (Excel)", type=["xlsx"])
frankcrum_file = st.sidebar.file_uploader("Upload FrankCrum Template (Excel)", type=["xlsx"])

# Main title
st.title("Payroll Assistant Chatbot")

# Container for chat interface
chat_container = st.container()
with chat_container:
    st.subheader("Chat with the AI")
    
    # Initialize session state for conversation if not already done
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Input area for chat message
    user_input = st.text_input("Enter your message:")
    
    # When the user sends a message, process it
    if st.button("Send", key="send_button") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Call the OpenAI API with conversation history
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a payroll assistant."}] + st.session_state.messages
        )
        ai_response = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.experimental_rerun()
    
    # Display conversation in a neat format
    st.markdown("### Conversation")
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**AI:** {message['content']}")
            
# Container for file processing
file_container = st.container()
with file_container:
    st.markdown("---")
    st.subheader("Processed Payroll Files")
    
    # Process files if both are uploaded
    if procare_file and frankcrum_file:
        try:
            procare_df = pd.read_excel(procare_file)
            frankcrum_df = pd.read_excel(frankcrum_file)
            
            # Example: Map ProCare hours to FrankCrum template
            if "Total Regular Hours" in procare_df.columns and "Total Overtime Hours" in procare_df.columns:
                frankcrum_df["REGH"] = procare_df["Total Regular Hours"]
                frankcrum_df["OTX"] = procare_df["Total Overtime Hours"]
                st.success("Files processed successfully.")
            else:
                st.error("Required columns are missing in the ProCare file.")
        except Exception as e:
            st.error(f"An error occurred while processing files: {e}")
        
        # Download button for the updated payroll file
        csv_data = frankcrum_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download Updated Payroll File",
            data=csv_data,
            file_name="Updated_Payroll.csv",
            mime="text/csv"
        )
    else:
        st.info("Please upload both payroll files using the sidebar.")
