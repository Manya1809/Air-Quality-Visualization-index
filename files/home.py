import streamlit as st

def app():
    st.title("**:violet[🌍WELCOME TO AIR VISUAL]**")
    st.write("""
        This web app provides an analysis of **air quality trends from 2015-2020** across multiple cities.

        **Overview:**
        - Track air quality changes over the years
        - Compare city-wise AQI levels
        - Identify pollution trends and patterns

        Navigate through the sections in the sidebar to explore data-driven insights.
        """)
    st.header("**:blue[🎗🌍AIR QUALITY INDEX]**")
    st.write("An air quality index (AQI) is an indicator developed by government agencies to communicate to the public how polluted the air currently is or how polluted it is forecast to become."
             " As air pollution levels rise, so does the AQI, along with the associated public health risk. ")
    image="img.png"
    st.image(image,width=300)

    st.header("**:blue[📈 Air Quality Summary (2015-2020)]**")
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

    # Impact on Health and Well-being

    st.header('🦠👩‍⚕🧬 :blue[Impact on Health and Well-being]')

    st.markdown("""
    Poor air quality isn't just an inconvenience; it poses a serious threat to human health and well-being. 
    Here's a breakdown of some key health concerns:

    - **Respiratory diseases**: Exposure to air pollutants irritates the lungs, worsening asthma symptoms and triggering chronic obstructive pulmonary disease (COPD). 
        A 2023 study published in the European Respiratory Journal found a link between long-term exposure to air pollution (particularly PM2.5) and an increased risk of developing COPD, highlighting the long-term consequences of air quality.

    - **Cardiovascular diseases**: Air pollution can damage blood vessels and increase the risk of heart attacks, strokes, and other cardiovascular problems. 
        A 2022 Harvard University study found that even short-term exposure to traffic-related air pollution can lead to an increased risk of heart attacks, emphasizing the need for immediate action in areas with high traffic volumes.
    """)

    # Impact on Life Expectancy
    st.header(':blue[🧘‍♀️🥗🍎 Impact on Life Expectancy]')

    st.markdown("""
    The impact of air pollution extends beyond immediate health problems. It can shorten lifespans:

    - **Reduced Life Expectancy**: The World Health Organization (WHO) estimates that air pollution cuts global life expectancy by an average of 1.8 years. 
        This means millions of lives are lost prematurely due to poor air quality.

    - **City-Specific Impact**: The impact varies by location. Highly polluted cities can see reductions in life expectancy as high as 4-5 years. 
        This highlights the need for stricter regulations and cleaner energy sources in urban areas.

    - **Fine Particulate Matter (PM2.5)**: Long-term exposure to PM2.5, tiny particles that enter deep into the lungs, is particularly detrimental and significantly reduces life expectancy.
    """)



