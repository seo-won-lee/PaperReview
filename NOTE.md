# Notes

## Data Flow

```
metadata.yaml

generate_readme.py

README.md
```

README.md is auto-generated.
Do NOT edit README.md directly.

---

## Add New Paper

1. Add PDF to `reviews/`
2. Run:

`python scripts/add_paper.py`

3. Commit & Push

---

## Manual Edit

If metadata.yaml is **modified manually**:

    `python scripts/generate_readme.py`

Then commit & push.

---

## Source of Truth

`metadata.yaml`