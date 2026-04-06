import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1.DATA GENERATION
np.random.seed(42)
n = 10000
cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Gurgaon"]
car_models = ["BMW X1", "BMW X3", "BMW X5", "BMW 3 Series", "BMW i4"]

data = pd.DataFrame({
    "customer_id": range(1, n+1),
    "age": np.random.randint(22, 65, n),
    "city": np.random.choice(cities, n),
    "website_visits": np.random.randint(1, 40, n),
    "instagram_engagement": np.random.randint(0, 100, n),
    "interested_model": np.random.choice(car_models, n),
    "ad_clicks": np.random.randint(0, 15, n),
    "brochure_download": np.random.choice([0, 1], n, p=[0.7, 0.3])
})

# Logic Injection
data['income_lpa'] = data['age'].apply(lambda x: x * 1.2 + np.random.normal(10, 5)) 
data['configurator_used'] = (data['website_visits'] > 20).astype(int)
data['test_drive'] = ((data['income_lpa'] > 35) & (data['configurator_used'] == 1)).astype(int)
data['purchase'] = data.apply(lambda r: 1 if (r['income_lpa']>45 and np.random.random()<0.7) else 0, axis=1)

# 2. ML CLUSTERING (Personas)
features = ['age', 'income_lpa', 'instagram_engagement']
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[features])
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
data['cluster'] = kmeans.fit_predict(scaled_features)
persona_map = {0: "Luxury Veteran", 1: "Aspiring Techie", 2: "Window Shopper"}
data['persona'] = data['cluster'].map(persona_map)

# --- 3. ETL PIPELINE LOGIC  ---
data["intent_score"] = (data["configurator_used"] * 10) + (data["brochure_download"] * 5)
conditions = [
    (data["purchase"] == 1),
    (data["test_drive"] == 1),
    (data["intent_score"] > 10),
    (data["website_visits"] > 15)
]
choices = ["Buyer", "Hot Lead", "Warm Lead", "Aware"]
data["journey_stage"] = np.select(conditions, choices, default="Cold Lead")

action_conditions = [
    (data["journey_stage"] == "Buyer"),
    (data["journey_stage"] == "Hot Lead"),
    (data["journey_stage"] == "Warm Lead"),
    (data["journey_stage"] == "Aware")
]
action_choices = ["Service Package Offer", "Immediate Sales Call", "Personalized Email", "Retargeting Ads"]
data["next_action"] = np.select(action_conditions, action_choices, default="Brand Awareness")

# Final Save
data.to_csv("BMW_Customer_Intelligence.csv", index=False)
print("MASTER DATA READY! ")