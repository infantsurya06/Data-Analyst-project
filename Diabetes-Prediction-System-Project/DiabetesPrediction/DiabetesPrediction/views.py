from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(r"static/DiabetesPrediction/dataset/Diabetes Data.csv")

    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    pregnancies = float(request.GET['pregnancies'])
    glucose = float(request.GET['glucose'])
    blood_pressure = float(request.GET['blood-pressure'])    
    skin_thikness = float(request.GET['skin-thikness'])
    insulin = float(request.GET['insulin'])
    bmi = float(request.GET['bmi'])
    diabetes_pedigree = float(request.GET['diabetes-pedigree'])
    age = float(request.GET['age'])

    pared = model.predict([[pregnancies, glucose, blood_pressure, skin_thikness, insulin, bmi, diabetes_pedigree, age]])

    print()
    print("pregnancies =", pregnancies, "glucose =", glucose, "blood-pressure =", blood_pressure, "skin-thikness =", skin_thikness)
    print("insulin =", insulin, "bmi =", bmi, "diabetes_pedigree =", diabetes_pedigree, "age =", age)
    print()

    result1 = " "
    msg = None

    if pared == [1]:
        msg = "Oops! You have diabetes. 🙁 Please consult with your healthcare provider. 👍"
    elif pared == [0]:
        msg = "You do not have diabetes. 😊 Keep up with a healthy lifestyle. ✌"
    
    return render(request, 'predict.html', {'msg':msg})