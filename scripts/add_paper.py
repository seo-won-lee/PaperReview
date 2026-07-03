# ==========================================
# Add new paper under "papers:"
#
# title: 
# year: 
# venue: 
# url: 
# read_date: 
# keywords: 
# review: reviews/
# ==========================================
import subprocess
from pathlib import Path
import yaml
from datetime import date

ROOT = Path(__file__).parent.parent
METADATA_FILE = ROOT / "metadata.yaml"

# import metadata.yaml 
if METADATA_FILE.exists():
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
else:
    data = {}

data.setdefault("papers", [])

print("\n=== Add New Paper ===\n")

title = input("Title: ").strip()
year = int(input("Year: ").strip())
venue = input("Venue: ").strip()
url = input("URL: ").strip()

keywords_input = input(
    "Keywords (comma separated): "
).strip()

pdf_name = input(
    "PDF filename (e.g. cosmos3.pdf): "
).strip()

read_date = input(
    f"Read date [default={date.today()}]: "
).strip()

if not read_date:
    read_date = str(date.today())

keywords = [
    k.strip()
    for k in keywords_input.split(",")
    if k.strip()
]

paper = {
    "title": title,
    "year": year,
    "venue": venue,
    "url": url,
    "read_date": read_date,
    "keywords": keywords,
    "review": f"reviews/{pdf_name}"
}

# duplication check
existing_idx = None

for idx, p in enumerate(data["papers"]):
    if p.get("title", "").lower() == title.lower():
        existing_idx = idx
        break

# add paper info    
if existing_idx is not None:
    data["papers"][existing_idx] = paper
    print(f"\n🔄 Updated existing paper: {title}")
else:
    data["papers"].append(paper)
    print(f"\n➕ Added new paper: {title}")
    
with open(METADATA_FILE, "w", encoding="utf-8") as f:
    yaml.dump(
        data,
        f,
        allow_unicode=True,
        sort_keys=False
    )

# generate README.md
subprocess.run(
    ["python", "scripts/generate_readme.py"]
)