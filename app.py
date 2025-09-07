import os
from flask import Flask, render_template,request, redirect, url_for
from ultralytics import YOLO
import cv2

app= Flask(__name__)

app.config["UPLOAD_FOLDER"]= "static/uploads"
app.config["RESULT_FOLDER"]="static/results"

model = YOLO("brain_tumor_model.pt", task="segment")

@app.route("/" ,methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return redirect(request.url)
    
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file :
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        results =model.predict(file_path, save=True, project=app.config["RESULT_FOLDER"] , name="output",exist_ok=True)
        result_path = os.path.join(app.config["RESULT_FOLDER"],"output", file.filename)
        return render_template('index.html', uploaded_image= file_path, result_image=result_path)


if __name__ == "__main__":
    app.run(debug=True)
