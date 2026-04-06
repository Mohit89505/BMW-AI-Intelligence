import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse  # HELPS IN MY SQL SPECIAL SYMBOL :PASSWORD 

# 1. Database Details
user = "root"
raw_password = "YOUR_PASSWORD_HERE" # Password ko variable mein rakha
host = "localhost"
db_name = "bmw_db"

safe_password = urllib.parse.quote_plus(raw_password)

def run_mysql_pipeline(csv_file):
    try:
        # Step A: Load Cleaned CSV
        df = pd.read_csv(csv_file)

        # Step B: Create Engine (Yahan 'safe_password' use kiya hai)
        engine = create_engine(f"mysql+mysqlconnector://{user}:{safe_password}@{host}/{db_name}?compress=false")

        # Step C: Load Data
        df.to_sql("customer_analytics", con=engine, if_exists="replace", index=False)

        return f"✅ Success: 10,000 Rows migrated to MySQL Table 'customer_analytics'!"
    
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    result = run_mysql_pipeline("BMW_Customer_Intelligence.csv")
    print(result)