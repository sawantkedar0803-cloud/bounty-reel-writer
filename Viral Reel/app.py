import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Viral Reel Generator", page_icon="🎬")
st.title("🎬 Viral Reel Script Writer")
st.markdown("Convert any boring topic into a high-retention script.")


# Logic
def generate_script(topic):
    hooks = [f"Stop scrolling! {topic} is actually a game changer.", f"The secret to {topic} finally revealed.",
             f"Why you're failing at {topic}... and how to fix it."]
    ctas = [f"Follow for more {topic} hacks!", f"Drop a 🚀 if you love {topic}!", f"Link in bio for my {topic} course."]

    return {
        "hook": random.choice(hooks),
        "value": f"First, focus on the core of {topic}. Next, apply the 80/20 rule to maximize results. Finally, stay consistent.",
        "cta": random.choice(ctas)
    }


# UI
topic_input = st.text_input("Enter your boring topic:", placeholder="e.g. Tax Accounting")

if st.button("Generate Script"):
    if topic_input:
        res = generate_script(topic_input)
        st.success("Script Generated!")
        st.subheader("Your Script:")
        st.write(f"**Hook:** {res['hook']}")
        st.write(f"**Body:** {res['value']}")
        st.write(f"**CTA:** {res['cta']}")
    else:
        st.error("Enter a topic first!")