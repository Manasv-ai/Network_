## 🧠 Network Security Threat Detection System

This project is an **end-to-end Machine Learning pipeline** designed to detect and predict potential **network security threats** using an automated **ETL (Extract, Transform, Load)** and **MLflow-tracked model**.
It also includes a **FastAPI-based web interface** to serve predictions and visualize results in an HTML table.

---

### 🚀 Features

* ✅ **Automated Data Ingestion:** Reads and validates raw network data from MongoDB or CSV files.
* ✅ **Data Validation:** Uses schema checks to ensure input data integrity.
* ✅ **Data Transformation:** Cleans, encodes, and normalizes data for model training.
* ✅ **Model Training & Evaluation:** Uses MLflow for model tracking, versioning, and performance logging.
* ✅ **Model Registry:** The best model is saved in the `final_model` directory.
* ✅ **Prediction API (FastAPI):** Allows prediction on new input data and displays output in an HTML table format.
* ✅ **Docker Support:** Easily containerize and deploy the entire project.

---

### 🧩 Project Structure

```
Network Security project/
│
├── Network_data/              # Raw network traffic data
├── Networksecurity/           # Core pipeline modules (ingestion, validation, transformation, training)
├── data_schema/               # JSON/YAML schema for data validation
├── final_model/               # Finalized trained ML model
├── mlruns/                    # MLflow experiment tracking directory
├── prediction_output/         # Generated prediction results
├── templates/                 # HTML templates for FastAPI frontend
├── valid_data/                # Cleaned and validated data ready for training
│
├── app.py                     # FastAPI application for prediction
├── main.py                    # Training and MLflow orchestration script
├── push_data.py               # Script to push data into MongoDB or local storage
├── Dockerfile                 # Docker setup for containerized deployment
├── requirment.txt             # Project dependencies
├── package.json               # For Node-related utility scripts (if any)
├── .gitignore                 # Git ignored files
└── README.md                  # Project documentation
```

---

### ⚙️ Installation & Setup

#### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "Network Security project"
```

#### 2. Create and activate a virtual environment

```bash
python -m venv venvs
venvs\Scripts\activate      # For Windows
source venvs/bin/activate   # For Linux/Mac
```

#### 3. Install dependencies

```bash
pip install -r requirment.txt
```

If you face FastAPI errors, ensure you have this installed:

```bash
pip install python-multipart
```

#### 4. Run the training pipeline

```bash
python main.py
```

This will perform ETL, validate data, train the model, and log metrics to MLflow.

#### 5. Start the FastAPI server

```bash
uvicorn app:app --reload
```

#### 6. Access the web interface

Open your browser and visit:

```
http://127.0.0.1:8000
```

Swagger Docs (API Testing UI):

```
http://127.0.0.1:8000/docs
```

---

### 🧮 Example Workflow

1. Place your input data in the **Network_data/** directory.
2. Run the pipeline using `python main.py`.
3. The cleaned data appears in **valid_data/**, and predictions in **prediction_output/**.
4. Launch the FastAPI app to upload or view predictions via an HTML table (under `/predict`).

---

### 📊 Tech Stack

* **Python 3.10+**
* **FastAPI** (Backend framework)
* **Scikit-learn / XGBoost** (ML models)
* **MLflow** (Model tracking)
* **Pandas / NumPy** (Data processing)
* **MongoDB** (Data source)
* **Docker** (Containerization)
* **Jinja2 Templates** (HTML rendering)

---

### 🧾 Author

**Manas Khatri**
*B.Tech in Mathematics and Computing*
*M.S. Ramaiah University of Applied Sciences*
