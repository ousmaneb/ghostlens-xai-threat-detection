# GhostLens: Explainable AI for Threat Detection

**GhostLens** is an open-source tool that leverages machine learning and explainable AI to detect and interpret network threats in real time. It's designed for cybersecurity analysts and engineers who need not only accurate threat detection but also clear insights into how decisions are made.

This project showcases applied skills in machine learning, cybersecurity, and model interpretability.

## What It Does

- Detects anomalies in real network traffic using supervised ML
- Explains detection results using SHAP, LIME, and interpretable models
- Visualizes insights and feature importance for better analysis
- Focuses on real-world attack types, such as DDoS and port scans

## Dataset

This project uses the [CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html) dataset, specifically:

- `Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`

The dataset includes labeled network traffic for multiple attack types, including Distributed Denial of Service (DDoS).

## Key Technologies

- Python 3
- Pandas, NumPy, Matplotlib
- Scikit-learn
- SHAP, LIME
- Jupyter Notebooks
- Git, GitHub

## Project Structure
ghostlens-xai-threat-detection/
├── data/ # Dataset files (CICIDS2017)
├── notebooks/ # Jupyter notebooks for exploration and modeling
├── models/ # Trained models (to be added)
├── reports/ # Visualizations and analysis
├── ghostlens/ # Core source code (planned)
├── requirements.txt # Dependencies
└── README.md

## Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/ghostlens-xai-threat-detection.git
cd ghostlens-xai-threat-detection

Set up your environment
python -m venv venv
.\venv\Scripts\activate   # For Windows

Install dependencies
pip install -r requirements.txt
If requirements.txt doesn't exist yet:
pip install pandas numpy matplotlib scikit-learn shap lime

Launch Jupyter Notebook
jupyter notebook

Roadmap
•	Load and clean dataset
•	Analyze label distribution and feature types
•	Handle missing values and duplicates
•	Build baseline ML models (Random Forest, Isolation Forest)
•	Add SHAP and LIME explanations
•	Package into reusable components
•	Build lightweight web app (Streamlit or Flask)
•	
License
This project is licensed under the MIT License.

Author
Ousmane Barry, PhD

