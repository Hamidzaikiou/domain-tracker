import json
from datetime import datetime

# عينة متجددة تحاكي جلب أحدث المبيعات من Sedo, Afternic, Spaceship, Atom
new_sales = [
    {
        "domain": "hyperflow.ai",
        "price": "14,000 USD",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "venue": "Sedo"
    },
    {
        "domain": "brandboost.com",
        "price": "9,500 USD",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "venue": "Afternic"
    },
    {
        "domain": "orbit.io",
        "price": "6,800 USD",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "venue": "Spaceship"
    },
    {
        "domain": "nexusdomain.com",
        "price": "11,200 USD",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "venue": "Atom"
    }
]

# قراءة البيانات القديمة لدمجها مع الجديدة
try:
    with open("sales.json", "r", encoding="utf-8") as f:
        existing_sales = json.load(f)
except Exception:
    existing_sales = []

# دمج المبيعات الجديدة مع القديمة
all_sales = new_sales + existing_sales

# حفظ القائمة المحدثة
with open("sales.json", "w", encoding="utf-8") as f:
    json.dump(all_sales, f, ensure_ascii=False, indent=4)

print("تم تحديث ملف المبيعات بنجاح!")
