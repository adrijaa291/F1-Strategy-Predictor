# main.py

import joblib
import pandas as pd
import numpy as np

# === Load your saved model ===
rf = joblib.load('pit_strategy_model.pkl')

# === Load circuits and constructors CSVs ===
circuits = pd.read_csv('circuits.csv')
constructors = pd.read_csv('constructors.csv')

# Preprocess: add lowercase columns for robust matching
circuits['name_lower'] = circuits['name'].str.lower()
constructors['name_lower'] = constructors['name'].str.lower()

def predict_strategy(circuit_input, constructor_input):
    # Robust partial match
    circuit_match = circuits[circuits['name_lower'].str.contains(circuit_input.lower())]
    constructor_match = constructors[constructors['name_lower'].str.contains(constructor_input.lower())]

    if not circuit_match.empty:
        circuit_id_input = circuit_match.iloc[0]['circuitId']
        circuit_name_input = circuit_match.iloc[0]['name']
    else:
        return f"❌ No circuit found for '{circuit_input}'"

    if not constructor_match.empty:
        constructor_id_input = constructor_match.iloc[0]['constructorId']
        constructor_name_input = constructor_match.iloc[0]['name']
    else:
        return f"❌ No constructor found for '{constructor_input}'"

    # Predict for upcoming year
    example = np.array([[2025, circuit_id_input, constructor_id_input]])
    pred_stops = rf.predict(example).flatten()
    pred_stops = sorted([round(lap) for lap in pred_stops if lap > 0])

    # Merge silly close stops (within 5 laps)
    MIN_GAP = 5
    if len(pred_stops) > 1:
        clean_stops = [pred_stops[0]]
        for lap in pred_stops[1:]:
            if lap - clean_stops[-1] >= MIN_GAP:
                clean_stops.append(lap)
        if not clean_stops:
            clean_stops = [round(np.median(pred_stops))]
    else:
        clean_stops = pred_stops

    return f"✅ Recommended pit stops for {constructor_name_input} at {circuit_name_input}: {clean_stops}"
