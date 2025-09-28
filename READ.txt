# Ola Ride Insights Project

## 1. Problem Statement
The goal of this project was to analyze Ola's ride-sharing data to derive actionable insights for enhancing operational efficiency, improving customer satisfaction, and optimizing business strategies.

## 2. Project Workflow
1.  **Data Cleaning & Preparation**: Loaded the dataset, handled missing values, corrected data types, and engineered new features like `hour_of_day`.
2.  **SQL Analysis**: Imported the clean data into a MySQL database and ran 10 different SQL queries to extract specific insights.
3.  **Power BI Dashboard**: Connected Power BI to the MySQL database and built a multi-page, interactive dashboard with an "Ola" theme.
4.  **Streamlit Showcase**: Developed a web application to serve as a presentation layer for the final dashboard. The dashboard was designed to be fully interactive in Power BI, but due to account-related deployment constraints, a static version using high-quality screenshots is presented here.

## 3. Key Insights from the Dashboard
* **📈 Ride Volume Trends**: Ride activity remains consistently high, with predictable peaks during morning (7–10 AM) and evening (5–8 PM) commuter hours, supporting targeted driver allocation.

* **🚫 Cancellation Analysis**: Customer cancellations are primarily due to operational issues (e.g., driver not moving), while driver cancellations are dominated by personal or vehicle-related issues. This highlights a need for better driver-customer coordination.

* **💰 Revenue Insights**: Total revenue for the analyzed period reached ₹56.53M, with cash being the most used payment method. A small segment of top customers contributed disproportionately to this revenue, indicating an opportunity for loyalty programs.

* **📍 Vehicle Performance**: Prime Sedan leads in both distance traveled and revenue generated, making it the most commercially effective vehicle type.

* **⭐ Ratings Overview**: Both driver and customer ratings average around 4.0, indicating a generally satisfactory and consistent service quality with few outliers.

* **🌍 Geographic Distribution**: Ride pickups span multiple continents, with high activity in Asia and North America—indicating Ola’s global footprint and diverse user base.

* **📊 Fare vs. Distance Correlation**: A clear positive correlation exists between fare and ride distance. Premium vehicles show a higher fare-per-kilometer, validating the tiered pricing model.

## 4. Tools Used
* **Python**: Pandas (for data cleaning)
* **Database**: MySQL (for querying)
* **Visualization**: Power BI
* **Web App**: Streamlit

## 5. How to Run
1. Ensure all screenshot files are in the same directory.
2. Run the command: `streamlit run ola.py`