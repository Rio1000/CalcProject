import numpy as np
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import messagebox

# Given data
heights = np.array([1.872, 2.362, 2.718, 3.188, 3.212, 3.555, 4.058, 4.543, 5.09])
weights = np.array([62.5, 100, 150, 200, 250, 300])
rope_lengths = np.array([
    [14, 56, 90, 135, 135, np.nan, 218, 275, 330],
    [2.5, 49, 75, 125, 117, np.nan, 190, 250, 300],
    [-2, 26, 55, 90, 97, np.nan, 160, 200, np.nan],
    [-4, 15, 47, 74, 75, np.nan, 148, 181, np.nan],
    [6.5, 0, 27, 60, 62, np.nan, 125, 159, np.nan],
    [-36, -9, 10, 43, 54, np.nan, 108.5, 149, 189]
])

# Filter data for fitting
valid_indices = ~np.isnan(rope_lengths)
filtered_weights = np.repeat(weights, len(heights))[valid_indices.flatten()]
filtered_heights = np.tile(heights, len(weights))[valid_indices.flatten()]
filtered_rope_lengths = rope_lengths[valid_indices]

# Define and fit model
def rope_length_model(x, a, b, c):
    return a * x[0] + b * x[1] + c

x_data = np.vstack((filtered_weights, filtered_heights))
params, _ = curve_fit(rope_length_model, x_data, filtered_rope_lengths)

# Prediction function
def predict_rope_length(weight, height):
    a, b, c = params
    return a * weight + b * height + c

# GUI setup
def calculate_rope_length():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bottle_height = float(bottle_height_entry.get())
        result = predict_rope_length(weight, height) - bottle_height + 25
        messagebox.showinfo("Predicted Rope Length", f"The predicted rope length (adjusted for bottle height) is: {result:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight, height, and bottle height.")
S
# Create tkinter window
window = tk.Tk()
window.title("Rope Length Predictor")

# Input fields
tk.Label(window, text="Enter Weight (g):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Enter Height (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Enter Bottle Height (cm):").grid(row=2, column=0, padx=10, pady=10)
bottle_height_entry = tk.Entry(window)
bottle_height_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate Rope Length", command=calculate_rope_length)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

window.mainloop()

