# GhostLens: Explainable AI for Threat Detection

GhostLens is an open-source tool that combines machine learning with explainable AI to detect and understand network threats in real time. It’s designed for cybersecurity analysts and engineers who need both accuracy and clarity when defending networks against modern attacks.

This project is built to showcase applied skills in ML, cybersecurity, and interpretability

## What It Does

- Detects anomalies in real network traffic using supervised ML
- Explains detection results using SHAP, LIME, and interpretable models
- Visualizes insights and feature importance for analysts
- Focuses on real-world attack types, including DDoS and port scans

## Dataset

This project uses the [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) dataset, specifically:

- `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`

The dataset contains labeled network traffic with multiple attack types, including Distributed Denial of Service (DDoS).

## Key Technologies

- Python 3
- Pandas, NumPy, Matplotlib
- Scikit-learn
- SHAP / LIME (for explainability)
- Jupyter Notebooks
- Git, GitHub

## Project Structure

ghostlens-xai-threat-detection/
├── data/ # Dataset files (CICIDS2017)
├── notebooks/ # Jupyter notebooks for exploration and modeling
├── models/ # Trained models (TBD)
├── reports/ # Visualizations and output analysis
├── ghostlens/ # Planned source code module
├── requirements.txt # Dependencies
└── README.md

## Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/ghostlens-xai-threat-detection.git
cd ghostlens-xai-threat-detection
Set up your environment

python -m venv venv
.\venv\Scripts\activate   # Windows
Install dependencies

pip install -r requirements.txt
Or, if requirements.txt doesn't exist yet:

pip install pandas numpy matplotlib scikit-learn shap lime
Launch Jupyter

jupyter notebook
Roadmap
 Load and clean dataset

 Analyze label distribution and feature types

 Handle missing values and duplicates

 Build baseline ML models (Random Forest, Isolation Forest)

 Add SHAP and LIME explanations

 Package into reusable components

 Build lightweight web app (Streamlit or Flask)

License


Author
Ousmane Barry, PhD
