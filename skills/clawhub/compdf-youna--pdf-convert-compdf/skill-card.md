## Description: <br>
PDF conversion toolkit featuring AI layout analysis and OCR. Converts PDFs to Word, Markdown, JSON, PPT, CSV, HTML, and XML for seamless LLM data processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[compdf-youna](https://clawhub.ai/user/compdf-youna) <br>

### License/Terms of Use: <br>
Commercial / Proprietary <br>


## Use Case: <br>
Developers and agents use this skill to convert local PDF or image files into editable office documents, structured JSON, Markdown, CSV, HTML, text, RTF, or image outputs. It is suited for document preparation, extraction, and LLM-ready data processing workflows where ComPDFKitConversion is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on ComPDF's commercial SDK and first-run downloads for the SDK license file and, when AI layout or OCR is used, the Document AI model. <br>
Mitigation: Install only where this vendor dependency is acceptable; pre-place license.xml and documentai.model for offline or sensitive workflows, and set COMPDF_DOCUMENT_AI_MODEL when reusing a managed model file. <br>
Risk: The included trial license is limited and trial conversion counts are tracked locally. <br>
Mitigation: Use a valid ComPDF license for production workflows and monitor local trial usage before relying on the skill for repeated conversions. <br>
Risk: The AI layout model is large and may delay or fail conversion in environments without access to ComPDF's download endpoint. <br>
Mitigation: Pre-stage the model file or disable AI layout with --no-enable-ai-layout when layout analysis is not required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/compdf-youna/skills/pdf-convert-compdf) <br>
- [ComPDF Website](https://www.compdf.com/?utm_source=clawhub&utm_medium=skillhub&utm_campaign=pdf_skill_pdf_convert&ref_platform_id=clawhub_skills) <br>
- [ComPDFKit Conversion SDK Python Overview](https://www.compdf.com/guides/conversion-sdk/python/overview) <br>
- [ComPDFKit Python Apply License](https://www.compdf.com/guides/conversion-sdk/python/apply-license) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Converted document files with Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports PDF and image inputs on Windows or macOS; AI layout and OCR can require a first-run model download.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
