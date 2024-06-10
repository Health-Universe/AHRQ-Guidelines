import streamlit as st
import requests

# App description
st.title("AHRQ Guidelines Search")
st.write("""
### Search AHRQ Guidelines
This app allows you to easily search for guidelines published by the Agency for Healthcare Research and Quality (AHRQ). Simply enter a keyword or topic, and the app will fetch relevant guidelines for you.
""")

# Input field for search query
query = st.text_input("Enter a keyword or topic to search for AHRQ guidelines")

# Function to search AHRQ guidelines
def search_ahrq_guidelines(query):
    url = f"https://api.ahrq.gov/search?query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Perform search when user submits a query
if query:
    st.write(f"Searching for guidelines related to '{query}'...")
    results = search_ahrq_guidelines(query)
    if results:
        st.write(f"Found {len(results['guidelines'])} guidelines:")
        for guideline in results['guidelines']:
            st.write(f"- **{guideline['title']}**: {guideline['summary']}")
            st.write(f"  [Link to full guideline]({guideline['url']})")
    else:
        st.write("No guidelines found for the given query.")

# Error handling
if query and results is None:
    st.write("An error occurred while fetching the guidelines. Please try again later.")
