

# Interactive BMI + Diet Plan App

# --- Inputs from user ---
name = input("Enter your name: ")
height_cm = float(input("Enter your height (in cm): "))
weight_kg = float(input("Enter your weight (in kg): "))
has_kitchen = input("Do you have kitchen access? (yes/no): ").lower() == "yes"

# --- BMI calculation ---
height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

# --- BMI category ---
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
else:
    category = "Overweight"

# --- Diet plans ---
underweight_diets = ["Eggs", "Paneer", "Dal", "Nuts", "Banana milkshake"]
normal_diets = ["Roti", "Sabzi", "Dal", "Fruits", "Curd"]
overweight_diets = ["Oats", "Boiled veggies", "Fruits", "Moong dal", "Salads"]
hostel_tips = ("Fruits", "Curd", "Chana", "Avoid fried food", "Drink more water")

# --- Choose plan ---
if has_kitchen:
    if category == "Underweight":
        plan = underweight_diets
    elif category == "Normal":
        plan = normal_diets
    else:
        plan = overweight_diets
else:
    plan = hostel_tips

# --- Output ---
print("\n----- BMI & Diet Report -----")
print("Name:", name)
print("Height (cm):", height_cm)
print("Weight (kg):", weight_kg)
print("Kitchen access:", "Yes" if has_kitchen else "No")
print("BMI:", round(bmi, 1))
print("Category:", category)
print("Diet Plan:", ", ".join(plan))
print("-----------------------------")