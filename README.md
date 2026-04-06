# 🚗 BMW Customer Intelligence & AI Strategy

### 🌟 Project Overview
This is an End-to-End **Data Science & Engineering** project designed to segment BMW customers and automate marketing strategies. It features a synthetic data generator, a **MySQL ETL pipeline**, and a **Live Streamlit Dashboard**.

### 🛠️ Tech Stack
- **Language:** Python
- **Database:** MySQL (SQLAlchemy)
- **ML Algorithm:** K-Means Clustering
- **Dashboard:** Streamlit & Plotly
- **Environment:** python-dotenv (Security)

### 🚀 Key Features
1. **AI Segmentation:** Groups 10,000+ customers into personas (Luxury Veterans, Aspiring Techies, etc.) using K-Means.
2. **SQL Pipeline:** Automated data migration from CSV to MySQL with secure URL-encoded connections.
3. **Business Logic:** Generates "Next Best Action" for every customer to improve sales conversion.
4. **Live Dashboard:** Real-time analytics connected directly to the MySQL backend.

### 📁 How to Run
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up your `.env` file with MySQL credentials.
4. Run `python mysql_pipeline.py` to load data.
5. Launch dashboard: `streamlit run app.py`.
