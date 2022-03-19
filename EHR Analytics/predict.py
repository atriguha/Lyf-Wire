import pickle

def predict(pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle,
            sacral_slope, pelvic_radius, degree_spondylolisthesis):
    model = pickle.load(open("model.sav", "rb"))
    diagnosis = ["Hernia", "Spondylolisthesis", "Normal"]
    pred = model.predict([[pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle,
                sacral_slope, pelvic_radius, degree_spondylolisthesis]])
    result = map(lambda x: diagnosis[x], pred)
    print(list(result))
    # print(diagnosis[pred])

if __name__ == "__main__":
    pelvic_incidence = float(input("Please Enter Pelvic Incidence Value of Patient: "))
    pelvic_tilt = float(input("Please Enter Pelvic Tilt Value of Patient: "))
    lumbar_lordosis_angle = float(input("Please Enter Lumbar Lordois Angle Value of Patient: "))
    sacral_slope = float(input("Please Enter Sacral Slope Value of Patient: "))
    pelvic_radius = float(input("Please Enter Pelvic Radius Value of Patient: "))
    degree_spondylolisthesis = float(input("Please Enter Degree Spondylolisthesis Value of Patient: "))
    predict(pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle,
                sacral_slope, pelvic_radius, degree_spondylolisthesis)
