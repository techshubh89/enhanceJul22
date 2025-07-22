import streamlit as st

# ---- Gupshup Branding ----
GUPSHUP_PURPLE = '#754FFE'
GUPSHUP_BG = '#F9F6FF'

# ---- Core Logic Functions ----
def categorize_template(template: str) -> str:
    marketing_keywords = ["discount", "offer", "sale", "exclusive", "promo", "deal"]
    return "Marketing" if any(word.lower() in template.lower() for word in marketing_keywords) else "Utility"

def generate_utility_version(template: str) -> str:
    # Simplify message to a functional update (stub for LLM)
    return (
        f"Hello {{1}}, your request has been processed: {template.strip()}"
    )

def generate_nudges(template: str, hours: int) -> list:
    if hours == 24:
        return [
            (f"Hi {{1}}, your request is on the way!", 
             "Keeps user informed and reduces support queries."),
            (f"Need help? Reply HELP anytime.", 
             "Offers proactive support to increase satisfaction.")
        ]
    else:
        return [
            (f"Hope everything went well. Feedback? Reply FEEDBACK.", 
             "Collects user satisfaction data."),
            (f"Need a follow-up? Reply REFOLLOW.", 
             "Drives further engagement and support.")
        ]

def generate_engaging_marketing_version(template: str) -> tuple:
    enhanced = (
        "🚀 Ready for more? Unlock exclusive benefits today!"
    )
    quick_replies = ["Learn More", "Get Started", "Contact Us"]
    return enhanced, quick_replies

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

# ---- App Configuration ----
st.set_page_config(page_title="WhatsApp Template Enhancer", layout="wide")

# ---- App Title ----
st.title("✏️ WhatsApp Template Enhancer")

# ---- Input Section (only paste) ----
st.subheader("1. Paste your WhatsApp template below:")
template_text = st.text_area(
    "Paste the template content here:",
    height=200
)

# ---- Analyze Button ----
if st.button("Analyze & Enhance") and template_text.strip():
    # Generate outputs
    classification = categorize_template(template_text)
    utility = generate_utility_version(template_text)
    nudges_24h = generate_nudges(template_text, 24)
    nudges_48h = generate_nudges(template_text, 72)
    marketing, quick_replies = generate_engaging_marketing_version(template_text)

    # Display results
    st.subheader("🗂 Classification")
    st.write(f"**{classification} Template**")

    st.subheader("⚙️ Utility Version")
    st.code(utility)

    st.subheader("⏱️ Nudges within 24 Hours")
    for nudge, reason in nudges_24h:
        st.markdown(f"- **{nudge}** — {reason}")

    st.subheader("⏳ Nudges within 48–72 Hours")
    for nudge, reason in nudges_48h:
        st.markdown(f"- **{nudge}** — {reason}")

    st.subheader("🎨 Engaging Marketing Version")
    st.code(marketing)
    st.markdown("**Quick Replies:**")
    cols = st.columns(len(quick_replies))
    for col, label in zip(cols, quick_replies):
        col.button(label)

    # Mobile Preview
    st.subheader("📱 Mobile Preview")
    preview_html = f"""
    <div class=\"mobile-preview\">  
      <div class=\"whatsapp-header\">  
        <img src=\"https://static.whatsapp.net/rsrc.php/yl/r/PNjJ3ojTLwL.ico\" alt=\"WA Logo\">  
        <span class=\"title\">WhatsApp Preview</span>  
      </div>  
      <div class=\"bubble\">  
        {marketing}  
      </div>  
      <div class=\"quick-replies\">  
    """
    for qr in quick_replies:
        preview_html += f"<button>{qr}</button>"
    preview_html += "</div></div>"
    st.markdown(preview_html, unsafe_allow_html=True)
else:
    st.info("Enter a template and click **Analyze & Enhance** to see results.")

st.markdown("---")
st.caption("Produced by Gupshup Conversation Cloud | Beta Prototype")
