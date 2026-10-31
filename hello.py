import json
import datetime
import sys

def load_records():
    try:
        with open("records.json","r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.json","w",encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

def add_record():
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

def show_list():
    records = load_records()
    if not records:
        print("没有记录，先记一笔吧")
        return
    for i,r in enumerate(records,start=1):
        print(i, r["date"], r["category"], r["amount"], "元")

def show_report():
    records = load_records()
    month = datetime.date.today().strftime("%Y-%m")

    total = 0
    count = 0
    by_category = {}

    for r in records:
        if r["date"].startswith(month):
            total = total + r["amount"]
            count = count + 1

            cat = r["category"]
            if cat in by_category:
                by_category[cat] = by_category[cat] + r["amount"]
            else:
                by_category[cat] = r["amount"]

    print(month, "一共花了", total, "元")


    if count > 0:
        print("平均每笔", total / count, "元")
    else:
        print("这个月还没有记录")
        
    for cat, money in by_category.items():
        print("  ", cat, money, "元")
if len(sys.argv) > 1:
    command = sys.argv[1]
else:
    command = "add"

if command =="list":
    show_list()
elif command == "report":
    show_report()
else:
    add_record()

