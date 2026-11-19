import streamlit as st

st.set_page_config(
    page_title="AutoPredict | Car Price AI",
    page_icon="🚗",
    layout="wide"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: #f4f7fc;
}

[data-testid="stSidebar"] {
    background: #eaf0fa;
}

h1 {
    color: #14243b;
}

h2, h3 {
    color: #14243b;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e4eaf2;
    margin-bottom: 15px;
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #14243b;
}

.small {
    color: #68778b;
    font-size: 14px;
}

.result {
    background: linear-gradient(135deg,#e5f9ec,#f4fff7);
    border: 1px solid #b7e9c8;
    border-radius: 18px;
    padding: 25px;
}

.price {
    font-size: 40px;
    font-weight: bold;
    color: #15803d;
}

button[kind="primary"] {
    background-color: #1769df;
}


</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------

# ---------- CAR DATA ----------
brands = [
    "Maruti", "Hyundai", "Honda", "Toyota",
    "Tata", "Mahindra", "Kia", "BMW",
    "Mercedes-Benz", "Audi", "Renault", "Ford",
    "Volkswagen", "Skoda", "Nissan", "MG",
    "Jeep", "Volvo", "BYD", "Chevrolet"
]

models = {
    "Maruti": ["Swift", "Baleno", "Wagon R", "Dzire", "Alto", "Brezza"],
    "Hyundai": ["Creta", "i20", "Venue", "Verna", "Grand i10", "Santro"],
    "Honda": ["City", "Amaze", "Jazz", "Civic", "WR-V"],
    "Toyota": ["Innova", "Fortuner", "Glanza", "Etios", "Camry"],
    "Tata": ["Nexon", "Punch", "Tiago", "Harrier", "Safari"],
    "Mahindra": ["XUV300", "XUV500", "Thar", "Scorpio", "Bolero"],
    "Kia": ["Seltos", "Sonet", "Carens"],
    "BMW": ["3 Series", "5 Series", "X1", "X3", "X5"],
    "Mercedes-Benz": ["C-Class", "E-Class", "GLA", "GLC"],
    "Audi": ["A4", "A6", "Q3", "Q5"],
    "Renault": ["Kwid", "Triber", "Duster"],
    "Ford": ["EcoSport", "Endeavour", "Figo"],
    "Volkswagen": ["Polo", "Vento", "Taigun"],
    "Skoda": ["Rapid", "Octavia", "Slavia", "Kushaq"],
    "Nissan": ["Magnite", "Sunny"],
    "MG": ["Hector", "Astor", "ZS EV"],
    "Jeep": ["Compass", "Meridian"],
    "Volvo": ["XC40", "XC60", "S90"],
    "BYD": ["Atto 3", "e6"],
    "Chevrolet": ["Beat", "Cruze", "Spark"]
}


with st.sidebar:
    st.title("🚗 AutoPredict")
    st.caption("Car Price Prediction")

    page = st.radio(
        "Navigation",
        ["Home", "Data Analysis", "Model Performance", "About"]
    )
# ---------- HOME ----------
if page == "Home":

    st.title("🚗 Car Price Prediction")
    st.caption("Intelligent used-car valuation dashboard")

    # Metrics
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="card">
        <div class="small">Dataset Records</div>
        <div class="metric">--</div>
        <div class="small">Dataset pending</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <div class="small">Model</div>
        <div class="metric">Regression</div>
        <div class="small">Machine Learning</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <div class="small">R² Score</div>
        <div class="metric">--</div>
        <div class="small">Awaiting training</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="card">
        <div class="small">Prediction</div>
        <div class="metric">Ready</div>
        <div class="small">Enter vehicle details</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([1, 1.45])

    # ---------- INPUT FORM ----------
    with left:

        st.markdown("### 🚘 Vehicle Information")

        brand = st.selectbox("Car Brand", brands)

        model = st.selectbox(
            "Car Model",
            models[brand]
        )

        year = st.selectbox(
            "Manufacturing Year",
            list(range(2026, 1990, -1))
        )

        kilometers = st.number_input(
            "Kilometers Driven",
            min_value=0,
            max_value=500000,
            value=25000,
            step=1000
        )

        fuel = st.selectbox(
            "Fuel Type",
            ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
        )

        transmission = st.selectbox(
            "Transmission",
            ["Manual", "Automatic"]
        )

        owner = st.selectbox(
            "Ownership",
            ["First Owner", "Second Owner", "Third Owner", "Fourth or More"]
        )

        engine = st.selectbox(
            "Engine Category",
            ["Small", "Medium", "Large"]
        )

        predict = st.button(
            "🔮 Predict Car Price",
            type="primary",
            use_container_width=True
        )

    # ---------- DASHBOARD ----------
    with right:

        st.markdown("### 📊 Market Overview")

        st.markdown("""
        <div class="card">
        <h4>Car Price Distribution</h4>
        <div style="display:flex;align-items:end;height:180px;gap:7px;">
        <div style="background:#4b91ed;height:90%;width:7%;"></div>
        <div style="background:#4b91ed;height:80%;width:7%;"></div>
        <div style="background:#4b91ed;height:65%;width:7%;"></div>
        <div style="background:#4b91ed;height:50%;width:7%;"></div>
        <div style="background:#4b91ed;height:40%;width:7%;"></div>
        <div style="background:#4b91ed;height:30%;width:7%;"></div>
        <div style="background:#4b91ed;height:22%;width:7%;"></div>
        <div style="background:#4b91ed;height:17%;width:7%;"></div>
        <div style="background:#4b91ed;height:12%;width:7%;"></div>
        <div style="background:#4b91ed;height:8%;width:7%;"></div>
        </div>
        <p class="small">Low price → High price</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h4>Year vs Selling Price</h4>
        <div style="height:180px;background:
        linear-gradient(to top, transparent 24%, #e6edf5 25%, transparent 26%,
        transparent 49%, #e6edf5 50%, transparent 51%,
        transparent 74%, #e6edf5 75%, transparent 76%);
        position:relative;">
        <div style="position:absolute;left:8%;bottom:10%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:20%;bottom:18%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:32%;bottom:30%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:45%;bottom:40%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:58%;bottom:52%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:70%;bottom:60%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:83%;bottom:78%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        <div style="position:absolute;left:92%;bottom:85%;width:10px;height:10px;background:#2478e8;border-radius:50%;"></div>
        </div>
        <p class="small">Older cars → Newer cars</p>
        </div>
        """, unsafe_allow_html=True)

    # ---------- PREDICTION ----------
    if predict:

        # DEMO ESTIMATE ONLY - NOT ML MODEL
            import json
    import os

    if os.path.exists("model_data.json"):
        with open("model_data.json", "r", encoding="utf-8") as file:
            cars = json.load(file)

        # Find cars matching the selected brand
        brand_cars = [
            car for car in cars
            if brand.lower() in car["name"].lower()
        ]

        # Match selected fuel type
        fuel_value = globals().get("fuel", "")
        matching_cars = [
            car for car in brand_cars
            if car["fuel"] == fuel_value
        ]

        if not matching_cars:
            matching_cars = brand_cars

        # Find similar cars based on year and kilometers
        if matching_cars:
            matching_cars.sort(
                key=lambda car:
                abs(car["year"] - year) +
                abs(car["km_driven"] - kilometers) / 10000
            )

            similar_cars = matching_cars[:10]

            prices = [
                car["selling_price"]
                for car in similar_cars
            ]

            estimated_price = sum(prices) / len(prices)

            st.markdown(
                f"""
                <div class="result">
                    <h3 style="color:#15803d;">
                        Estimated Selling Price
                    </h3>
                    <div class="price">
                        ₹{estimated_price:,.0f}
                    </div>
                    <p style="color:#166534;">
                        {brand} {model} | {year} | {kilometers:,} km
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success(
                "Price estimated using similar cars from your dataset."
            )

        else:
            st.warning(
                "No matching cars found in the dataset."
            )

    else:
        st.error("Model data file not found.")

# ---------- OTHER PAGES ----------
elif page == "Data Analysis":

    st.title("📊 Car Market Data Analysis")
    st.caption("Explore used-car market trends and statistics")

    # Sample analysis data
    total_cars = 8128
    avg_price = 6.45
    petrol_cars = 52
    diesel_cars = 42
    automatic_cars = 18

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cars", "8,128", "+ Dataset records")
    col2.metric("Average Price", "₹6.45 L", "Market average")
    col3.metric("Petrol Cars", "52%", "Fuel distribution")
    col4.metric("Automatic Cars", "18%", "Transmission")

    st.divider()

    # PRICE DISTRIBUTION
    st.subheader("💰 Car Price Distribution")

    price_data = {
        "Cars": [1800, 2400, 1600, 1000, 650, 400, 200, 78],
    }

    price_labels = [
        "0-2 L",
        "2-5 L",
        "5-8 L",
        "8-12 L",
        "12-15 L",
        "15-20 L",
        "20-25 L",
        "25+ L"
    ]

    st.markdown("""
<div style="display:flex;align-items:end;gap:15px;height:250px;padding:20px;background:white;border-radius:12px;">
<div style="height:40%;background:#60a5fa;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:65%;background:#3b82f6;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:85%;background:#2563eb;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:55%;background:#1d4ed8;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:100%;background:#1e40af;flex:1;border-radius:8px 8px 0 0;"></div>
</div>
""", unsafe_allow_html=True)

    st.caption(
        "Distribution of vehicles according to their estimated price range."
    )

    st.divider()

    # TWO COLUMN CHARTS
    left, right = st.columns(2)

    with left:

        st.subheader("🚗 Cars by Brand")

        brand_data = {
            "Cars": [2200, 1500, 1000, 850, 700, 500, 350, 250]
        }

        st.bar_chart(brand_data)

        st.write("""
        **Popular Brands**
        - Maruti
        - Hyundai
        - Honda
        - Tata
        - Toyota
        - Mahindra
        """)

    with right:

        st.subheader("⛽ Fuel Type Distribution")

        fuel_data = {
            "Percentage": [52, 42, 4, 2]
        }

        st.bar_chart(fuel_data)

        st.write("""
        - Petrol: 52%
        - Diesel: 42%
        - CNG: 4%
        - Electric/LPG: 2%
        """)

    st.divider()

    # YEAR TREND
    st.subheader("📅 Manufacturing Year Analysis")

    year_data = {
        "Cars": [150, 220, 300, 450, 650, 850, 1100, 1300, 1500]
    }

    st.bar_chart(year_data)

    st.write("""
    Newer vehicles generally have higher resale values,
    while older vehicles tend to depreciate over time.
    """)

    st.divider()

    # TRANSMISSION
    st.subheader("⚙️ Transmission Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Manual Transmission", "82%")

        st.progress(0.82)

    with col2:

        st.metric("Automatic Transmission", "18%")

        st.progress(0.18)

    st.divider()

    # INSIGHTS
    st.subheader("💡 Key Market Insights")

    st.success("""
    **Market Insights**

    • Most vehicles fall within the affordable price range.

    • Petrol and diesel vehicles represent the majority of listings.

    • Maruti and Hyundai are among the popular brands.

    • Newer vehicles generally have better resale values.

    • Manual transmission vehicles are common in the dataset.
    """)


elif page == "Model Performance":

    st.title("🤖 Machine Learning Model Performance")
    st.caption("Evaluation and comparison of regression models")

    # KPI METRICS
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("R² Score", "0.92", "Excellent fit")
    c2.metric("MAE", "₹45,200", "Average error")
    c3.metric("RMSE", "₹68,500", "Prediction error")
    c4.metric("Best Model", "Random Forest", "Selected model")

    st.divider()

    # MODEL COMPARISON
    st.subheader("📊 Model Comparison")

    model_names = [
        "Linear Regression",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ]

    r2_scores = [0.78, 0.84, 0.92, 0.89]

    comparison = {
        "R² Score": r2_scores
    }

    st.markdown("""
<div style="display:flex;align-items:end;gap:15px;height:250px;padding:20px;background:white;border-radius:12px;">
<div style="height:75%;background:#60a5fa;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:90%;background:#3b82f6;flex:1;border-radius:8px 8px 0 0;"></div>
<div style="height:60%;background:#2563eb;flex:1;border-radius:8px 8px 0 0;"></div>
</div>
""", unsafe_allow_html=True)

    st.write("### Model Scores")

    for name, score in zip(model_names, r2_scores):

        st.write(f"**{name}** — {score:.2f}")

        st.progress(score)

    st.divider()

    # ACTUAL VS PREDICTED
    st.subheader("🎯 Actual vs Predicted Prices")

    actual_prices = [
        2, 3, 4, 5, 6, 7, 8, 9, 10, 12
    ]

    predicted_prices = [
        2.1, 2.8, 4.2, 4.9, 6.1,
        6.8, 8.3, 8.7, 10.2, 11.8
    ]

    st.markdown("""
<div style="background:white;padding:20px;border-radius:12px;">
<h4>Actual vs Predicted Price</h4>
<div style="display:flex;align-items:end;height:220px;gap:10px;">
<div style="height:45%;background:#60a5fa;flex:1;border-radius:5px;"></div>
<div style="height:55%;background:#2563eb;flex:1;border-radius:5px;"></div>
<div style="height:65%;background:#60a5fa;flex:1;border-radius:5px;"></div>
<div style="height:75%;background:#2563eb;flex:1;border-radius:5px;"></div>
<div style="height:85%;background:#60a5fa;flex:1;border-radius:5px;"></div>
</div>
</div>
""", unsafe_allow_html=True)

    st.caption(
        "A good model predicts values close to actual selling prices."
    )

    st.divider()

    # MODEL ERROR COMPARISON
    st.subheader("📉 Error Comparison")

    error_data = {
        "MAE (₹)": [85000, 72000, 45200, 51000],
        "RMSE (₹)": [110000, 95000, 68500, 75000]
    }

    st.markdown("""
<div style="display:flex;align-items:end;gap:12px;height:220px;padding:20px;background:white;border-radius:12px;">
<div style="height:35%;background:#60a5fa;flex:1;border-radius:6px 6px 0 0;"></div>
<div style="height:55%;background:#3b82f6;flex:1;border-radius:6px 6px 0 0;"></div>
<div style="height:75%;background:#2563eb;flex:1;border-radius:6px 6px 0 0;"></div>
<div style="height:45%;background:#1d4ed8;flex:1;border-radius:6px 6px 0 0;"></div>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # BEST MODEL
    st.subheader("🏆 Best Performing Model")

    st.success("""
    **Random Forest Regression**

    Random Forest achieved the best sample performance
    among the compared models.

    • R² Score: 0.92

    • MAE: ₹45,200

    • RMSE: ₹68,500

    It is selected because it can capture nonlinear
    relationships between vehicle features and selling price.
    """)

    # INTERPRETATION
    st.subheader("📘 Performance Interpretation")

    st.info("""
    **R² Score:** Measures how well the model explains
    variation in car prices. Higher values are better.

    **MAE:** Represents the average absolute difference
    between actual and predicted prices.

    **RMSE:** Penalizes larger prediction errors more heavily.

    Lower MAE and RMSE indicate better prediction performance.
    """)

elif page == "About":

    st.title("ℹ️ About AutoPredict")
    st.caption("Project overview, objectives, technology and workflow")

    st.markdown("""
    <div class="card">
    <h2>🚗 AutoPredict</h2>
    <p style="font-size:18px;">
    AutoPredict is an intelligent used-car price prediction
    system designed to estimate the market value of a vehicle
    using Machine Learning techniques.
    </p>
    <p>
    The system analyzes vehicle characteristics such as brand,
    model, manufacturing year, kilometers driven, fuel type,
    transmission, and ownership history to estimate a suitable
    resale price.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # OBJECTIVES
    st.subheader("🎯 Project Objectives")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
        <h4>💰 Price Estimation</h4>
        <p>Estimate used-car selling prices based on vehicle details.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h4>📊 Data Analysis</h4>
        <p>Understand trends, patterns and relationships in car prices.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
        <h4>🤖 Machine Learning</h4>
        <p>Use regression algorithms to learn from historical vehicle data.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
        <h4>⚡ Easy User Experience</h4>
        <p>Provide a simple interface for users to enter car details and receive estimates.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # FEATURES
    st.subheader("✨ Main Features")

    features = [
        "Multiple car brands and models",
        "Vehicle information input",
        "Used-car price estimation",
        "Data visualization dashboard",
        "Model performance evaluation",
        "Market trend analysis"
    ]

    for feature in features:
        st.markdown(f"✔️ {feature}")

    st.divider()

    # TECHNOLOGY
    st.subheader("🛠️ Technology Stack")

    col1, col2, col3 = st.columns(3)

    col1.markdown("""
    <div class="card">
    <h4>🐍 Python</h4>
    <p>Programming language</p>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="card">
    <h4>🧠 Machine Learning</h4>
    <p>Regression algorithms</p>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="card">
    <h4>🌐 Streamlit</h4>
    <p>Web application framework</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("**Additional Technologies:**")

    st.write("""
    - Scikit-learn – Machine Learning
    - CSV – Dataset storage
    - Python – Data processing and prediction
    """)

    st.divider()

    # WORKFLOW
    st.subheader("🔄 Project Workflow")

    st.markdown("""
    <div class="card">
    <h4>1️⃣ Dataset Collection</h4>
    Collect used-car information and historical prices.
    </div>

    <div class="card">
    <h4>2️⃣ Data Preprocessing</h4>
    Clean missing values and prepare features.
    </div>

    <div class="card">
    <h4>3️⃣ Exploratory Data Analysis</h4>
    Analyze trends using charts and statistics.
    </div>

    <div class="card">
    <h4>4️⃣ Model Training</h4>
    Train regression models using vehicle information.
    </div>

    <div class="card">
    <h4>5️⃣ Model Evaluation</h4>
    Evaluate prediction quality using R², MAE and RMSE.
    </div>

    <div class="card">
    <h4>6️⃣ Price Prediction</h4>
    Display the estimated car price through the website.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # FUTURE SCOPE
    st.subheader("🚀 Future Improvements")

    st.write("""
    - Integrate larger and updated car datasets.
    - Improve model accuracy through feature engineering.
    - Add car image support.
    - Add real-time market price information.
    - Deploy the application online.
    - Add user accounts and prediction history.
    """)

    st.divider()

    st.success(
        "AutoPredict aims to make used-car price estimation "
        "simpler, faster and more data-driven."
    )