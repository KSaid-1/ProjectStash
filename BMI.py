# Calculate Body mass index (BMI) which is a value derived from the mass and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms and height in metres
mass = float(input("Mass in kilograms? "))
height = float(input("Height in metres? "))
bmi = mass/height**2
print ("Body mass index = ",bmi)
if bmi < 18.5:
    print ("Underweight")
if 18.5 <= bmi <= 24.9:
    print ("Normal weight")
if 24.9 < bmi <= 29.9:
    print ("Overweight")
if bmi > 29.9:
    print ("obese")
#----------------plot-------------------------
import numpy as np
import matplotlib.pyplot as plt
X, Y = np.meshgrid(np.linspace(10, 120, 100), np.linspace(1, 2, 100))
Z = X/Y**2
levels = [np.min(Z),18.5,24.9,29.9,np.max(Z)]

# plot
fig, ax = plt.subplots()
ax.contourf(X, Y, Z, levels=levels,cmap='Greys')
ax.scatter(mass,height,marker="*",c="black")
if bmi < 18.5:
    ax.text(mass-7.,height+0.02,"You're Underweight")
if 18.5 <= bmi <= 24.9:
    ax.text(mass-7.,height+0.02,"You're Normal")
if 24.9 < bmi <= 29.9:
    ax.text(mass-7.,height+0.02,"You're Overweight")
if bmi > 29.9:
    ax.text(mass-7.,height+0.02,"You're obese")
ax.text(30.,1.95,"Underweight")
ax.text(78.,1.95,"Normal")
ax.text(96.,1.95,"Overweight")
ax.text(90.,1.4,"Obese")
ax.set_xlabel(r'Mass [kg]', color= 'Black')
ax.set_ylabel(r'Height [m]', color= 'Black')
plt.show()
