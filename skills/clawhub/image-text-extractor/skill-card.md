## Description: <br>
Extracts text from uploaded images and PDF documents, preserving structure where possible and returning readable, structured results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, office workers, students, researchers, content creators, and developers use this skill to convert uploaded PDFs, scanned documents, screenshots, and image assets into editable text or Markdown for review, archiving, note-taking, and reuse. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive document contents may be displayed in chat or persisted if the user asks to save extracted output. <br>
Mitigation: Avoid processing highly sensitive documents unless the user accepts that extracted text may appear in chat or be saved as a Markdown file that may need deletion later. <br>
Risk: OCR and PDF extraction accuracy can be reduced by blurry images, complex layouts, scanned PDFs, or encrypted PDFs. <br>
Mitigation: Tell users when text cannot be extracted reliably, provide the best available extraction, and recommend OCR or a clearer source document when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/image-text-extractor) <br>
- [README.en.md](artifact/README.en.md) <br>
- [README.md](artifact/README.md) <br>
- [PDF text extraction script](artifact/scripts/pdf_text_extractor.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text, optional Markdown files, and JSON status from the PDF extraction script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PDF extraction reports success status, extracted text, page count, and error details when applicable.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
