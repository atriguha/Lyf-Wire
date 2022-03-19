import pickle

def predict(model, pelvic_incidence, pelvic_tilt, )

if __name__ == "__main__":
    pelvic_incidence = float(input("Please Enter Pelvic Incidence Value of Patient: "))
    pelvic_tilt = float(input("Please Enter Pelvic Tilt Value of Patient: "))
    model = pickle.load(open("model.sav", "rb"))