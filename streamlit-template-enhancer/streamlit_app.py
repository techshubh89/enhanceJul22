import streamlit as st
from PIL import Image

# ---- Gupshup Branding ----
GUPSHUP_PURPLE = '#754FFE'
GUPSHUP_BG = '#F9F6FF'

# ---- Inject CSS ----
st.markdown(f"""
<style>
.stApp {{ background-color: {GUPSHUP_BG}; }}
header .css-18e3th9 {{ background-color: {GUPSHUP_PURPLE}; }}
.mobile-preview {{
    background: #FFFFFF;
    width: 360px;
    height: 640px;
    border-radius: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    padding: 16px;
    overflow-y: auto;
    margin: auto;
}}
.whatsapp-header {{
    display: flex;
    align-items: center;
    padding: 8px;
    background: #075E54;
    border-radius: 20px 20px 0 0;
}}
.whatsapp-header img {{ width:32px; height:32px; border-radius:16px; margin-right:8px; }}
.whatsapp-header .title {{ color:#FFFFFF; font-weight:bold; }}
.bubble {{
    background:#DCF8C6;
    padding:12px 16px;
    border-radius:16px;
    margin:8px 0;
    width:fit-content;
}}
.bubble.user {{ background:#FFF; margin-left:auto; }}
.quick-replies button {{
    background-color:{GUPSHUP_PURPLE};
    color:#FFF;
    border:none;
    border-radius:20px;
    padding:8px 12px;
    margin:4px;
    cursor:pointer;
}}
</style>
""" , unsafe_allow_html=True)

# ---- App Config ----
st.set_page_config(page_title="WhatsApp Template Enhancer", layout="wide")
st.title("📝 WhatsApp Template Enhancer")

# ---- Layout ----
col1, col2 = st.columns(2)

with col1:
    st.header("1. Upload or Paste Template")
    uploaded = st.file_uploader("Upload .txt template file", type=["txt"])
    if uploaded:
        template = uploaded.read().decode()
    else:
        template = st.text_area("Or paste your template here:", height=200)

    if st.button("Analyze & Enhance"):
        # TODO: integrate LLM logic here
        st.success("Template processed! See preview.")

with col2:
    st.header("2. Mobile Preview")
    st.markdown("""
    <div class="mobile-preview">
      <div class="whatsapp-header">
        <img src="https://static.whatsapp.net/rsrc.php/yl/r/PNjJ3ojTLwL.ico" alt="WA Logo">
        <span class="title">Instamart</span>
      </div>
      <div class="bubble">
        <!-- Enhanced message will render here -->
        Hello {{1}}, welcome to the preview!
      </div>
      <div class="quick-replies">
        <button>Order Now</button>
        <button>Track Order</button>
        <button>Talk to Doctor</button>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Produced by Gupshup Conversation Cloud | Beta Prototype")
