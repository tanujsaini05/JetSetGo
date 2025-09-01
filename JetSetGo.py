import streamlit as st
from crewai import Crew,Process
from Agents import booking_agent,travel_planner_ag
from task import booking_task,travel_planner_task
#from 




st.title("🌍 AI-Powered Trip Planner")

st.markdown("""
    **Plan your trip with AI!**
 Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
 Best places to visit 🎡   Accommodation & budget planning 💰
 Local food recommendations 🍕   Transportation & visa details 🚆
""")
from_city = st.text_input("🏡 From City","Chandigarh")
destination = st.text_input("✈️ Destination City","Delhi")
budget = st.number_input("💸 Budget")
people = st.number_input("👨🏾‍🤝‍👨🏾 Number of People ")
stay = st.number_input("👔 Stay (in Days)")

date_from = st.date_input("📅 Departure Date")

if st.button("🚀 Generate Travel Plan"):
    if not from_city or not destination or not budget or not people or not stay or not date_from:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    else:
        st.write("⏳ AI is preparing your personalized travel itinerary... Please wait.")

        crew_ = Crew(
            agents=[booking_agent,travel_planner_ag],
            tasks=[booking_task,travel_planner_task],
            process=Process.sequential,
            full_output=True,
            share_crew=False,
            verbose=True
        )

        result = crew_.kickoff(inputs={
            "start_trip": from_city,
            "destination": destination,
            "Budget": budget,
            "people": people,
            "day": stay,
            "start_date": str(date_from)
        })

        st.subheader("✅ Your AI-Powered Travel Plan")
        st.markdown(result)


        # Ensure result is a string
        travel_plan_text = str(result)

        st.download_button(
            label="📥 Download Travel Plan",
            data=travel_plan_text,  # ✅ Now passing a valid string
            file_name=f"Travel_Plan_{destination}.txt",
            mime="text/plain"
        )

                

