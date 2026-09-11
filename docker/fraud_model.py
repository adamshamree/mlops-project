# Simple fraud detection model
def predict_fraud(transaction):
    amount = transaction.get("amount", 0)
    is_foreign = transaction.get("foreign", False)
    hour = transaction.get("hour", 12)
    score = 0
    if amount > 5000: score += 2
    if is_foreign: score += 2
    if hour < 6 or hour > 23: score += 1
    return {"fraud": score >= 3, "score": score}

if __name__ == "__main__":
    test = {"amount": 8000, "foreign": True, "hour": 2}
    print(predict_fraud(test))
