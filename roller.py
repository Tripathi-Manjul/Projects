from random import randint
import streamlit as st 
import altair as alt 
import pandas as pd 

st.title("Dice Roller App")

# Allow the user to choose what size die they’re rolling
side_options = [6, 10, 12, 20]
num_sides = st.sidebar.radio("Number of sides:", side_options) 

# Let the user choose the number of dice to roll, from one to ten
num_dice = st.sidebar.slider("Number of dice:", 1, 10, value=2)

num_rolls_sim = st.sidebar.slider("Number of rolls in simulation",
                          1_000, 100_000, value=1_000, step=1_000)

# Initialize roll variable in session state
if 'roll' not in st.session_state:
    st.session_state.roll = 0

# Adds a button to the dashboard
if st.button("Roll"):
    rolls = [randint(1, num_sides) for _ in range(num_dice)]
    st.session_state.roll = sum(rolls)
    st.write("---")
    st.write(st.session_state.roll)
    st.write(str(rolls))

# Simulation rolls
sim_rolls = []
for _ in range(num_rolls_sim):
    sim_roll = sum([randint(1,num_sides) for _ in range(num_dice)])
    sim_rolls.append(sim_roll)
df_sim = pd.DataFrame({"rolls": sim_rolls})

# Create histogram
chart = alt.Chart(df_sim).mark_bar().encode(
    alt.X("rolls",bin=True),
    y="count()",
)
chart.title = f"Simulation of {num_rolls_sim} rolls"

st.write("---")
st.altair_chart(chart)
