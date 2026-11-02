import streamlit as st
#page configurationUSB_Analiz

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


import subprocess

result = subprocess.run(
    ["lsblk", "-J"],
    capture_output=True,
    text=True
)

print(result.stdout)



print("STDOUT:", repr(result.stdout))
print("STDERR:", repr(result.stderr))
print("RETURN CODE:", result.returncode)

import json

data = json.loads(result.stdout)
devices = data["blockdevices"]
usb_count = 0
total_storage = 0

for device in devices:
    if device["rm"]:
        usb_count+=1
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

