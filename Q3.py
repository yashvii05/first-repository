import streamlit as st

def main():
    st.title("Basic Travel Itinerary Generator")
    st.write("Welcome! Enter your travel details below.")
    destination = st.text_input("Enter your destination:")
    duration = st.slider("How many days will your trip last?") 
    if st.button("Generate Itinerary"):
        if destination:
            st.write(f"Your itinerary for a {duration}-day trip to {destination}:")
            st.write("### Places to Visit:")
            st.write("- Visit the main attractions.")
            st.write("- Explore the local culture and landmarks.")

            st.write("### Food Recommendations:")
            st.write("- Try local delicacies and popular street foods.")
            st.write("- Visit popular restaurants or food markets.")

            st.write("### Activities to Enjoy:")
            st.write("- Take a sightseeing tour.")
            st.write("- Relax at the park or beach.")

        else:
            st.error("Please enter a valid destination.")
if __name__ == "__main__":
    main()
