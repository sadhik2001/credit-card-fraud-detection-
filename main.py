# main.py
from src.preprocess import load_and_preprocess
from src.train_model import train_model
from src.evaluate import evaluate_model

def main():
    # Step 1: Load and preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess()

    # Step 2: Train model
    model = train_model(X_train, y_train)

    # Step 3: Evaluate model
    evaluate_model(model, X_test, y_test)

if __name__ == '__main__':
    main()
