import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import faq

# Set page configuration
st.set_page_config(page_title="Air Quality App", layout="wide")
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.users = {"admin": "manya"}  # Default user for demo


# Function for user authentication
def authenticate(username, password):
    return st.session_state.users.get(username) == password


# Function to handle login/logout
def login():
    st.title("**:violet[WELCOME TO AIR VISUAL]**")
    st.subheader("🔐 Login to Access the Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful! Access granted.")
            st.rerun()
        else:
            st.error("🚫 Incorrect username or password!")


# Function to handle new user registration
def register():
    st.subheader("🆕 Register New Account")
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")

    if st.button("Register"):
        if new_username in st.session_state.users:
            st.error("⚠️ Username already exists! Choose a different one.")
        else:
            st.session_state.users[new_username] = new_password
            st.success("✅ Registration successful! Please log in.")
            st.rerun()


# Login or Register page
if not st.session_state.authenticated:

    st.sidebar.title("🔑 User Access")
    st.markdown("""
            <style>
                [data-testid=stSidebar] {
                    background-color:#9569A6;
                }
            </style>
            """, unsafe_allow_html=True)
    choice = st.sidebar.radio("Select an option:", ["Login", "Register"])

    if choice == "Login":
        login()
    else:
        register()
    st.stop()  # Stop execution until authenticated

page_bg_img = """
<style>
/* Main app background */
[data-testid="stAppViewContainer"] {
    background-image: url('');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    opacity: 2.5;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    #background-image: url('https://images.fineartamerica.com/images-medium-large/yellow-flower-blue-background-matthias-hauser.jpg');
    background-size: cover;
    background-color:#9569A6;
    background-position: center;
    color: white;
}

/* Main container for cards and image */
.main-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 40px;
}

/* Card container layout (side-by-side cards) */
/* Card container layout (side-by-side cards) */
.cards-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-bottom: 60px;
}
.info-card {
    background-color: #1c1e24;
    padding: 20px;
    width: 300px;
    border-radius: 10px;
    border: 1px solid #3e424b;
    color: white;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Smooth transition */
}

.info-card:hover {
    transform: translateY(-10px);  /* Card moves up when hovered */
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.3);  /* Add shadow on hover */
}

.info-card-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
.info-card-description {
    font-size: 16px;
    color: #b5b5b5;
}

/* Image container */
.image-container {
    width: 35%; /* Adjust width for the image on the right */
    text-align: center;
}

.image-container img {
    width: 100%;  /* Make image responsive */
    height: auto;
    border-radius: 10px;
}
</style>
"""

# Apply CSS styles
st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"


# Sidebar navigation
# Sidebar navigation
def navigation():
    pages = ["🏠Home", "📜Use Cases", "❓FAQ","📊Dashboard","🔎Check Status","🙋Queries","🥇Quiz","⭐💬Review", "⬇️Download","📝Conclusion"]
    st.sidebar.title("📌*Main Menu*")
    for page in pages:
        if st.sidebar.button(page,use_container_width=True):
            st.session_state.page = page


# Home page with side-by-side cards and image
def home_page():
    st.title("Welcome to the Air Quality App")
    st.write("""
        This app provides insights into air quality data across regions. 
        Navigate through the pages to explore use cases, dashboards, and query functionalities.
    """)

    # Add the new image directly under the text
    st.image("pollution.jpg", use_container_width=True)

    # Header section
    st.markdown("""
        <div class="header-container">
            <h1 class="header-title">Monitor and Understand Air Quality</h1>
            <p>Analyze pollution levels, trends, and insights on air quality in your region.</p>
        </div>
    """, unsafe_allow_html=True)

    # Cards layout (side-by-side)
    st.markdown("""
        <div class="cards-container">
            <div class="info-card">
                <h2 class="info-card-title">Real-Time Monitoring</h2>
                <p class="info-card-description">
                    Track air quality in real-time across multiple locations with our interactive maps.
                </p>
            </div>
            <div class="info-card">
                <h2 class="info-card-title">Comprehensive Analysis</h2>
                <p class="info-card-description">
                    Gain insights into pollution trends and patterns with detailed analytics.
                </p>
            </div>
            <div class="info-card">
                <h2 class="info-card-title">Customizable Queries</h2>
                <p class="info-card-description">
                    Ask specific questions and receive tailored answers on air quality data.
                </p>
            </div>
        </div>

    """, unsafe_allow_html=True)

    st.markdown("""
            <div class="header-container">
                <h1 class="header-title">Understand Air Quality Index</h1>
                <p>Analyze pollution levels, trends, and insights on air quality in your region.</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("""
            - The AQI has shown fluctuations in various cities, with industrial areas facing higher pollution levels.
            - The highest pollution levels were recorded in **2019**, with an average AQI exceeding 300 in major metro cities.
            - Measures taken post-2020 have helped improve air quality in many regions.
            """)

    st.markdown(
        """
        This app shows you the air pollution levels in Indian cities.
        It tracks NO2, CO, AOI, PM 2.5, PM 10, and more. You'll see pollution trends and get health recommendations.l.

        """
    )
    st.header("**📈 Air Quality Summary (2015-2020)**")
    st.write("""
            - The AQI has shown fluctuations in various cities, with industrial areas facing higher pollution levels.
            - The highest pollution levels were recorded in **2019**, with an average AQI exceeding 300 in major metro cities.
            - Measures taken post-2020 have helped improve air quality in many regions.
            """)

    st.markdown(
        """
        This app shows you the air pollution levels in Indian cities.
        It tracks NO2, CO, AOI, PM 2.5, PM 10, and more. You'll see pollution trends and get health recommendations.l.

        """
    )

# Use Cases page
# Use Cases page
def use_cases_page():
    st.title("Use Cases")

    # Description of Use Cases
    st.write("""
        Discover how air quality data can be used in different domains:
    """)

    # Cards layout for Use Cases
    st.markdown("""
        <div class="cards-container">
            <div class="info-card">
                <h2 class="info-card-title">Urban Planning</h2>
                <p class="info-card-description">
                    Air quality data helps urban planners make decisions about zoning, green spaces, and traffic management.
                </p>
            </div>
            <div class="info-card">
                <h2 class="info-card-title">Health Impact Assessments</h2>
                <p class="info-card-description">
                    Researchers and health organizations use air quality data to study its impact on public health.
                </p>
            </div>
            <div class="info-card">
                <h2 class="info-card-title">Environmental Policy</h2>
                <p class="info-card-description">
                    Policymakers rely on air quality data to draft regulations and environmental protection policies.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Add more use cases as needed
    st.markdown("""
        <div class="cards-container">
            <div class="info-card">
                <h2 class="info-card-title">Research and Education</h2>
                <p class="info-card-description">
                    Air quality data is essential in academic research and can be used to educate the public about pollution levels.
                </p>
            </div>
            <div class="info-card">
                <h2 class="info-card-title">Transportation Safety</h2>
                <p class="info-card-description">
                    Real-time air quality data can help ensure the safety of transportation systems, especially during high pollution events.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)


# Dashboard page (with Power BI embed)
def dashboard_page():
    st.title("Dashboard")
    st.write("""
        Explore insights into air quality trends through the interactive dashboard below:
    """)

    # Embed Power BI dashboard
    st.components.v1.iframe(
        src="https://app.powerbi.com/reportEmbed?reportId=76a6849e-d201-40b3-b305-4385f9da75f7&autoAuth=true&ctid=f497e3a6-df97-4d8a-93ef-88fbb967478f",
        width=1000,
        height=600,
        scrolling=True,
    )


def load_data():
    df = pd.read_csv('C:/Users/Dell/OneDrive/Desktop/Cleaned_Data_air.csv')
    return df

def conclusion():
    st.markdown("""
                        <div style="background-color: rgba(0, 0, 0, 0.6); padding: 30px; border-radius: 15px; margin: 20px 0;">
                        <blockquote style="font-style: italic; font-size: 24px; color: #ff6f61; text-align: center; margin-bottom: 20px;">
                        "The air we breathe is the very essence of life. Understanding it is our first step towards protecting it."
                        </blockquote>

                        <p style="color: white; font-size: 18px; line-height: 1.6; text-align: justify;">
                        Our Air Quality Prediction app is more than just a tool—it's a mission to empower individuals with critical environmental insights. 
                        In an era of increasing environmental challenges, knowledge is our most powerful weapon in the fight for cleaner, healthier air.
                        </p>

                        <h2 style="color: #4CAF50; text-align: center; margin-top: 20px;">Our Vision</h2>

                        <p style="color: white; font-size: 16px; line-height: 1.6; text-align: justify;">
                        We believe that by providing real-time, accurate air quality information, we can:
                        • Raise awareness about environmental health
                        • Help individuals make informed decisions
                        • Contribute to a global movement of environmental consciousness
                        </p>

                        <p style="color: #FFEB3B; text-align: center; margin-top: 20px; font-size: 16px;">
                        Together, we can breathe easier. Together, we can make a difference.
                        </p>
                        </div>
                        """, unsafe_allow_html=True)

# Queries page (with pollutant and city selection)
def queries_page():
    st.title("Queries")
    st.write("""
        Submit queries to retrieve specific air quality data.
        You can filter data by city, select pollutants, and analyze trends.
    """)

    # Load the data
    df = load_data()

    # Get the list of unique cities
    cities = df['City'].unique()

    # Dropdown for city selection
    city = st.selectbox("Select City:", cities)

    # List of pollutants to choose from
    pollutants = {
        "PM10": "PM10 🌫️",
        "PM2.5": "PM2.5 🌀",
        "NO2": "NO2 💨",
        "NO": "NO ⚡",
        "NOx": "NOx 🌩️",
        "NH3": "NH3 🧪",
        "CO": "CO 🛑",
        "SO2": "SO2 🏭",
        "O3": "O3 🌳",
        "Benzene": "Benzene 🧴",
        "Toluene": "Toluene 🌼"
    }

    # Allow users to select multiple pollutants horizontally
    num_columns = 3  # Number of columns for the horizontal layout
    columns = st.columns(num_columns)

    # List to store selected pollutants
    selected_pollutants = []
    pollutant_keys = list(pollutants.keys())

    for i in range(0, len(pollutants), num_columns):
        column_pollutants = pollutant_keys[i:i + num_columns]

        for j, pollutant in enumerate(column_pollutants):
            with columns[j]:
                if st.checkbox(pollutants[pollutant], key=pollutant):
                    selected_pollutants.append(pollutant)

    # Button to submit the query
    if st.button("Submit Query"):
        if not selected_pollutants:
            st.write("Please select at least one pollutant.")
        else:
            # Filter data based on selected city and pollutants
            filtered_data = df[df['City'] == city][['YEAR'] + selected_pollutants]

            # Check if the filtered data is empty
            if filtered_data.empty:
                st.write(f"No data found for the selected pollutants in {city}.")
            else:
                # Generate the response in English sentences
                result = f"The air quality data for {city} is as follows:\n\n"

                for pollutant in selected_pollutants:
                    latest_data = filtered_data[pollutant].values[-1]  # Get the most recent data
                    result += f"The {pollutants[pollutant].split()[0]} level is {latest_data}.\n"

                # Display the response
                st.write(result)


# Review page
# Send feedback email function
def send_feedback_email(rating, suggestion):
    try:
        # Email configuration
        smtp_server = "smtp.office365.com"
        smtp_port = 587
        smtp_user = "support@aptpath.in"
        smtp_password = "kjydtmsbmbqtnydk"
        sender_email = "support@aptpath.in"
        receiver_email = "jmanya216@gmail.com"

        # Create the email content
        subject = "New Feedback from Air Quality App"
        body = f"Rating: {rating} Stars\n\nSuggestion: {suggestion}"

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()

        # Notify the user of success
        st.success("Thank you for your feedback! Your review has been submitted.")
    except Exception as e:
        st.error(f"Failed to send feedback. Error: {e}")


# Review page function
def review_page():
    st.title("Review the Air Quality App")

    # Custom star rating with emojis
    st.write("**Rate the App (1 to 5 Stars):**")
    star_options = ["★", "★★", "★★★", "★★★★", "★★★★★"]
    rating = st.radio("Your Rating", options=range(1, 6), format_func=lambda x: star_options[x - 1])

    # Collect user suggestions using a text box
    st.write("**Provide Your Suggestions or Feedback Below:**")
    suggestion = st.text_area("Enter your feedback:")

    # Submit button to send feedback
    if st.button("Submit Feedback"):
        if suggestion.strip():  # Ensure the suggestion is not empty
            send_feedback_email(rating, suggestion)  # Send email with rating and feedback
        else:
            st.warning("Please enter some feedback or suggestions before submitting.")


# Download page
def download_page():
    st.title("Download Power BI Dashboard")

    st.write("""
        You can download the Power BI dashboard file below to explore the air quality data and analytics on your local system.
    """)

    # Provide a downloadable .pbix file (Power BI file)
    with open("C:/Users/Dell/Downloads/MANYAinf.pbix", "rb") as f:  # Replace with your actual file path
        st.download_button(
            label="Download Power BI Dashboard",
            data=f,
            file_name="Dashboard_Air_Quality.pbix",
            mime="application/octet-stream",
        )

    st.download_button(
        label="Download Dataset",
        data="This is your dataset content.",
        file_name="Data_air.csv",
        mime="text/csv"
    )


def display_quiz():
    st.subheader("Quiz")
    questions = {
        "What does the Air Quality Index (AQI) measure?": ["Water Purity", "Air Pollution levels", "Soil Quality",
                                                           "Noise Pollution"],
        "What is the main cause of air pollution?": ["Factories", "Trees", "Lakes", "Mountains"],
        "Which gas is most responsible for global warming?": ["Oxygen", "Nitrogen", "Carbon Dioxide",
                                                              "Hydrogen"],
        "What is a major consequence of water pollution?": ["Clean water", "Marine life destruction",
                                                            "Better farming",
                                                            "Fresh air"],
        "Which of the following is an effective way to improve air quality?": ["Dirty water", "Marine life destruction",
                                                                               "Encouraging public transportation and vehicles",
                                                                               "Building more highways"],
        "Which of these technologies can help reduce air pollution?": ["Air Purifiers",
                                                                       "Catalytic converters in vehicles",
                                                                       "Renewable Energy sources", "All of the above"],
        "Which of these is a natural source of air pollution?": ["Forest fires", "Car emissions", "Factory smoke",
                                                                 "Power plants"],
        "Long-term exposure to high levels of air pollution can lead to:": ["Respiratory diseases",
                                                                            "Cardiovascular problems",
                                                                            "Increased risk of lung cancer",
                                                                            "All of the above"],
        "Which of the following groups is MOST vulnerable to poor air quality?": [
            " People with no underlying conditions", "College students", "Young children and elderly people",
            "Professional athletes"],
        "What AQI range is considered “Unhealthy for Sensitive Groups”?": ["0-50", "51-100", "101-150", "151-200"]

    }
    answers = ["Air Pollution levels", "Factories", "Carbon Dioxide", "Marine life destruction",
               "Encouraging public transportation and vehicles", "All of the above", "Forest fires", "All of the above",
               "Young children and elderly people", "101-150"]
    user_answers = []

    for i, (question, options) in enumerate(questions.items()):
        user_answers.append(st.radio(question, options, key=i))

    if st.button("Submit Quiz"):
        score = sum([1 for i in range(len(answers)) if user_answers[i] == answers[i]])
        st.success(f"Your Score: {score}/{len(answers)}")


def check_aqi_status():
    st.subheader("Check Your Status")
    aqi = st.number_input("Enter AQI value:", min_value=0, max_value=500, step=1)

    if aqi >= 0 and aqi <= 50:
        bg_color = "#90EE90"
        status = "Good"
        img = "img_3.png"
    elif aqi >= 51 and aqi <= 100:
        bg_color = "#FFFF99"
        status = "Moderate"
        img = "img_4.png"
    elif aqi >= 101 and aqi <= 150:
        bg_color = "FFA07A"
        status = "Unhealthy for Sensitive Groups"
        img = "img_5.png"
    elif aqi >= 151 and aqi <= 200:
        bg_color = "#FF6347"
        status = "Unhealthy"
        img = "img_6.png"
    elif aqi >= 201 and aqi <= 300:
        bg_color = "#4B0082"
        status = "Very Unhealthy"
        img = "img_7.png"
    else:
        bg_color = "#BB9DDE"
        status = "Hazardous"
        img = "img_8.png"

    st.markdown(f'<div style="background-color: {bg_color}; padding: 40px; border-radius: 10px;">',
                unsafe_allow_html=True)
    st.markdown(f"### AQI Status: {status} {img}")
    st.image(img, width=400)
    st.markdown("</div>", unsafe_allow_html=True)









# Render the sidebar navigation
navigation()

# Display the selected page
# Display the selected page
if st.session_state.page == "🏠Home":
    home_page()
elif st.session_state.page == "📜Use Cases":
    use_cases_page()
elif st.session_state.page == "📊Dashboard":
    dashboard_page()
elif st.session_state.page == "🙋Queries":
    queries_page()
elif st.session_state.page == "⭐💬Review":
    review_page()
elif st.session_state.page == "⬇️Download":
    download_page()
elif st.session_state.page == "❓FAQ":
    faq.app()
elif st.session_state.page == "📝Conclusion" :
    conclusion()
elif st.session_state.page == "🥇Quiz" :
    display_quiz()
elif st.session_state.page == "🔎Check Status":
    check_aqi_status()

st.sidebar.button("🔚 Logout", on_click=lambda: (st.session_state.update(authenticated=False)))