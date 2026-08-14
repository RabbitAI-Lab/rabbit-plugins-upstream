# Anki Import Guide

Flashcard Forge outputs CSV files designed for direct import into
[Anki](https://apps.ankiweb.net/). This guide walks through the import process
for both Q&A (Basic) and cloze card types.

## CSV Format

### Q&A CSV (Basic cards)

```
Front;Back
"What is photosynthesis?";"The process by which plants convert light into chemical energy"
"Mitochondria";"The powerhouse of the cell, responsible for ATP production"
```

- **Separator**: semicolon (`;`)
- **Header row**: `Front;Back`
- **Fields are quoted** to handle commas and newlines within card text

### Cloze CSV (Cloze cards)

```
Text;Extra
"The powerhouse of the cell is the {{c1::mitochondria}}";""
"DNA stands for {{c1::deoxyribonucleic acid}}";""
```

- **Separator**: semicolon (`;`)
- **Header row**: `Text;Extra`
- Cloze deletions use `{{c1::...}}` syntax
- The `Extra` field is for additional context (often empty)

## Importing Q&A Cards (Basic)

1. **Open Anki** and select or create a deck.
2. Go to **File → Import...** (or press `Ctrl+I` / `Cmd+I`).
3. Select your `.csv` file.
4. In the import dialog:
   - **Type**: Basic
   - **Deck**: choose your target deck
   - **Field separator**: semicolon (`;`) — Anki usually auto-detects
5. Verify the field mapping: column 1 → Front, column 2 → Back.
6. Click **Import**.

### Importing Cloze Cards

1. **Ensure you have a Cloze note type.** Anki includes one by default. If you
   don't see it, go to Tools → Manage Note Types → Add → Cloze.
2. Go to **File → Import...**
3. Select your cloze `.csv` file.
4. In the import dialog:
   - **Type**: Cloze
   - **Deck**: choose your target deck
   - **Field separator**: semicolon (`;`)
5. Verify the field mapping: column 1 → Text, column 2 → Extra.
6. Click **Import**.

> **Important:** Cloze cards with no `{{c1::...}}` deletion will fail to import.
> Flashcard Forge guarantees at least one cloze per card.

## Common Import Issues

### "The first field of this note type must be unique"

This happens if Anki detects duplicate front text. Options:

- Enable "Allow HTML in fields" is **not** the fix — instead, update existing
  cards on import.
- Or, pre-deduplicate your CSV. Flashcard Forge deduplicates within a single
  run; if you're merging multiple runs, dedup manually.

### Garbled characters

Ensure the CSV is UTF-8 encoded. Flashcard Forge always writes UTF-8. If you
opened and re-saved the file in Excel, it may have changed the encoding —
re-export from the script instead.

### Wrong delimiter detected

If Anki shows all data in one column, the delimiter wasn't auto-detected. In
the import dialog, manually set the field separator to semicolon.

### Cloze cards show as blank

The note type must be **Cloze**, not Basic. If you imported cloze CSV as Basic
cards, delete them and re-import with the correct type.

## Bulk Import Tips

- **Large decks**: Import in batches of 200-500 cards to avoid performance
  issues.
- **Tags**: Add tags during import (e.g., `biology`, `chapter-3`) for easier
  filtering.
- **Review after import**: Always review 10-20 cards to catch extraction errors
  before committing to a study schedule.

## Verification Checklist

- [ ] CSV opens correctly in a plain text editor
- [ ] Fields are semicolon-separated and quoted
- [ ] Cloze CSV contains `{{c1::...}}` syntax
- [ ] Note type matches card mode (Basic for qa, Cloze for cloze)
- [ ] Imported cards render correctly in Anki browser
- [ ] Sample review session shows correct front/back
