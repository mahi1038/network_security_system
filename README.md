# 🔐 Online Security System

This project predicts whether a website is **safe** or **phishing/malicious**, using a set of well-known features commonly used in phishing detection systems. It is a **classification problem** built with a robust data pipeline, feature validation, and multiple machine learning models.

---

## 📊 Problem Statement

Cybersecurity threats like phishing attacks are increasingly prevalent. This system leverages **categorical features** derived from URLs and website behavior to **classify websites as safe or unsafe**.

The dataset used in this project is sourced from **Kaggle** and contains a variety of features such as IP address usage, URL length, HTTPS presence, domain registration, traffic ranking, and more.

---

## 🚀 Features Used

| Feature Name               | Description |
|---------------------------|-------------|
| `having_IP_Address`       | Uses IP instead of domain name |
| `URL_Length`              | Length of the full URL |
| `Shortining_Service`      | Uses URL shorteners like bit.ly |
| `having_At_Symbol`        | Presence of "@" in the URL |
| `double_slash_redirecting`| Use of `//` for redirection |
| `Prefix_Suffix`           | Hyphen in domain name |
| `having_Sub_Domain`       | Number of subdomains |
| `SSLfinal_State`          | Validity of SSL certificate |
| `Domain_registeration_length` | Length of domain registration |
| `Favicon`                 | Favicon loaded from external source |
| `port`                    | Use of non-standard ports |
| `HTTPS_token`            | Misleading "https" in domain |
| `Request_URL`             | External objects in URL |
| `URL_of_Anchor`           | Anchor tags leading to other domains |
| `Links_in_tags`           | Meta/script/link tag links |
| `SFH`                     | Form handler behavior |
| `Submitting_to_email`     | Form submits to email address |
| `Abnormal_URL`            | URL differs from page source |
| `Redirect`                | Number of redirections |
| `on_mouseover`            | Changes on mouse hover |
| `RightClick`              | Right click disabled |
| `popUpWidnow`             | Presence of pop-ups |
| `Iframe`                  | Use of invisible iframes |
| `age_of_domain`           | Age of the domain |
| `DNSRecord`               | Availability of DNS info |
| `web_traffic`             | Site traffic rank |
| `Page_Rank`               | Google's page ranking |
| `Google_Index`            | Indexed by Google or not |
| `Links_pointing_to_page`  | Inbound links to the page |
| `Statistical_report`      | Reported in phishing/malware lists |

---

## ⚙️ Tech Stack

Language: Python 3.8+

Backend:
  - FastAPI
  - Uvicorn (ASGI Server)

Machine Learning:
  - Scikit-learn
  - NumPy
  - Pandas

Experiment Tracking & Serialization:
  - MLflow
  - dill

Database:
  - MongoDB Atlas (Cloud NoSQL)
  - PyMongo

Configuration & Environment:
  - python-dotenv
  - certifi
  - pyaml

---

## 🧱 Project Architecture
MongoDB Atlas: Raw data is pushed to a NoSQL database hosted on the cloud.

Data Ingestion: Loads data from MongoDB and splits it into training and test sets.

Data Validation: Validates schema, checks for missing values, and generates data drift reports.

Data Transformation: Prepares the dataset for training by encoding features.

Model Training: Trains and evaluates models on the dataset.

Artifact Tracking: Each component generates and logs artifacts (train/test data, models, metrics).

---

## 🧪 Models Used

The following models are trained and compared based on classification metrics:

'Random Forest': RandomForestClassifier(verbose = 1)  

'Decision Tree': DecisionTreeClassifier()  

'Gradient Boosting': GradientBoostingClassifier()  

'Logistic Regression': LogisticRegression(verbose = 1)  

'AdaBoost': AdaBoostClassifier()

---

## 📦 Installation

 1. Clone the repository-
git clone https://github.com/your-username/online-security-system.git
cd online-security-system  


2. Create and activate a virtual environment (optional but recommended)  


3. Install the required dependencies-
pip install -r requirements.txt  


4. Environment Setup-
MONGODB_URL="your_mongodb_atlas_connection_string"  


5. run in terminal- 
uvicorn app:app --reload    


This will open the interactive FastAPI Swagger UI, where you can test the API endpoints for training and prediction.

---




