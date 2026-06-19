\# 🌧️ Rainfall Prediction using Machine Learning



<p align="center">

&#x20; <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python"/>

&#x20; <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white"/>

&#x20; <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white"/>

&#x20; <img src="https://img.shields.io/badge/RandomForest-74%25\_Accuracy-green?style=for-the-badge"/>

</p>



<p align="center">

&#x20; An end-to-end Machine Learning project that predicts rainfall based on weather parameters — complete with EDA, model training, hyperparameter tuning, and a live interactive Streamlit web app.

</p>



\---



\## 🚀 Live App



Run locally with one command:

```bash

streamlit run app.py

```



\---



\## ✨ Features



| Feature | Description |

|--------|-------------|

| 🧹 \*\*Data Preprocessing\*\* | Missing value handling, feature cleaning |

| 📊 \*\*EDA\*\* | Histograms, boxplots, correlation heatmaps |

| ⚖️ \*\*Class Balancing\*\* | Downsampling for imbalanced rainfall data |

| 🌲 \*\*Random Forest Model\*\* | Tuned using GridSearchCV (216 combinations) |

| ✅ \*\*\~74% Accuracy\*\* | Validated with 5-fold cross-validation |

| 🖥️ \*\*Streamlit Web App\*\* | Interactive UI for real-time predictions |

| 💾 \*\*Model Persistence\*\* | Saved using Pickle for reuse |



\---



\## 🛠️ Technologies Used



```

Language       →  Python

Data Handling  →  Pandas, NumPy

ML Framework   →  Scikit-learn

Visualization  →  Matplotlib, Seaborn

Web App        →  Streamlit

Model Storage  →  Pickle

Development    →  Google Colab

```



\---



\## 📊 Model Performance



| Metric | Score |

|--------|-------|

| Test Accuracy | \~74% |

| F1 Score | 0.75 |

| Cross-Validation | 5-Fold |

| Algorithm | Random Forest Classifier |

| Hyperparameter Tuning | GridSearchCV (216 combinations) |



\---



\## 📁 Project Structure



```

Rainfall-Prediction/

│

├── Rainfall\_Prediction.ipynb       # Full ML pipeline notebook

├── app.py                          # Streamlit web application

├── rainfall\_prediction\_model.pkl   # Trained Random Forest model

├── requirements.txt                # Python dependencies

└── README.md                       # Project documentation

```



\---



\## ▶️ How to Run



\### 1. Clone the Repository

```bash

git clone https://github.com/Shrinetsingh9648/Rainfall-Prediction.git

cd Rainfall-Prediction

```



\### 2. Create Virtual Environment

```bash

python -m venv .venv

.venv\\Scripts\\activate        # Windows

source .venv/bin/activate     # Mac/Linux

```



\### 3. Install Dependencies

```bash

pip install -r requirements.txt

```



\### 4. Run the Streamlit App

```bash

streamlit run app.py

```



\### 5. Use the App

Enter weather parameters (pressure, dew point, humidity, cloud cover, sunshine, wind direction, wind speed) and click \*\*Predict Rainfall\*\* to get instant results.



\---



\## 🧠 Model Pipeline



```

Raw Weather Data

&#x20;       ↓

Data Cleaning \& Missing Value Handling

&#x20;       ↓

Exploratory Data Analysis (EDA)

&#x20;       ↓

Feature Selection \& Class Balancing

&#x20;       ↓

Random Forest + GridSearchCV Tuning

&#x20;       ↓

Model Evaluation (Accuracy, F1-Score)

&#x20;       ↓

Pickle Model Export

&#x20;       ↓

Streamlit Web App for Predictions

```



\---



\## 🎯 Future Improvements



\- \[ ] Real-time weather API integration

\- \[ ] Deploy on Streamlit Cloud / Render

\- \[ ] Add more advanced models (XGBoost, Neural Networks)

\- \[ ] Location-based rainfall prediction



\---



\## 👨‍💻 Author



\*\*Shrinet Singh\*\*



\[!\[GitHub](https://img.shields.io/badge/GitHub-Shrinetsingh9648-black?style=flat\&logo=github)](https://github.com/Shrinetsingh9648)



\---



<p align="center">⭐ Star this repo if you found it useful!</p>



