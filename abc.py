import os
import streamlit as st
from pathlib import Path

def organize_files_by_extension(directory):
    all_items = os.listdir(directory)
    for item in all_items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            continue
        file_extension = os.path.splitext(item)[1][1:]
        if not file_extension:
            file_extension = 'no_extension'
        new_dir = os.path.join(directory, file_extension)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        os.rename(item_path, os.path.join(new_dir, item))

def main():
    st.title("File Organizer")
    st.write("Organize files in a directory based on their file extensions.")

    directory = st.text_input("Enter the directory path to organize:")
    
    if st.button("Organize Directory"):
        if directory and os.path.isdir(directory):
            organize_files_by_extension(directory)
            st.success(f"Files in '{directory}' have been organized by extension.")
        else:
            st.warning("Please enter a valid directory path.")

if __name__ == "__main__":
    main()
