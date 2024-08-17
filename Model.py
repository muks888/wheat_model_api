# 1. Library imports
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from pydantic import BaseModel
import joblib


# 2. Class which describes a wheat grain measurements
class WheatSpecies(BaseModel):
    A: float 
    P: float 
    C: float 
    L: float
    W: float
    CF: float
    LG: float



# 3. Class for training the model and making predictions
class WheatModel:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and 
    #    saves the model
    def __init__(self):
        self.df = pd.read_csv('wheat-dataset.csv')
        #for self.df in pd.read_csv("wheat-dataset.csv", chunksize=2):
        #print(self.df)
        self.model_fname_ = 'wheat-dataset_model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)
        

    # 4. Perform model training using the RandomForest classifier
    def _train_model(self):
        X = self.df.drop('Class', axis=1)
        y = self.df['Class']
        rfc = RandomForestClassifier()
        model = rfc.fit(X, y)
        return model


    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_species(self, A, P, C, L, W, CF, LG):
        data_in = [[A,P,C,L,W,CF,LG]]
        prediction = self.model.predict(data_in)
        print(prediction)
        print('-------------')
        probability = self.model.predict_proba(data_in).max()
        return prediction[0], probability
    
 
