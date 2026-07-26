## Description: <br>
Extracts structured Markdown and JSON from PDFs and document images, including tables, formulas, charts, headers, footers, multi-column layout, and reading order. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bobholamovic](https://clawhub.ai/user/bobholamovic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and document-processing users can use this skill to invoke PaddleOCR document parsing for PDFs and images that need structured text, tables, formulas, and layout-aware extraction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documents processed through the hosted PaddleOCR API may contain confidential, regulated, customer, legal, financial, or identity information. <br>
Mitigation: Process only documents permitted by the user's data-sharing and retention requirements, and prefer summaries or redacted excerpts when full extracted text is not needed. <br>
Risk: The skill requires a PaddleOCR access token and depends on the installed PaddleOCR CLI package. <br>
Mitigation: Keep the token in the environment rather than prompts or logs, and install the CLI only from a trusted source. <br>


## Reference(s): <br>
- [PaddleOCR Official API CLI Documentation](https://www.paddleocr.ai/latest/en/version3.x/inference_deployment/serving/paddleocr_official_api/cli.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/bobholamovic/skills/paddleocr-doc-parsing) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include extracted Markdown text, image or resource links, saved output paths, and user-facing CLI error details.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
