# 🚩 Drug Integration (DI) Flag Detection

## 📖 Project Overview

This project is a Natural Language Processing (NLP) application that detects **DI Flag issues** by analyzing textual descriptions. The system preprocesses raw text, extracts meaningful features using NLP techniques, and classifies whether a description contains a DI Flag.

The project demonstrates an end-to-end Machine Learning workflow, from text preprocessing and feature engineering to model training, evaluation, and deployment.

---

## 🎯 Problem Statement

Organizations often need to identify potential DI Flag issues from large volumes of textual descriptions. Manual analysis is time-consuming and prone to inconsistencies.

This project automates the detection process using Machine Learning and NLP, enabling faster and more consistent identification of DI Flag issues.

---

## 📂 Dataset

The project uses a labeled dataset containing textual descriptions and their corresponding DI Flag labels.

The dataset is preprocessed before model training to improve prediction accuracy.

---

## 🚀 Features

* Automated DI Flag detection
* Advanced text preprocessing pipeline
* TF-IDF and Bag of Words feature extraction
* Machine Learning-based text classification
* Interactive Streamlit application for predictions

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* TF-IDF Vectorizer
* Bag of Words
* Streamlit
* Pickle

---

## 🤖 Machine Learning Pipeline

### Text Preprocessing

* HTML tag removal
* Hashtag removal
* Special character removal
* Numeric value removal
* Tokenization
* Stop-word removal
* Stemming
* Lemmatization

### Feature Engineering

* Bag of Words (BoW)
* TF-IDF Vectorization

### Model Evaluation

* Confusion Matrix
* Accuracy Score
* Validation Testing

The trained model was validated for **30 days** before deployment.

---

## 📁 Project Structure

```text
di_flag_project/
│
├── app.py
├── di_flag_dataset.csv
├── di_flag_model.pkl
├── dl_flag.ipynb
├── tfidf.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Sowmya-lanka-28/di_flag_project.git
```

Navigate to the project folder

```bash
cd di_flag_project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 💻 How It Works

1. The user enters a textual description.
2. The text is cleaned and preprocessed.
3. TF-IDF converts the processed text into numerical features.
4. The trained Machine Learning model predicts whether the description contains a DI Flag.
5. The prediction is displayed through the Streamlit interface.

---

## 📊 Machine Learning Workflow

* Data Collection
* Data Cleaning
* Text Preprocessing
* Feature Extraction (BoW & TF-IDF)
* Model Training
* Model Evaluation
* Validation Testing
* Streamlit Deployment

---

## 🔮 Future Improvements

* Fine-tune classification models for improved accuracy
* Integrate Transformer-based models such as BERT
* Add confidence scores for predictions
* Deploy the application on Streamlit Community Cloud
* Expand support for multiple issue categories

---


## 👩‍💻 Author

**Sowmya Lanka**

**Data Scientist | Generative AI Engineer | Machine Learning Engineer**

* GitHub: https://github.com/Sowmya-lanka-28
* LinkedIn: https://linkedin.com/in/sowmya-lanka-323806400
