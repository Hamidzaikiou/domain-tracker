import json
from datetime import datetime, timedelta
import random

def generate_dynamic_sales():
    prefixes = ["cloud", "ai", "meta", "crypto", "hyper", "apex", "nexus", "smart", "swift", "nova", "prime", "data", "zenith", "cyber", "next", "pulse", "block", "vision", "quantum", "alpha", "zen", "vector", "orbit", "peak", "stellar", "flux", "synth", "vertex"]
    suffixes = ["flow", "tech", "shield", "hub", "labs", "pay", "net", "base", "core", "vault", "sync", "stack", "wave", "pulse", "ify", "ly", "hq", "box", "lab", "ify", "point", "desk", "ware"]
    tlds = [".com", ".io", ".ai", ".co", ".net", ".org", ".dev"]
    venues = ["Sedo", "Afternic", "Atom", "Spaceship"]
    
    new_sales = []
    # توليد عدد كبير من الصفقات دفعة واحدة (ما بين 40 و 60 صفقة جديدة)
    count = random.randint(40, 60)
    
    for _ in range(count):
        domain = random.choice(prefixes) + random.choice(suffixes) + random.choice(tlds)
        price_val = random.choice([800, 1500, 2500, 4200, 6800, 9500, 12000, 18500, 27000, 35000, 48000, 65000])
        price_str = f"{price_val:,} USD"
        venue = random.choice(venues)
        
        days_ago = random.randint(0, 15)
        sale_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        
        new_sales.append({
            "domain": domain,
            "price": price_str,
            "date": sale_date,
            "venue": venue
        })
        
    return new_sales

# قراءة الملف القديم
try:
    with open("sales.json", "r", encoding="utf-8") as f:
        existing_sales = json.load(f)
except Exception:
    existing_sales = []

# توليد البيانات الجديدة
incoming_sales = generate_dynamic_sales()

# دمج الصفقات مع تفادي التكرار
existing_domains = {item["domain"] for item in existing_sales}
unique_new_sales = [item for item in incoming_sales if item["domain"] not in existing_domains]

all_sales = unique_new_sales + existing_sales

# الحفاظ على آخر 250 مبيعة في الملف باش يبقى الموقع خفيف وفي نفس الوقت يعمر بـ 100 في العرض
all_sales = all_sales[:250]

# حفظ الملف
with open("sales.json", "w", encoding="utf-8") as f:
    json.dump(all_sales, f, ensure_ascii=False, indent=4)

print(f"تمت إضافة {len(unique_new_sales)} صفقة جديدة بنجاح! الإجمالي: {len(all_sales)}")
