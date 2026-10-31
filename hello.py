import json
import datetime

def load_records():
    try:
        with open("records.json","r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.json","w",encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

while True:
    amount =input("花了多少钱？（直接回车就退出）")
    if amount == "":
        break
    category = input("花在哪？（比如 吃饭/交通/学习)")
    record = {
        "date" :datetime.date.today().isoformat(),
        "amount": float(amount),
        "category": category,
    }
    records = load_records()
    records.append(record)
    save_records(records)

    print("记好了，现在一共",len(records),"笔")