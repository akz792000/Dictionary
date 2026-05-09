# Processing Instructions for Dictionary JSON Files

## Target Files
- File_0.json (and others as needed)

## Data Structure
Each entry has:
- `id`: unique number
- `fa`: Farsi sentence
- `en`: English sentence
- `groupCode`: group identifier (integer)

---

## Instructions
- Correct the `en` sentences based on advanced American English
- Don't over-correct — only fix clear mistakes
- Do not correct punctuation like dots, commas, and other similar signs
- If a Farsi word appears in parentheses inside an English sentence (e.g., "(لوز)"), it is a pronunciation guide added intentionally — do NOT remove or change it
- Some sentences may be intentional quotes or cultural references from movies/TV series — do not correct their grammar as it may be stylistic on purpose

## Processing Strategy
- When confirming each change, give 4 options: "Correct it" (apply the fix), "Correct it with desc" (apply the fix + add a desc field explaining the reason), "Don't touch it" (keep original), or "Give my opinion" (user types their preferred version)
- After each batch, save the changes to the file before moving to the next batch
- Any new advice or instructions from the user should be added here in INSTRUCTIONS.md

