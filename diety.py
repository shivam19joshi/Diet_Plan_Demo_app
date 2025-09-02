import streamlit as st

# App config
st.set_page_config(page_title="🥗 Personalized Diet Planner", layout="centered")

# Title
st.title("🥗 Personalized Diet Planner")

st.write("Enter your details to get a customized diet suggestion!")

# User Inputs
name = st.text_input("👤 Enter your Name")
age = st.slider("🎂 Select Age", 10, 80, 25)
height = st.slider("📏 Height (in cm)", 100, 220, 170)
weight = st.slider("⚖️ Weight (in kg)", 30, 150, 65)

# Calculate BMI
if height > 0:
    bmi = weight / ((height / 100) ** 2)
else:
    bmi = 0

st.write(f"**Your BMI:** {bmi:.2f}")

# Diet Suggestions
if bmi < 18.5:
    plan = """
    🍽️ **Diet Plan for Underweight**  
    - Eat calorie-dense foods like nuts, avocados, peanut butter  
    - Include protein shakes, milk, and yogurt  
    - Eat 5–6 smaller meals a day  
    - Add strength training exercises  
    """
elif 18.5 <= bmi < 24.9:
    plan = """
    🍽️ **Diet Plan for Normal Weight**  
    - Balanced diet with whole grains, vegetables, and lean proteins  
    - Maintain portion control  
    - Stay hydrated (8–10 glasses of water)  
    - Regular exercise to stay fit  
    """
elif 25 <= bmi < 29.9:
    plan = """
    🍽️ **Diet Plan for Overweight**  
    - Reduce refined carbs and sugar  
    - Focus on high-fiber foods and lean proteins  
    - Practice portion control  
    - Add cardio + strength workouts  
    """
else:
    plan = """
    🍽️ **Diet Plan for Obese**  
    - Strictly avoid junk and fried food  
    - Eat more vegetables, fruits, and whole grains  
    - High protein, low-carb diet  
    - Daily walking and exercise routine  
    - Consult a nutritionist for a detailed plan  
    """

# Display Results
if name:
    st.success(f"Hello {name}, here’s your recommended diet plan 👇")
    st.markdown(plan)
