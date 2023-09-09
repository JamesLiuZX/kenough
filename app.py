import streamlit as st
import os

def main():
    st.title("Video File Uploader")
    
    options = ["Option1", "Option2", "Option3"]
    selected_option = st.selectbox("Select an option", options)
    st.write("You selected:", selected_option)
    
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])
    if uploaded_file is not None:
        # Process the uploaded file
        st.video(uploaded_file)
        
        # Define the directory where you want to save the uploaded files
        save_directory = "/Users/rachpradhan/Desktop/condensation/"
        
        # Ensure the directory exists
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        
        # Save the uploaded file to the specified directory
        file_path = os.path.join(save_directory, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File saved to: {file_path}")

    # Add a textbox
    text = st.text_input("Enter your text here")
    st.info(text)

if __name__ == "__main__":
    main()
