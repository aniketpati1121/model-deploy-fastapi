from fastapi import FastAPI


app = FastAPI() 

def load_data():
    import json
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/")
def hello():
    return {"message": "paitent management system API"}

@app.get('/about')
def about():
    return {"message": "An API for managing patient data, including BMI calculations and health verdicts."} 

@app.get('/view')
def view():
    data = load_data()
    return {"patients": data}
         