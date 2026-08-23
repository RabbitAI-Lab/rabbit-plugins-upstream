# 归墟 Hub → PDF Generation Pipeline

> Technique extracted from 2026-05-31 session: Still病指南文章审核

## Problem

归墟 Hub (`http://192.168.3.82:8765`) is a Vue SPA. Running `google-chrome --headless --print-to-pdf` directly on a note URL captures the dashboard/homepage, not the rendered note content. CDN resources (marked.js) may also fail due to SSL handshake errors in headless mode.

## Solution: API Fetch → Self-Contained HTML → PDF

### Step 1: Fetch note content via API

```python
import json, subprocess
result = subprocess.run(
    ['curl', '-s', 'http://192.168.3.82:8765/api/notes/note_XXX'],
    capture_output=True, text=True, timeout=15
)
data = json.loads(result.stdout)
note = data.get('data', data)
content = note.get('content', '')  # Markdown content
version = note.get('version')      # Needed for PUT
```

### Step 2: Embed SVG figures as base64 data URIs

If the note references SVG figures stored locally (e.g. `/home/ubsea/Down-PDF/Review/figures/`):

```python
import base64
with open(svg_path, 'r') as f:
    svg_content = f.read()
svg_b64 = base64.b64encode(svg_content.encode()).decode()
img_tag = f'<img src="data:image/svg+xml;base64,{svg_b64}" style="max-width:100%; height:auto;" />'
# Insert after the figure description text in markdown
```

### Step 3: Build self-contained HTML

Key: **inline marked.js**, don't use CDN.

```python
content_js = json.dumps(content, ensure_ascii=False)  # Safe JS string

html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<script>""" + marked_js_source + """</script>
<style>
  /* A4-optimized print styles */
  @page { size: A4; margin: 20mm 18mm; }
  body { font-family: "Noto Sans SC", sans-serif; max-width: 760px; 
         margin: 0 auto; line-height: 1.85; font-size: 13.5px; }
  /* ... table, code, blockquote styles ... */
</style>
</head>
<body>
<div id="content"></div>
<script>
document.getElementById('content').innerHTML = marked.parse(""" + content_js + """);
</script>
</body>
</html>"""
```

### Step 4: Generate PDF

```bash
google-chrome --headless --disable-gpu --no-sandbox \
  --virtual-time-budget=5000 \
  --print-to-pdf=/tmp/output.pdf \
  --no-margins \
  file:///tmp/article.html
```

- `--virtual-time-budget=5000`: Wait 5s for JS to render
- `--no-sandbox`: Required on PVE Ubuntu / container environments
- `file://` protocol: Avoids SSL issues entirely

### Step 5: Verify PDF

```python
import fitz
doc = fitz.open('/tmp/output.pdf')
print(f'Pages: {len(doc)}')
text = doc[0].get_text()[:200]  # Check first page has real content
doc.close()
```

## 归墟 PUT API Rules

```
PUT /api/notes/{id}
Body: { "version": <current_version>, "content": "..." }
```

- **Must pass current version number** — if stale, returns `VERSION_CONFLICT`
- After successful PUT, version auto-increments
- If you accidentally PUT garbage (test content), version increments anyway — use the new version for the real update
- **Append, don't delete**: Edits should modify existing content in-place, not replace the entire note

## Environment

- Chrome: `/usr/bin/google-chrome` (requires `--no-sandbox` on this system)
- 归墟: `http://192.168.3.82:8765`
- marked.js: Download locally to `/tmp/marked.min.js` first via `curl -sL https://cdn.jsdelivr.net/npm/marked/marked.min.js`
