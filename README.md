# F1-Strategy-Predictor

# 🏎️ Formula 1 Pit Stop Strategy Optimizer

This project predicts **optimal pit stop strategies** for Formula 1 races based on the given circuit and constructor name. It uses real-world data from the [OpenF1 API](https://openf1.org/) and a machine learning model trained on historical race data from Kaggle. The UI is sleek and interactive, featuring a racing video background and a clean, responsive input form.

---

## 🚀 Features

- 🏁 Input any **F1 circuit name** and **constructor name**
- 🤖 Predicts **best lap numbers for pit stops** using a trained Random Forest model
- 🌍 Uses actual race data from multiple seasons
- 💡 Smart lap merging logic (no redundant pit stops)
- 🎨 Stylish HTML + CSS frontend with fullscreen video background
- ⚙️ Flask-based backend integration for easy deployment

---

## 📸 UI Preview

> ![Preview](cars.mp4)

---

## 🎥 Demo Video

▶️ [Watch the screen recording](https://drive.google.com/file/d/11YpIFQedqJi4NHsrJMXm4Yg8FLtuRuOg/view?usp=sharing)

---

## 🧠 How It Works

1. User enters a **circuit name** and **constructor name** via the frontend.
2. The backend:
   - Matches them to real circuit and constructor IDs using CSVs.
   - Forms a feature vector `[year, circuitId, constructorId]`.
   - Uses a trained **MultiOutput Random Forest Regressor** to predict up to 3 pit stop laps.
   - Post-processes and merges closely spaced stops.
3. Final recommended pit stop lap numbers are shown in the UI.

---

## 🧪 Model Training (Colab)

The model is trained using historical F1 race data from Kaggle:

- **Dataset Source**:  
  📦 [Formula 1 World Championship 1950–2020 (by Rohan Rao)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)

- Files used:
  - `pit_stops.csv`
  - `races.csv`
  - `results.csv`
  - `constructors.csv`
  - `circuits.csv`

- Features:
  - `year`, `circuitId`, `constructorId`

- Targets:
  - Up to 3 pit stop lap numbers (padded if fewer)

- Model:
  ```python
  rf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
  rf.fit(X_train, y_train)
  
- Evaluation:
 ```python
   MAE = mean_absolute_error(y_test, rf.predict(X_test))
 ```

- Export
  ```python
  joblib.dump(rf, 'pit_strategy_model.pkl')
  ```

  Download the Trained Model
  Due to GitHub’s file size limit, the model is hosted on Google Drive: https://drive.google.com/file/d/11YpIFQedqJi4NHsrJMXm4Yg8FLtuRuOg/view?usp=drive_link

  Project Structure:
  ```bash
  ├── app.py                  # Flask backend
  ├── main.py                 # Strategy prediction using ML model
  ├── templates/
   └── index.html          # Frontend form with video background
  ├── static/
    └── cars.mp4            # Background racing video
  ├── circuits.csv            # Circuit info
  ├── constructors.csv        # Constructor info
  ├── pit_strategy_model.pkl  # 🔗 Download from Google Drive
  ├── requirements.txt        # Dependencies
  └── README.md
  ```
Running Locally
1. Clone the Repo
```bash
git clone https://github.com/your-username/Formula1_strategy.git
cd Formula1_strategy
```
2. Install Requirements
```bash
pip install -r requirements.txt
```
3. Add Model File
Download the model file from this link
```bash
Place it as pit_strategy_model.pkl in the root directory.
```
4. Run the App
```bash
python app.py
```
Visit http://127.0.0.1:5000 in your browser.

Requirements:
flask
numpy
pandas
scikit-learn
joblib

📌 Future Enhancements
Integrate live weather and tire data
Predict strategies per driver
Support for multiple constructors
Deploy on Streamlit or PythonAnywhere

🏁 Credits
📊 Dataset: Kaggle - Formula 1 World Championship 1950–2020 (Rohan Rao)
🤖 ML Model: Scikit-learn Random Forest Regressor
💻 UI: Custom HTML + CSS with embedded racing video
