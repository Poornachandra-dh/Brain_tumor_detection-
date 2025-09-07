# 🧠 Brain Tumor Detection Web App

A deep learning–powered web application for **brain tumor segmentation** using **YOLOv11n**.  
The model is trained on a custom MRI dataset, deployed via **Flask**, and **Dockerized** for easy deployment.

---

## 📌 Features
- ✅ Upload MRI images and get **tumor segmentation results**
- ✅ Powered by **YOLOv11n** custom-trained model
- ✅ Flask web interface for real-time inference
- ✅ Docker support for containerized deployment
- ✅ Organized project structure with `templates/`, `static/`, and `app.py`

---

## 📂 Project Structure
brain-tumor-detection/
│── app.py # Flask backend
│── requirements.txt # Python dependencies
│── Dockerfile # For containerization
│── .dockerignore
│── .gitignore
│── brain_tumor_model.pt # YOLOv11n trained model
│── templates/
│ └── index.html # Frontend (upload form + results)
│── static/
│ ├── uploads/ # Uploaded MRI images
│ └── results/output/ # Segmented output images
│── notebook/
│ └── brain.ipynb # Training / experimentation




---

## ⚙️ Installation (Local Setup)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/brain-tumor-detection.git
cd brain-tumor-detection



python -m venv env
source env/bin/activate       # Linux/Mac
env\Scripts\activate          # Windows



pip install -r requirements.txt


python app.py


docker build -t brain-tumor-app .

docker run -p 5000:5000 brain-tumor-app
