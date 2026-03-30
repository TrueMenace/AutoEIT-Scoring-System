# AutoEIT: Automated Scoring for Elicited Imitation Task

## 📌 Overview

This project implements an automated scoring system for the **Elicited Imitation Task (EIT)** as part of the **HumanAI AutoEIT GSoC project**.

The system evaluates learner transcriptions against prompt sentences and assigns a score (0–4) based on meaning preservation and accuracy, following a rubric-based approach.

---

## 🎯 Key Features

- ✅ Multi-sheet Excel processing
- ✅ Text preprocessing and normalization
- ✅ Feature engineering:
  - Word overlap
  - Missing words
  - Length ratio
  - Sequence similarity
- ✅ Semantic similarity using Sentence Transformers
- ✅ Hybrid rule-based scoring engine
- ✅ Explainable AI (score + reasoning)
- ✅ Automated Excel output generation

---

## 🧠 Scoring Logic

The system combines:

- **Lexical similarity** (word overlap, missing words)
- **Structural similarity** (sequence similarity)
- **Semantic similarity** (Sentence Transformers)

Final scores are determined primarily by semantic similarity and aligned with the EIT scoring rubric:

| Score | Description |
|------|------------|
| 4 | Exact or near-exact reproduction |
| 3 | Meaning preserved with minor differences |
| 2 | Partial meaning captured |
| 1 | Limited meaning retained |
| 0 | Incorrect or unrelated response |

---

## 📂 Project Structure
AutoEIT/
├── data/
├── outputs/
├── src/
├── requirements.txt
├── README.md

---

## ⚙️ Installation

1. Create virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

2. Create virtual environment:
```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the pipeline:
```
python src/main.py
```
Output file will be generated:
```
outputs/scored_output.xlsx
```

---

## 📊 Output

Each sheet contains:

- Original stimulus
- Learner response
- Predicted score
- Explanation of score

---

## 🚀 Future Improvements

- Model fine-tuning on EIT-specific data
- Calibration with human-rated scores
- Error-type classification (grammar, omission, substitution)
- Web interface for real-time scoring

---

## 👨‍💻 Author
Ansh Shrivastava
GSoC 2026 Applicant — HumanAI AutoEIT