from url_model.featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model

model = load_model('url_model/model/phishingdetection')


def predict(url):
    data = featureExtraction(url)
    result = predict_model(model, data=data)
    
    # Get the prediction score for the positive class (Phishing)
    prediction_score = result['prediction_score'][0]  
    prediction_label = result['prediction_label'][0]  
    # domain_age = result['Domain_Age'][0]  
    # print('Result -> ', url)
    
    return {
        'prediction_label': prediction_label,
        'prediction_score': prediction_score * 100,
    }