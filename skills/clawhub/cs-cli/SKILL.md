---
name: camscanner
description: "CamScanner document processing - an intelligent document conversion and processing platform and official CamScanner Skill. Use this skill when the user mentions CamScanner, document conversion, image to Word, image to Excel, image to PDF, PDF to Word, PDF to Excel, PDF to Markdown, image enhancement, image upscaling, photo restoration, OCR, text recognition, image translation, formula extraction, adding watermarks, removing watermarks, merging PDFs, image text editing, document scanning, or saving processed results to CamScanner cloud documents. Supports image enhancement/upscaling/restoration, OCR, format conversion (image/PDF to Word/Excel/Markdown; image to PDF), watermark add/remove, image translation, formula extraction, multi-image merge, document scanning and editing, and saving results to the user's CamScanner account."
metadata: {"homepage":"https://www.camscanner.com","version":"1.1.0","requires":{"bins":["camscanner-cli"],"cliHelp":"camscanner-cli --help"},"category":"productivity","keywords":["CamScanner","document conversion","image to Word","image to Excel","image to PDF","PDF to Word","PDF to Excel","PDF to Markdown","image enhancement","image upscaling","photo restoration","OCR","text recognition","image translation","formula extraction","watermark","remove watermark","merge PDF","merge Word","merge Excel","document scanning","image editing","cloud documents"],"file_types":["jpg","jpeg","png","pdf","txt","md"]}
---

# CamScanner CLI Skill Guide

The CamScanner CLI Skill provides a complete document processing toolkit through the `camscanner-cli` command-line tool and the CamScanner AI Tools API. It supports image enhancement, OCR, format conversion, watermarking, translation, restoration, merging, and related operations. Results can also be saved to the user's CamScanner account.

## Environment Setup

Before using this Skill for the first time in a session, the agent **must** complete the following decision flow. This only needs to run once per session.

**The agent must strictly follow this flow — skipping any step is prohibited:**

```
Step 1: camscanner-cli --version
         │
         ├─ Command exists (outputs version) → Step 2
         │
         └─ Command not found → [Windows?] Double-check with Test-Path ↓
                          │
                          ├─ Test-Path "$env:LOCALAPPDATA\camscanner-cli\camscanner-cli.exe" = True
                          │   → Refresh PATH → Step 2 (no install needed)
                          │
                          └─ False / Non-Windows → Run install script → Step 3 (skip upgrade)

Step 2: Run upgrade script
         │
         └─ Done → Step 3

Step 3: camscanner-cli auth status
         │
         ├─ Logged in → ✅ Environment ready, proceed with user task
         │
         └─ Not logged in / expired → Run camscanner-cli auth login → Verify → ✅
```

### Step 1. Check Installation

Run `camscanner-cli --version`:

- **Command exists** (outputs version) → Already installed, continue to Step 2
- **Command not found** (command not found / not recognized) → **On Windows, you must perform the double-check below first**. If confirmed not installed, run the install script. After installation, **skip directly to Step 3**.

**Windows double-check (mandatory)**:

`camscanner-cli --version` failing on Windows does not necessarily mean it is not installed — the PATH may not be refreshed or ConPTY may swallow output. **Before running the install script**, check whether the file exists:

```powershell
Test-Path "$env:LOCALAPPDATA\camscanner-cli\camscanner-cli.exe"
```

- Returns **True** → CLI is installed, just missing from PATH. Refresh PATH then continue to Step 2:
  ```powershell
  $env:PATH = "$env:LOCALAPPDATA\camscanner-cli;$env:PATH"
  ```
- Returns **False** → Confirmed not installed, run the install script → Step 3

| Platform | Install Command |
|----------|-----------------|
| Linux/macOS | `bash scripts/setup.sh` |
| Windows | `powershell -ExecutionPolicy Bypass -File scripts/setup.ps1` |

### Step 2. Version Upgrade Check (installed users only)

Run the upgrade script to check for a new version (the script handles detection internally; exits silently if no update is available; network failures do not block usage):

| Platform | Upgrade Command |
|----------|-----------------|
| Linux/macOS | `bash scripts/upgrade.sh` |
| Windows | `node scripts/upgrade.cjs` |
| Fallback (any platform) | `node scripts/upgrade.cjs` |

> The upgrade script updates both the CLI binary and Skill files (SKILL.md, references/, scripts/) to keep them in sync. On failure it auto-rolls back; manual rollback: `bash scripts/upgrade.sh --rollback` or `node scripts/upgrade.cjs --rollback`.

### Step 3. Authentication Check

```bash
camscanner-cli auth status
```

- **Logged in** → Environment ready, proceed with user task
- **Not logged in or token expired** → Run `camscanner-cli auth login`, then verify again

> **Agent login behavior rules (mandatory)**:
> - Must run `camscanner-cli auth login` in the **foreground** (no `&` backgrounding). The command blocks until the user completes browser OAuth and returns automatically.
> - After login, verify with `camscanner-cli auth status`; on failure, inform the user to retry.

| Action | Command |
|--------|---------|
| Check status | `camscanner-cli auth status` |
| Browser login | `camscanner-cli auth login` |
| Log out | `camscanner-cli auth logout` |

> **Token safety**: Never display token plaintext to the user or write it to an unsafe location.

---

## Operating Limits

1. **Do not leak credentials**: Tokens must only be obtained through `camscanner-cli auth login` and stored in the system keychain.
2. **File size limit**: Uploaded files must not exceed 40 MB.
3. **Supported image formats**: JPG, JPEG, PNG.
4. **Supported document formats**: PDF, TXT, Markdown.

---

## Command Format

```bash
camscanner-cli <group> <command> [file...] [flags]
```

**Groups**: `image` (image processing), `pdf` (PDF processing), `txt` (text processing), `auth` (authentication management).

**Common flags**:

| Flag | Description |
|------|-------------|
| `-o, --output <path>` | Output file path. If omitted, the CLI derives one automatically. |
| `-s, --save` | Save the result to the user's CamScanner account and skip local download. |
| `--save-title <title>` | Cloud document title. If omitted, the CLI generates one in the form `{feature}{time}`. |
| `-h, --help` | Show help. |

### Interaction Between `-o` and `-s`

| Arguments | Behavior |
|-----------|----------|
| No `-o`, no `-s` | Save locally to an automatically derived path. |
| `-o path` | Save only to the specified local path. |
| `-s` | **Save only to the cloud** and skip local download. |
| `-o path -s` | Save both locally **and** to the cloud. |

### Agent Default Save Policy

> **Mandatory rule**: When the user does not explicitly specify a save method, the agent **must** save both locally and to the cloud (pass the `-s` flag). Saving only locally without `-s` is **incorrect behavior**. Only omit `-s` when the user explicitly says "save locally only" / "don't save to cloud".

| User Intent | Agent Behavior |
|-------------|----------------|
| No explicit save preference | **Must** use `-s` to save both locally and to cloud (i.e., `-o <auto-derived path> -s`) |
| Explicitly says "save locally" or specifies a path | Only `-o path`, no `-s` |
| Explicitly says "save to cloud/account" | Only `-s`, no `-o` |
| Feature does not support `-s` (see commands marked with No in the overview) | Save locally only, no `-s` |

### `--save-title` Smart Naming Rules

When saving to cloud with `-s`, the agent **must** attempt smart naming via `--save-title`:

1. **Prefer smart naming**: Generate a concise, meaningful title based on the filename, user intent, and document content.
   - Example: User says "convert this invoice to Excel" → `--save-title "Invoice to Excel"`
   - Example: File is `meeting_notes_0810.png`, converting to Word → `--save-title "Meeting Notes 0810"`
   - Example: Merging multiple scans into PDF → `--save-title "Scanned Documents Merged"`
2. **Fallback when naming fails**: If a meaningful title cannot be inferred from context (e.g., filename has no semantics, user did not describe intent), **do not pass** `--save-title` — let the CLI use its default rule (`{feature}{time}`).
3. **Title requirements**: Concise (20 chars or fewer), meaningful, no file paths or technical parameters.

---

## Capabilities

### Tool Overview

| Category | Command | Function | Output Type | Supports `-s` |
|----------|---------|----------|-------------|---------------|
| **Image enhancement** | `image enhance` | Remove shadows, sharpen, convert to black and white, and other 10 modes | Image | Yes |
| **Image enhancement** | `image hd` | Upscale images and improve resolution | Image | Yes |
| **Image enhancement** | `image restore` | Restore old photos | Image | Yes |
| **Format conversion** | `image convert` | Image -> Word/Excel/TXT/Markdown | Document | Yes, except TXT |
| **Format conversion** | `image to-pdf` | Single image -> PDF | PDF | Yes |
| **Format conversion** | `pdf convert` | PDF -> Word/Excel/TXT/Markdown | Document | Yes |
| **Format conversion** | `txt to-word` | TXT -> Word | Word | Yes |
| **Watermark** | `image watermark` | Add a text watermark to an image | Image | Yes |
| **Watermark** | `pdf watermark` | Add a text watermark to a PDF | PDF | Yes |
| **Watermark** | `pdf remove-watermark` | Remove watermarks from a PDF | PDF | Yes |
| **Translation** | `image translate` | Translate text in an image while preserving layout | Image | Yes |
| **Formula** | `image extract-formula` | Extract mathematical formulas | Image | Yes |
| **Merge** | `image merge-pdf` | Merge multiple images into a PDF, up to 100 images | PDF | Yes |
| **Merge** | `image merge-excel` | Merge multiple images into Excel, up to 100 images | Excel | Yes |
| **Merge** | `image merge-word` | Merge multiple images into Word, up to 100 images | Word | Yes |
| **PDF** | `pdf to-images` | Convert each PDF page to an image | Image directory | Yes |
| **PDF** | `pdf to-images-zip` | Convert PDF pages to an image ZIP | ZIP | No |
| **Recognition** | `image ocr` | OCR text recognition | stdout text | No |
| **Recognition** | `image merge-text` | OCR multiple images and merge text, up to 100 images | stdout/file | No |
| **Detection** | `image validate` | Tampering/AI-generated image detection | stdout JSON | No |
| **Editing** | `image scan` | Analyze image layout and obtain character indexes and OSS keys | stdout/JSON | No |
| **Editing** | `image edit` | Replace, delete, or move text based on scan results | Image | Yes |

### Unsupported Operations

- Online collaborative editing.
- File version management.
- Video/audio processing.
- Batch folder management.

---

## Reference Routing

Before executing an operation, the agent **must** read the corresponding reference file for full parameters and usage.

### Command References (Required)

| Trigger | Reference File | Contents |
|---------|----------------|----------|
| Processing image files | `references/image-processing.md` | Full parameters, mode values, and examples for all `image` commands |
| Processing PDF files | `references/pdf-processing.md` | Full parameters, limits, and examples for all `pdf` commands |
| User request requires multiple steps | `references/tool-combos.md` | Scenario-to-command combination mapping |

### Workflow References (Required for Multi-Step Tasks)

| Trigger | Workflow File | Contents |
|---------|---------------|----------|
| Multiple images need merging or batch conversion | `references/workflows/batch-convert.md` | Merge strategy selection and batching logic |
| Image enhancement, upscaling, or restoration | `references/workflows/image-enhance.md` | Mode selection decision tree |
| OCR or text extraction | `references/workflows/ocr-extract.md` | Plain text vs Markdown vs Word comparison |
| Image translation | `references/workflows/translate.md` | Language codes and multilingual version workflow |
| Watermark add/remove | `references/workflows/watermark-protection.md` | Recommended parameters and scenario mapping |

---

## Intent Routing Rules

Route intents in the priority order below. **Do not jump directly to a command based only on keywords.**

### Level 1: Determine Input File Type

| Input File Type | Available Command Group |
|-----------------|-------------------------|
| Image (jpg/jpeg/png) | `image *` |
| PDF | `pdf *` |
| TXT/Markdown | `txt to-word` |
| Mixed types (image + PDF) | Process each type separately. **Cross-type merging into a single artifact is not supported.** |

### Level 2: Determine Operation Intent

Use the user's verbs, keywords, and context to determine the operation type.

| Operation Type | Trigger Evidence | Command Direction |
|----------------|------------------|-------------------|
| Format conversion | "convert to Word", "convert to Excel", "convert to PDF", "convert to Markdown" | `convert` / `to-pdf` / `merge-*` |
| OCR recognition | "recognize", "OCR", "extract text" | `ocr` / `merge-text` / `pdf convert --format txt/md` |
| Image enhancement | "enhance", "remove shadows", "sharpen", "remove moire" | `image enhance` |
| Image upscaling | "HD", "clearer", "increase resolution", "blurry" | `image hd` |
| Photo restoration | "restore", "old photo", "scratch", "faded" | `image restore` |
| Watermark processing | "add watermark", "remove watermark" | `watermark` / `remove-watermark` / `enhance --mode 10` |
| Translation | "translate" | `image translate` |
| Detection | "detect", "Photoshop", "tampered", "AI-generated" | `image validate` |
| Editing | "edit image text", "replace text", "modify text", "change X to Y" | `image scan` -> `image edit` (automatically locate character indexes) |
| Formula extraction | "formula", "LaTeX" | `image extract-formula` |

### Level 3: Determine Quantity and Artifact

| Condition | Route |
|-----------|-------|
| Single image -> format conversion | `image convert --format xx` or `image to-pdf` |
| Multiple images -> one document | `image merge-pdf/word/excel`, up to 100 images |
| Multiple images -> process separately | Execute one by one |
| Single PDF -> format conversion | `pdf convert --format xx` |
| Multiple PDFs | Execute one by one. **There is no PDF merge command.** |

### Level 4: Target Format and Required Parameters

| Input -> Target | Correct Command | Common Pitfall |
|-----------------|-----------------|----------------|
| Image -> Word | `image convert --format word` | |
| Image -> Excel | `image convert --format excel` | |
| Image -> Markdown | `image convert --format md` | |
| Image -> TXT | `image convert --format txt` | Does not support `-s` |
| Image -> PDF | `image to-pdf` for one image, or `image merge-pdf` for multiple images | **Not** `image convert --format pdf` |
| PDF -> Word | `pdf convert --format word` | |
| PDF -> Excel | `pdf convert --format excel` | |
| PDF -> Markdown | `pdf convert --format md` | |
| PDF -> images | `pdf to-images` or `pdf to-images-zip` | |
| TXT -> Word | `txt to-word` | |

### Intent Disambiguation Rules

When a user request matches multiple operations, disambiguate as follows.

| Conflict | Disambiguation Rule |
|----------|---------------------|
| "make it sharper and clearer": `enhance --mode 2` vs `hd` | If the original image is blurry or low-resolution, use `hd`; if it is already clear but needs sharper details, use `enhance --mode 2`; ask if uncertain. |
| "scan": `image scan` vs `to-pdf` | If the user intends to edit content, use `scan` + `edit`; otherwise default to "generate a PDF" and use `to-pdf`. |
| "OCR": plain text vs Markdown vs Word | Ask which format the user wants; default recommendation is `convert --format md` to preserve structure. |
| "restore": `restore` vs `enhance` | If the user mentions old photos, scratches, or fading, use `restore`; otherwise choose an enhance mode based on the specific issue. |
| "detect": tampering vs AI-generated | If the user mentions Photoshop, tampering, or modification, use mode 1; if the user mentions AI, generated, or fake, use mode 2; ask if uncertain. |
| "remove watermark": PDF vs image | Choose automatically by input type: PDF -> `pdf remove-watermark`, image -> `enhance --mode 10`. |

**Principle: if an ambiguity changes the command choice, ask the user instead of guessing.**

### Common Routing Mistakes the Agent Must Avoid

| User Request | Wrong Route | Correct Route | Reason |
|--------------|-------------|---------------|--------|
| "merge two PDFs" | ~~`image merge-pdf`~~ | Not currently supported; tell the user | `image merge-pdf` only accepts image inputs |
| "recognize text in this PDF" | ~~`image ocr`~~ | `pdf convert --format txt/md` | `image ocr` only accepts images |
| "scan these photos into a PDF" | ~~`image scan`~~ | `image to-pdf` or `image merge-pdf` | `image scan` is layout analysis |
| "remove the watermark from this image" | ~~`pdf remove-watermark`~~ | `image enhance --mode 10` | `pdf remove-watermark` only processes PDFs |
| "image to PDF" | ~~`image convert --format pdf`~~ | `image to-pdf` / `image merge-pdf` | `convert_image` does not support PDF output |
| "combine a.jpg and b.pdf into one Word file" | ~~silently process separately~~ | Explain that cross-type merging is not supported | Different input types cannot be merged into one artifact |

---

## Error Quick Reference

| Error Signature | Cause | Handling |
|-----------------|-------|----------|
| `Authentication failed, run camscanner-cli auth login` | Token expired or user is not logged in | Run `camscanner-cli auth login` |
| `file does not exist` | Input path is wrong | Check the file path |
| `file size exceeds the maximum limit` | File exceeds 40 MB | Compress the file and retry |
| `rate limit exceeded` (429) | Calls are too frequent | Wait 10 seconds and retry |
| `txt format cannot be saved as a cloud document` | TXT is not supported as a cloud document type | Use `--format md` instead |
| HTTP 504 | Backend service timeout | Wait 5 seconds and retry once |
| HTTP 500 | Internal server error | Wait 5 seconds and retry once |

### Retry Strategy

| Operation Type | Idempotent | Safe to Retry |
|----------------|------------|---------------|
| All conversion/enhancement commands | Yes | Safe to retry |
| Saving cloud documents with `-s` | No | Retry may create duplicate documents, which is acceptable |
| `image edit` | Yes | Safe to retry |

---

## Safety Constraints

- Tokens are managed by the system keychain. The skill does not store or log tokens.
- **Data flow**:
  - Input files are uploaded to CamScanner servers for processing and are temporarily stored there during processing.
  - Converted artifacts generate temporary `file_id` values, which are used to download results.
  - With `-s`, processing results are persistently saved to the user's CamScanner account.
  - With `-o`, results are downloaded locally; server-side temporary files are cleaned up according to the server retention policy.
  - The skill itself does not additionally cache or persist document content.
- **Output path conflict protection**: The CLI silently overwrites existing files when `-o` is used. Before write operations, the agent **must** check whether the output path already exists. If it does:
  1. Prefer appending a numeric suffix, such as `output_1.jpg` or `output_2.jpg`.
  2. Or ask the user to confirm overwrite.
  3. Never overwrite an existing user file without confirmation.
- **Multiple file argument rules**: Do not pass multiple files with glob wildcards such as `*.jpg`. The agent **must**:
  1. List files in the directory first and determine page order using natural sorting, where `page2` comes before `page10`.
  2. Pass each file as a full quoted path so spaces or special characters in filenames are safe.
  3. Confirm the file list and order with the user before execution.

  ```bash
  # Correct: explicitly listed, quoted, and ordered.
  camscanner-cli image merge-pdf "scan_01.jpg" "scan_02.jpg" "scan_03.jpg" -s

  # Wrong: glob order is uncertain and paths are unsafe.
  camscanner-cli image merge-pdf *.jpg -s
  ```
