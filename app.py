# 1. Library imports
import uvicorn
from fastapi import FastAPI
from Model import WheatModel, WheatSpecies

# 2. Create app and model objects
app = FastAPI()
model = WheatModel()

@app.get('/')
def home():
    return{"Hello":"Welcome to the RMS first ML app mod 21:57 Aug 21."}
# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict')
def predict_species(wheat: WheatSpecies):
    data = wheat.dict()
    print(data)

    #prediction=1 
    #probability=2
    prediction, probability = model.predict_species(
        data['A'], data['P'], data['C'], data['L'], data['W'], data['CF'], data['LG']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }


# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8005)
    
    ## local host--> 127.0.0.0  
    ## host --> 0.0.0.0 allows all host
