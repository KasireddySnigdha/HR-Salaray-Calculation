import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import tkinter as tk
from tkinter import messagebox

# Load the dataset
df = pd.read_csv("salaries_dataset.csv", sep=";")

# Create a linear regression model
linear_reg = LinearRegression()
linear_reg.fit(df[['experience_level']], df['salary'])

# Create a polynomial regression model
polynomial_regression = PolynomialFeatures(degree=4)
x_polynomial = polynomial_regression.fit_transform(df[['experience_level']])
polynomial_reg = LinearRegression()
polynomial_reg.fit(x_polynomial, df['salary'])

# Create a Tkinter window
window = tk.Tk()
window.title("HR Salary Prediction")

# Function to perform the prediction and display the result
def predict_salary():
    try:
        experience = float(entry_experience.get())

        # Perform linear regression prediction
        linear_pred = linear_reg.predict([[experience]])

        # Perform polynomial regression prediction
        poly_pred = polynomial_reg.predict(polynomial_regression.transform([[experience]]))

        messagebox.showinfo("Prediction Result",
                            f"Linear Regression Prediction: {linear_pred[0]}\n"
                            f"Polynomial Regression Prediction: {poly_pred[0]}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric value.")

# Create labels and entry fields for input
label_experience = tk.Label(window, text="Experience Level:")
label_experience.pack()
entry_experience = tk.Entry(window)
entry_experience.pack()

# Create a button to trigger the prediction
button_predict = tk.Button(window, text="Predict Salary", command=predict_salary)
button_predict.pack()

# Start the Tkinter event loop
window.mainloop()
