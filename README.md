Built for the GrowthLink Data Science Internship Program.
# credit-card-fraud-detection-
## 📁 Project Structure

```
credit-card-fraud-detection/
├── data/
│   └── creditcard.csv              # Dataset from Kaggle
├── src/
│   ├── preprocess.py              # Data cleaning, scaling, balancing
│   ├── train_model.py             # Training using Random Forest
│   ├── evaluate.py                # Confusion matrix & classification report
├── main.py                        # Runs the pipeline
├── README.md                      # This file
└── requirements.txt               # Dependencies
```

---

## 📊 Dataset

- Download it from: [Kaggle Dataset Link](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Contains 284,807 transactions with 492 frauds (highly imbalanced)

---

## ⚙️ How to Run the Project

```bash
# Step 1: Clone the repo or download project
# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Make sure dataset is in data/creditcard.csv

# Step 4: Run the main script
python main.py
```

---

## 🧪 Output Example

When you run it, you’ll see output like:

```
Classification Report:
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     56863
           1       0.91      0.84      0.87        99

    accuracy                           1.00     56962
   macro avg       0.96      0.92      0.94     56962
weighted avg       1.00      1.00      1.00     56962
```

And a confusion matrix plot with actual vs predicted labels.

---

## 📌 What You Learn

✅ Data cleaning & scaling  
✅ Handling imbalance using SMOTE  
✅ Building models using sklearn  
✅ Evaluating performance with F1, precision, recall

---



