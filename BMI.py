import numpy as np
import matplotlib.pyplot as plt

# Constants for BMI categories
UNDERWEIGHT = 18.5
NORMAL_WEIGHT = 24.9
OVERWEIGHT = 29.9

def calculate_bmi(mass, height):
    return mass / height ** 2

def get_bmi_category(bmi):
    if bmi < UNDERWEIGHT:
        return "Underweight"
    elif bmi <= NORMAL_WEIGHT:
        return "Normal weight"
    elif bmi <= OVERWEIGHT:
        return "Overweight"
    else:
        return "Obese"

def plot_bmi_chart(mass, height, bmi):
    X, Y = np.meshgrid(np.linspace(10, 120, 100), np.linspace(1, 2, 100))
    Z = X / Y ** 2
    levels = [np.min(Z), UNDERWEIGHT, NORMAL_WEIGHT, OVERWEIGHT, np.max(Z)]

    fig, ax = plt.subplots()
    ax.contourf(X, Y, Z, levels=levels, cmap='Greys')
    ax.scatter(mass, height, marker="*", c="black")
    
    category = get_bmi_category(bmi)
    ax.text(mass - 7., height + 0.02, f"You're {category}")
    
    ax.text(30., 1.95, "Underweight")
    ax.text(78., 1.95, "Normal")
    ax.text(96., 1.95, "Overweight")
    ax.text(90., 1.4, "Obese")
    
    ax.set_xlabel(r'Mass [kg]', color='Black')
    ax.set_ylabel(r'Height [m]', color='Black')
    plt.show()

def main():
    try:
        mass = float(input("Mass in kilograms? "))
        height = float(input("Height in metres? "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    bmi = calculate_bmi(mass, height)
    print(f"Body mass index = {bmi:.2f}")
    print(get_bmi_category(bmi))
    plot_bmi_chart(mass, height, bmi)

if __name__ == "__main__":
    main()