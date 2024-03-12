import pandas as pd
from django.shortcuts import render
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def result(request):
    data = pd.read_csv(r"D:\PROJECT INFANT\PROJECT COMPLTE\DiabetesPrediction\diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    Val1 = float(request.GET['n1'])
    Val2 = float(request.GET['n2'])
    Val3 = float(request.GET['n3'])
    Val4 = float(request.GET['n4'])
    Val5 = float(request.GET['n5'])
    Val6 = float(request.GET['n6'])
    Val7 = float(request.GET['n7'])
    Val8 = float(request.GET['n8'])
    
    prediction = model.predict([[Val1, Val2, Val3, Val4, Val5, Val6, Val7, Val8]])
    
    if prediction[0] == 1:
        result1 = "positive"
    else:
        result1 = "negative"
        
    return render(request, template_name="predict.html", context={"result2": result1})
