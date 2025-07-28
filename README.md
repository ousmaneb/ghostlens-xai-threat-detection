# GhostLens: Explainable AI for Threat Detection

GhostLens is an open-source tool that combines machine learning and explainable AI (XAI) to detect and interpret cybersecurity threats in real time. It’s designed to support analysts who need clarity and confidence in what the model sees — not just predictions, but reasons.

This project is part of a growing portfolio focused on practical applications of AI and machine learning in cybersecurity.

---

## What It Does

- Detects anomalies in labeled network traffic data using a supervised machine learning model (Random Forest)
- Supports clear explanations using SHAP and interpretable models
- Visualizes predictions and key insights for analysts
- Focuses on real-world attack types such as DDoS and benign flows

---

## Dataset

We use a subset of the [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) dataset:

- `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`

This file contains labeled network flow records, including both benign and DDoS traffic.

---

## Technologies

- **Python 3**
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- SHAP, LIME
- Streamlit (for deployment)
- Jupyter Notebooks
- Git, GitHub

---

## Project Structure

ghostlens-xai-threat-detection/
│
├── data/ # Raw dataset (not pushed to GitHub)
├── notebooks/ # Data exploration and model training
├── models/ # Trained model (.pkl) and feature list (.json)
├── app.py # Streamlit app for prediction
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ghostlens-xai-threat-detection.git
cd ghostlens-xai-threat-detection

### 2. Set up your environment
python -m venv venv
.\venv\Scripts\activate        # On Windows
# Or: source venv/bin/activate  # On macOS/Linux

### 3. Install dependencies

pip install -r requirements.txt

### 4. Train the model (optional)
Run the training notebook in the notebooks/ directory to retrain and export your model.

### 5. Run the web app
streamlit run app.py
Then open your browser at http://localhost:8501

## Deployment
To deploy online, you can use Streamlit Community Cloud. It's free, quick to set up, and perfect for showcasing projects like this.

## Next Steps
Expand support for other attack types in CICIDS2017
Improve explanation modules with SHAP visualizations
Add a real-time detection prototype using packet capture tools
Package as a CLI tool or microservice for SOC use


Author
Ousmane Barry, PhD
Cybersecurity | AI/ML

