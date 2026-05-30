i# Processing Instructions for Dictionary JSON Files

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
- Always capitalize the first letter of every English sentence — no need to confirm this with the user, just fix it silently
- Do not correct punctuation like dots, commas, and other similar signs
- If a Farsi word appears in parentheses inside an English sentence (e.g., "(لوز)"), it is a pronunciation guide added intentionally — do NOT remove or change it
- Some sentences may be intentional quotes or cultural references from movies/TV series — do not correct their grammar as it may be stylistic on purpose

## Progress
- Next batch to process: ids 3101–3200
- When confirming each change, give 4 options as selectable choices (not numbered): "Correct it" (apply the fix), "Correct it with desc" (apply the fix + add a desc field explaining the reason), "Don't touch it" (keep original), or "Give my opinion" (user types their preferred version) — user picks from the choice UI, no need to type a number
- After each batch, save the changes to the file before moving to the next batch
- Do NOT create git commits — the user handles all commits manually
- Any new advice or instructions from the user should be added here in INSTRUCTIONS.md
- After every step taken, update the "Next batch to process" line to reflect what's coming next

