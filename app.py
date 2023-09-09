import streamlit as st

def main():
    st.title("Video File Uploader")
    
    options = ["Option1", "Option2", "Option3"]
    selected_option = st.selectbox("Select an option", options)
    st.write("You selected:", selected_option)
    
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])
    if uploaded_file is not None:
        # Process the uploaded file
        st.video(uploaded_file)

    # Add a textbox
    text = st.text_input("Enter your text here")
    st.info(text)

if __name__ == "__main__":
    main()
