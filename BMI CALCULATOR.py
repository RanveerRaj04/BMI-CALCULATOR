#BMI CALCULATOR

weight= float(input("enter your weight in kg :"))
height= float(input("enter your height in meters :"))

bmi = weight/pow(height,2)
result = round(bmi,1)

print(f"your bmi is {result} ")

if bmi<18.5 and bmi>0:
    print("you are underweight")
elif bmi>=18.5 and bmi<24.9:
    print("you have normal weight")
elif bmi>=25 and bmi<29.9:
    print("you are overweight")
else:
    print("you have obesity")
