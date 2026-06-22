# Processing Instructions for Dictionary JSON Files

---

## Task 1 — English Sentence Corrections (`fa_en.json` via `File_0.json`)

### Target File
- `File_0.json`

### Data Structure
Each entry has:
- `id`: unique number
- `fa`: Farsi sentence
- `en`: English sentence
- `groupCode`: group identifier (integer)

### Instructions
- Correct the `en` sentences based on advanced American English
- Always capitalize the first letter of every English sentence — no need to confirm this with the user, just fix it silently
- Do not correct punctuation like dots, commas, and other similar signs
- If a Farsi word appears in parentheses inside an English sentence (e.g., "(لوز)"), it is a pronunciation guide added intentionally — do NOT remove or change it
- Some sentences may be intentional quotes or cultural references from movies/TV series — do not correct their grammar as it may be stylistic on purpose

### Progress
- Next batch to process: ids 3201–3300
- When confirming each change, give 4 options as selectable choices (not numbered): "Correct it" (apply the fix), "Correct it with desc" (apply the fix + add a desc field explaining the reason), "Don't touch it" (keep original), or "Give my opinion" (user types their preferred version) — user picks from the choice UI, no need to type a number
- After each batch, save the changes to the file before moving to the next batch
- Do NOT create git commits — the user handles all commits manually
- Any new advice or instructions from the user should be added here in INSTRUCTIONS.md
- After every step taken, update the "Next batch to process" line to reflect what's coming next

---

## Task 2 — German Verb Cards: Simple Sentence Conjugations (`en_de_verbs.json`)

### Goal
Replace bare conjugation lists with **simple example sentences** so learners see each form in a real (minimal) context.

### Target File
- `en_de_verbs.json` (305 entries, ids 20001–20305)

### Data Structure
Each entry has:
- `id`: unique number
- `en`: English meaning (e.g., `"Turn (off)"`)
- `de`: German conjugation table in Markdown (Präsens, Präteritum, Perfekt × 6 subjects)

### Current Format (BEFORE)
```
**Abbiegen**

**Präsens**
ich biege ab
du biegst ab
er/sie/es biegt ab
wir biegen ab
ihr biegt ab
sie/Sie biegen ab

**Präteritum**
ich bog ab
...

**Perfekt**
ich habe abgebogen
...
```

### Target Format (AFTER)
```
**Abbiegen**

**Präsens**
Ich biege an der Ecke ab.
Du biegst nach links ab.
Er biegt in die Straße ab.
Wir biegen am Kreisverkehr ab.
Ihr biegt an der Ampel ab.
Sie biegen nach rechts ab.

**Präteritum**
Ich bog gestern falsch ab.
Du bogst an der Kreuzung ab.
Er bog zu früh ab.
Wir bogen nach Süden ab.
Ihr bogt am Schild ab.
Sie bogen in die Gasse ab.

**Perfekt**
Ich habe an der Ecke abgebogen.
Du hast nach links abgebogen.
Er hat in die Straße abgebogen.
Wir haben am Kreisverkehr abgebogen.
Ihr habt an der Ampel abgebogen.
Sie haben nach rechts abgebogen.
```

### Rules
1. **One simple sentence per conjugation line** — replace "ich biege ab" with a complete, minimal German sentence using that exact conjugated form
2. **Keep it simple** — A1/A2 vocabulary, everyday situations. The sentence should be as short and natural as possible (5–10 words max)
3. **Use varied subjects** — for `er/sie/es`, pick ONE (e.g., "Er", "Sie", or "Es") depending on what sounds most natural for the sentence. Do NOT write "Er/sie/es" in the sentence
4. **Keep the Markdown structure intact** — bold verb title, bold tense headings (Präsens, Präteritum, Perfekt), two-space trailing linebreaks for the app's Markdown renderer
5. **Capitalize** the first letter of every sentence
6. **Each sentence within a tense should use a different context/object** so the card feels varied, not repetitive
7. **Do NOT change the `en` field** — only modify `de`
8. **Keep the `id` field unchanged**
9. **Ensure the verb is used correctly** — separable prefixes must separate in Präsens/Präteritum main clauses, Perfekt uses the combined participle

### Batch Processing
- Process **20 verbs per batch** (e.g., ids 20001–20020, then 20021–20040, …)
- For each verb, show the **before** (current `de`) and **after** (proposed `de`) side by side
- Give 3 options as selectable choices: "Apply" (save the new version), "Skip" (keep original), or "Give my opinion" (user provides feedback)
- After each batch, save changes to `en_de_verbs.json` before moving to the next batch
- Do NOT create git commits — the user handles all commits manually
- After every batch, update the progress line below

### Progress
- Next batch to process: ids 20021–20040

