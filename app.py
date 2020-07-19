from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("german_gpa.pkl","rb"))

@app.route("/",methods=["GET"])
def Home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method == "POST":
        max_cgpa = int(request.form['max_'])
        min_cgpa = int(request.form['min_'])
        obtained_cgpa = float(request.form['grade'])
        if obtained_cgpa < min_cgpa:
            return render_template("index.html",converted_gpa = "Obatined Grade should be greater than minimum Grade")
        prediction = model.predict([[max_cgpa,min_cgpa,obtained_cgpa]])
        output = round(prediction[0],1)
        if output<0:
            return render_template("index.html",converted_gpa = "Please the check the credentials again")
        else:
            return render_template("index.html",converted_gpa = "Converted GPA is {}".format(output))
    else:
        return render_template("index.html")
    
if __name__=="__main__":
    app.run(debug=True)