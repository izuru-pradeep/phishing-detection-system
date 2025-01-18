import content_model.feature_extraction as fe
from bs4 import BeautifulSoup
import joblib

# Load the saved RandomForestClassifier model
model= joblib.load('content_model/model/rf_model.pkl')

def predict(response):
    soup = BeautifulSoup(response.content, "html.parser")
    vector = [fe.create_vector(soup)]  # it should be 2d array, so added []
    result = model.predict(vector)
    
    return result