# Word Template Filler Skill

Fill/edit Word `.docx` templates on Windows via **win32com COM automation** — preserves ALL formatting, images, underlines, page breaks, and table layout. Combines template-filling precision with general-purpose document automation.

## Why win32com instead of python-docx

| Approach | Format/Image Preservation | Requires Word |
|---|---|---|
| **win32com** (this skill) | ✅ 100% — Word does the work | ✅ Yes |
| `python-docx` | ❌ Drops images, corrupts complex formatting | ❌ No |
| `docxtpl` (Jinja) | ⚠️ Better than python-docx, still risks layout drift | ❌ No |

## Requirements

- **Windows** with **Microsoft Word** installed
- **pywin32** (`pip install pywin32`)
- Python 3.x

## Core Principles

1. **Read-only template**: Always `shutil.copy2()` before modifying. Never touch the original.
2. **Never `doc.Range().Text = ...`**: Destroys all formatting, images, tables. Use targeted Find/Replace instead.
3. **`InsertBefore` for blank fields**: Insert text before the para mark to preserve character-level formatting (underlined spaces).
4. **Use Word's built-in Find/Replace** for text cleanup — preserves all formatting.
5. **Page breaks are `\f` characters**. Never replace a paragraph that contains `\f`.
6. **Paragraph indices are 1-based** in COM. Cell paragraph indices are per-cell.

## Techniques

### 1. Cover Field Filling (Preserve Underline Lines)

Templates often use **underlined spaces** (`空格 + underline=1`) for fill-in lines. Insert the value **before** the spaces:

```python
def fill_cover_field(doc, label_text, value):
    for p in doc.Paragraphs:
        txt = p.Range.Text
        if txt.startswith(label_text):
            colon_pos = txt.find('：')
            if colon_pos > 0:
                rng = p.Range.Duplicate
                insert_at = rng.Start + colon_pos + 1
                after_rng = rng.Duplicate
                after_rng.Start = insert_at
                if value:
                    after_rng.InsertBefore(value)
            return True
    return False
```

### 2. Append Answer After Question in Cell

```python
def append_answer(cell, question_text, answer_text):
    rng = cell.Range.Duplicate
    f = rng.Find
    f.Text = question_text
    f.MatchCase = True
    f.Forward = True
    f.Wrap = 1  # wdFindStop
    if f.Execute():
        found = f.Parent
        found.MoveEnd(1, -1)  # exclude para mark
        found.Text = question_text + '\n' + answer_text
        return True
    return False
```

**⚠️ Always verify for double punctuation** (`。？`, `！？`) after using this.

### 3. Fill Table Sub-Items by Paragraph Index

For sub-tables within cells (序号/名称/功能), fill blank paragraphs by index:

```python
def insert_into_blank_para(cell, para_1b, text):
    paras = cell.Range.Paragraphs
    if para_1b <= paras.Count:
        p = paras(para_1b)
        p.Range.InsertBefore(text)
```

Always analyze cell structure first:

```python
def debug_cell(cell):
    paras = cell.Range.Paragraphs
    for i in range(paras.Count):
        txt = repr(paras(i+1).Range.Text)
        print(f"  Para {i}: {txt}")
```

### 4. Page Break Management

Add a page break before a heading:

```python
for p in doc.Paragraphs:
    if 'C2.转向架' in p.Range.Text:
        rng = p.Range.Duplicate
        rng.Collapse(1)  # start of range
        rng.InsertBefore('\f')
        break
```

### 5. Find/Replace (Preserves Formatting)

```python
def find_replace(doc, find_text, replace_text):
    rng = doc.Range()
    f = rng.Find
    f.Text = find_text
    f.MatchCase = True
    f.Forward = True
    f.Wrap = 2  # wdFindContinue
    f.Replacement.Text = replace_text
    f.Execute(Replace=2)  # wdReplaceAll
```

### 6. Insert Text at Start/End of Document

```python
def insert_at(doc, text, where='end'):
    rng = doc.Range()
    if where == 'start':
        rng.Collapse(1)
    else:
        rng.Collapse(0)
    rng.InsertBefore(text + '\n')
```

### 7. Set Header/Footer Text

```python
def set_header_footer(doc, header_text='', footer_text=''):
    for section in doc.Sections:
        if header_text:
            header = section.Headers(1)
            header.Range.Text = header_text
        if footer_text:
            footer = section.Footers(1)
            footer.Range.Text = footer_text
```

### 8. Add/Replace Image at End of Document

```python
def add_image(doc, image_path, width=100):
    rng = doc.Range()
    rng.Collapse(0)
    inline_shape = rng.InlineShapes.AddPicture(image_path)
    inline_shape.Width = width
    inline_shape.Height = width * 0.75
```

### 9. Merge Multiple Documents

```python
def merge_docs(input_paths, output_path):
    merged = word.Documents.Add()
    for path in input_paths:
        merged.Range().InsertFile(path)
    merged.SaveAs(output_path)
    merged.Close()
```

### 10. Export to PDF

```python
def export_to_pdf(doc_path, output_path):
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(output_path, FileFormat=17)  # wdFormatPDF
    doc.Close()
```

## Verification Checklist

- Cover: underlined spaces preserved
- Page breaks: `\f` characters at correct positions
- No double punctuation: `。？`, `！？` patterns
- Table content: verify specific cells
- Content additions didn't shift page breaks

## Debugging Tips

- Kill `WINWORD.EXE` between runs: `taskkill /f /im WINWORD.EXE`
- Clean up output file between runs
- Use `.Duplicate` on ranges to avoid mutation side-effects
- Word COM is 1-based; always verify indices

## Critical Warnings

| Don't Do | Why |
|---|---|
| `doc.Range().Text = ...` | Destroys ALL formatting, images, tables |
| Replace paragraph containing `\f` | Loses page break |
| `python-docx` to save modified template | Loses images, complex formatting |
| `\n` in Word Find patterns | Word uses `\r` (chr 13) for paragraph marks |
| Blindly replace cover paragraph text | Destroys underlined spaces |
| Forget to verify after `append_answer` | Leaves extra `？` behind |
