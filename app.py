import streamlit as st

# Streamlit app
st.title('Personal Goal App')

name = st.text_input('Enter your name:')
age = st.number_input('Enter your age:', min_value=0)
goal = st.text_input('Enter your goal for the next week:')

if st.button('Submit'):
    if age < 79:
        response = f"Hi {name}, it's lovely to meet you. You're a little younger than my mum. I hope you have great success this week with your goal to {goal}!"
    elif age > 79:
        response = f"Hi {name}, it's lovely to meet you. You're a little older than my mum. I hope you have great success this week with your goal to {goal}!"
    else:
        response = f"Hi {name}, it's lovely to meet you. You're the same age as my mum! I hope you have great success this week with your goal to {goal}!"
    st.write(response)
