import csv
import json
import re
import os

FILE_PATH = "dataset/Car details v3.csv"

def extract_number(value):
    if not value:
        return 0
    match = re.search(r"[\d.]+", str(value))
    return float(match.group()) if match else 0

data = []

with open(FILE_PATH, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            price = float(row["selling_price"])
            year = float(row["year"])
            km = float(row["km_driven"])
            engine = extract_number(row["engine"])
            power = extract_number(row["max_power"])
            seats = extract_number(row["seats"])

            if price > 0:
                data.append([year, km, engine, power, seats, price])

        except:
            continue

print("Cars used for training:", len(data))

# Features and target
X = [row[:5] for row in data]
Y = [row[5] for row in data]

# Normalize features
mins = [min(col) for col in zip(*X)]
maxs = [max(col) for col in zip(*X)]

normalized_X = []

for row in X:
    normalized_X.append([
        (row[i] - mins[i]) / (maxs[i] - mins[i] + 0.00001)
        for i in range(5)
    ])

# Simple linear regression training
weights = [0.0] * 5
bias = sum(Y) / len(Y)

learning_rate = 0.01
epochs = 3000

for epoch in range(epochs):
    predictions = []

    for row in normalized_X:
        prediction = bias + sum(
            weights[i] * row[i] for i in range(5)
        )
        predictions.append(prediction)

    errors = [
        predictions[i] - Y[i]
        for i in range(len(Y))
    ]

    bias_gradient = sum(errors) / len(errors)

    weight_gradients = []

    for j in range(5):
        gradient = sum(
            errors[i] * normalized_X[i][j]
            for i in range(len(errors))
        ) / len(errors)

        weight_gradients.append(gradient)

    bias -= learning_rate * bias_gradient

    for j in range(5):
        weights[j] -= learning_rate * weight_gradients[j]

# Save trained model
model = {
    "weights": weights,
    "bias": bias,
    "mins": mins,
    "maxs": maxs
}

with open("model_data.json", "w") as file:
    json.dump(model, file)

print("Model training completed!")
print("Model saved as model_data.json")