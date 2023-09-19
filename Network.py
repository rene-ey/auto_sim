import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras

# Daten aus CSV-Datei laden
data = pd.read_csv('results.csv')

# Feature-Vektoren und Labels extrahieren
X = data[['car_numbers1', 'car_numbers2', 'car_numbers3', 'car_numbers4', 'duration1', 'duration3']].values
y = data['total_waiting_time'].values

# Daten in Trainings- und Testsets aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalisierung der Daten (optional, aber oft nützlich)
X_train = X_train / np.max(X_train, axis=0)
X_test = X_test / np.max(X_test, axis=0)

# Definition des neuronalen Netzwerks
model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(6,)),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1)
])

# Kompilierung des Modells
model.compile(optimizer='adam', loss='mean_squared_error')

# Training des Modells
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Vorhersagen mit dem trainierten Modell
predictions = model.predict(X_test)
print("test")
# Weitere Schritte: Evaluierung des Modells, Anwendung in Ihrer Simulation etc.
