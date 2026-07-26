## Description: <br>
CAD洞察专家 helps agents analyze PDF and DWG engineering drawings by extracting title blocks, dimensions, annotations, symbols, scales, quality issues, and quantity takeoff reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and construction review teams use this skill to turn local engineering drawings into structured title-block, dimension, symbol, scale, compliance, index, and quantity-takeoff outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read local engineering drawing files that contain sensitive project or customer information. <br>
Mitigation: Use it only with drawings approved for analysis in the agent environment and confirm intent before processing casual or generic PDF/CAD requests. <br>
Risk: Python parsing and OCR workflows can produce uncertain scale, dimension, quantity, or compliance outputs, especially for scanned drawings. <br>
Mitigation: Review proposed commands before execution and manually verify low-confidence OCR, scale, dimension, and takeoff results before relying on them for business decisions. <br>


## Reference(s): <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured JSON, table, CSV-style, Python, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local PDF/DWG drawing files and invoke Python parsing or OCR tooling when the agent environment permits it.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
