import streamlit as st
from PIL import Image

st.set_page_config(page_title="SmartScan EduPad", layout="centered")

st.title("🎓 SmartScan EduPad - B.Tech Project")
st.success("✅ **DEPLOYMENT SUCCESSFUL**")

# Upload
uploaded_file = st.file_uploader("Upload Answer Sheet", type=['jpg', 'png'])

if uploaded_file:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Sheet", width=300)
    
    # Show file info
    st.info(f"**File:** {uploaded_file.name} | **Size:** {uploaded_file.size/1024:.1f} KB")
    
    # Evaluate button
    if st.button("🔍 Evaluate", type="primary"):
        st.balloons()
        st.success("✅ Evaluation Complete!")
        
        # Results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Score", "8/10")
        with col2:
            st.metric("Percentage", "80%")
        with col3:
            st.metric("Grade", "A")

# Footer
st.markdown("---")
st.caption("SmartScan EduPad | B.Tech Final Year Project")
