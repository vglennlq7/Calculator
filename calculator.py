import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# ---- Title 
st.title("🧮 Simple Calculator")
st.caption("Welcome to the most *simple calculator on Earth* 😄")

# ---- Inputs
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input("Enter the first number:", value=0.0, step=1.0, format="%.6f")
with col2:
    number2 = st.number_input("Enter the second number:", value=0.0, step=1.0, format="%.6f")

operation = st.radio("Choose the operation:", ['+', '-', '*', '/'], horizontal=True)

# ---- Calculate
result = None
error_msg = None
if st.button("Calculate"):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        if number2 == 0:
            error_msg = "⚠️ Error: cannot divide by zero."
        else:
            result = number1 / number2

    # ---- Output
    if error_msg:
        st.error(error_msg)
    else:
        st.success(f"**The result is:** {result}")
        st.caption("That is all 🔥😄")

# ---- Optional: small footer
st.write("---")
st.markdown(
    "<div style='text-align:center; opacity:.7;'>Built with Streamlit</div>",
    unsafe_allow_html=True
)




