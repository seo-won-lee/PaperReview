from pathlib import Path
import yaml

ROOT = Path(__file__).parent.parent

METADATA_FILE = ROOT / "metadata.yaml"
README_FILE = ROOT / "README.md"

# load metadata
with open(METADATA_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f) or {}

papers = data.get("papers", [])

# sort by read_date
papers.sort(
    key=lambda x: x.get("read_date", ""),
    reverse=True
)

lines = []

lines.append("# Paper Reviews\n")

lines.append(
    "| Title | Venue |Keywords | Review |"
)
lines.append(
    "|---------|---------|---------|---------|"
)

for paper in papers:

    title = paper.get("title", "")
    venue = paper.get("venue", "")
    year = paper.get("year", "")
    url = paper.get("url", "")
    read_date = paper.get("read_date", "")

    keywords = ", ".join(
        paper.get("keywords", [])
    )

    review = paper.get("review", "")

    title_md = f"[{title}]({url})"
    review_md = f"[PDF]({review})"

    lines.append(
        f"| {title_md} | {venue} {year} | "
        f" {keywords} | {review_md} |"
    )

README_FILE.write_text(
    "\n".join(lines),
    encoding="utf-8"
)

print(
    f"README generated successfully "
    f"({len(papers)} papers)"
)