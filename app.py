import streamlit as st
from textblob import TextBlob
import time  # For a subtle loading effect

# --- Custom CSS for styling ---
st.markdown(
    """
    <style>
    /* Style for sidebar header */
    .sidebar .sidebar-content h4 {
        color: #ff6f61 !important; /* Example: Salmon color */
        font-weight: bold;
    }

    .stTextArea textarea {
        background-color: #f4f8ff; /* Light blue background for text area */
        border: 1px solid #d4d4d4;
        border-radius: 5px;
        color: #333; /* Default text color inside textarea */
        caret-color: black; /* Changed cursor color to black */
    }

    /* Style for the placeholder text (Enter hint) */
    .stTextArea textarea::placeholder {
        color: black !important; /* Changed placeholder text color to black */
        opacity: 0.7; /* Optional: Adjust opacity if needed, e.g., slightly faded black */
    }


    .stButton > button {
        background-color: #4CAF50; /* Green analyze button */
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .sentiment-positive { color: green; font-weight: bold; }
    .sentiment-negative { color: red; font-weight: bold; }
    .sentiment-neutral { color: gray; font-weight: bold; }
    .result-box {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .polarity-score { font-size: 0.9em; color: #777; margin-top: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

def analyze_sentiment(text):
    """Analyzes sentiment using TextBlob."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity

st.title("Sentiment Analyzer")
st.write("Uncover the sentiment behind your text! Enter any text below, and let's analyze its emotional tone.")

text_input = st.text_area("Enter your text and press ctrl + enter :", height=170, placeholder="Type your text here") # Changed placeholder to "Enter"

if text_input:
    with st.spinner("Analyzing sentiment..."): # Loading spinner
        time.sleep(0.5) # Simulate analysis time (remove or adjust as needed)
        sentiment, polarity_score = analyze_sentiment(text_input)

    st.markdown("<div class='result-box'>", unsafe_allow_html=True) # Start of result box
    st.subheader("Analysis Result:", divider='blue') # Subheader with divider

    col1, col2 = st.columns([1, 3])  # Two columns for layout

    with col1:
        sentiment_class = f"sentiment-{sentiment.lower()}" # CSS class for sentiment color
        st.markdown(f"<p class='{sentiment_class}' style='font-size: 1.5em;'>{sentiment}</p>", unsafe_allow_html=True) # Styled sentiment label

    with col2:
        progress_value = max(0, min(1, (polarity_score + 1) / 2)) # Normalized polarity
        sentiment_color = "green" if sentiment == "Positive" else ("red" if sentiment == "Negative" else "blue") # Color based on sentiment
        st.progress(progress_value, text=f"Sentiment Intensity: {sentiment_color.capitalize()}") # Colored progress bar with label
        st.markdown(f"<p class='polarity-score'>Polarity Score: {polarity_score:.2f} (Ranges from -1 to 1, where higher values indicate more positive sentiment)</p>", unsafe_allow_html=True) # Explanation of polarity

    st.markdown("</div>", unsafe_allow_html=True) # End of result box
    st.write("---")  # Separator line

st.sidebar.header("About This App") # More descriptive sidebar header
st.sidebar.info(
    "This interactive Sentiment Analyzer uses the power of Natural Language Processing (NLP) with TextBlob to determine the sentiment of any text you provide.\n\n"
    "Simply type or paste your text in the input area, and the app will instantly classify it as Positive, Negative, or Neutral, along with a sentiment intensity score.\n\n"
    "**Key Features:**\n"
    "- Real-time Sentiment Analysis\n"
    "- Visual Sentiment Intensity Indicator\n"
    "- Clear Sentiment Classification\n"
    "- User-friendly Interface\n\n"
    "Created for demonstration and educational purposes."
)