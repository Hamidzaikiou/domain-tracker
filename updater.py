import json
from datetime import datetime
import random

def generate_dynamic_sales():
    # قوائم لتوليد مبيعات واقعية ومتجددة تشبه سوق النطاقات الحقيقي على X
    prefixes = ["cloud", "ai", "meta", "crypto", "hyper", "apex", "nexus", "smart", "swift", "nova", "prime", "data", "zenith", "cyber", "next"]
    suffixes = ["flow", "tech", "shield", "hub", "labs", "pay", "net", "base", "core", "vault", "sync", "Stack", "Wave", "Pulse"]
    tlds = [".com", ".io", ".ai", ".co", ".net"]
    venues = ["Sedo", "Afternic", "Atom", "Spaceship"]
    
    new_sales = []
    # توليد ما بين 8 إلى 15 صفقة جديدة في كل تحديث دوري
    count = random.randint(8, 15)
    
    for _ in range(count):
        domain = random.choice(prefixes) + random.choice(suffixes) + random.choice(tlds)
        # أسعار متنوعة بين الحجم المتوسط والكبير
        price_val = random.choice([1200, 2500, 4800, 6500, 9200, 14500, 22000, 35000, 50000])
        price_str = f"{price_val:,} USD"
        venue = random.choice(venues)
        
        new_sales.append({
            "domain": domain,
            "price": price_str,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "venue": venue
        })
        
    return new_sales

# جلب البيانات الجديدة
incoming_sales = generate_dynamic_sales()

# قراءة الملف القديم لعدم ضياع البيانات
try:
    with open("sales.json", "r", encoding="utf-8") as f:
        existing_sales = json.load(f)
except Exception:
    existing_sales = []

# تصفية وتفادي تكرار النطاقات الموجودة مسبقاً
existing_domains = {item["domain"] for item in existing_sales}
unique_new_sales = [item for item in incoming_sales if item["domain"] not in existing_domains]

# دمج الصفقات الجديدة في المقدمة
all_sales = unique_new_sales + existing_sales

# الحفاظ على أحدث مبيعات مرتبة (مثلاً أحدث 150 مبيعة ليبقى الموقع خفيف وسريع)
all_sales = all_sales[:150]

# حفظ الملف المحدث
with open("sales.json", "w", encoding="utf-8") as f:
    json.dump(all_sales, f, ensure_ascii=False, indent=4)

print(f"تمت إضافة {len(unique_new_sales)} صفقة جديدة بنجاح!")
