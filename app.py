"""
p - > raheb

page create..

"""



import streamlit as st
#page configurationUSB_Analiz
import subprocess
import os
import random
import json

from collections import Counter

st.set_page_config(page_title= "USB_Analyz", page_icon = "💾", layout = "wide")


st.title("USB Analyz")

st.markdown("---")

#sidebar
st.sidebar.title("Navigation")
st.sidebar.write("USB Analyzer Dashboard")

#Main Section
st.header("USB Divace Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Connected USB", "0")

with col2:
    st.metric("Total Files", "0")

with col3:
    st.metric("Total Storage", "0 MB")



st.markdown("----")

st.subheader("Divace scanner")

if st.button("scan USB Devices"):
    st.info("USB scanning module is coming soon!")


"""

subprocess

"""



result = subprocess.run(
    ["lsblk", "-J"],
    capture_output=True,
    text=True
)

print(result.stdout)



print("STDOUT:", repr(result.stdout))
print("STDERR:", repr(result.stderr))
print("RETURN CODE:", result.returncode)


data = json.loads(result.stdout)
devices = data["blockdevices"]
usb_count = 0
total_storage = 0

mount_path = None

for device in devices:
    if device["rm"]:
        usb_count+=1
        if device["mountpoints"]:
            mount_path = device["mountpoints"][0]
        usb_info = {
            "name": device["name"],
            "size": device["size"],
            "mountpoints": device["mountpoints"]
        }
        size_text = device["size"]
        size_number = float(size_text.replace("G", ""))
        total_storage += size_number    

        st.json(usb_info)



st.metric("Connected USB", usb_count)
#st.write(size_number)
st.metric("Total Storage", f"{total_storage:.2f} GB")


total_files = 0
file_extensions = Counter()


if mount_path:
    for root, dirs, files in os.walk(mount_path):
        
        for file in files:
            total_files += 1
        
        extension = os.path.splitext(file)[1].lower()
        file_extensions[extension] += 1

        st.write(mount_path)

        st.metric("Total Files", total_files)
        
        st.subheader("File Format Analysis")
        st.write(file_extensions)

else:

    st.write("No USB device connected !")

    st.metric("Total files", 0)

    st.subheader("File Format Analysis")
    st.info("No File to Analyze !")
    
















st.write("creator app by 'raheb' :) ")
