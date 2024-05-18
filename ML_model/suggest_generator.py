import pandas as pd
import pickle


def create_sugestion(year, km, fuel, trans, owner, mil, engine, seats, price):
    test = pd.DataFrame()

    test['Year'] = [int(year)]
    test['Kilometers_Driven'] = [int(km)]
    test['Fuel_Type'] = [int(fuel)]
    test['Transmission'] = [int(trans)]
    test['Owner_Type'] = [int(owner)]
    test['Mileage'] = [int(mil)]
    test['Engine'] = [int(engine)]
    test['Seats'] = [int(seats)]
    test['Price'] = [int(price)]

    gnb_pkl_file = "ML_model\car_classifier_model.pkl"

    with open(gnb_pkl_file, 'rb') as file:  
        model = pickle.load(file)

    y_pred = model.predict(test)

    #print(y_pred)

    return y_pred