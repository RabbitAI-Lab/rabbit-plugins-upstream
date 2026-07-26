## Description: <br>
Recognizes bank-check images and extracts key fields such as check number, issue date, amount, payer information, account details, and stamp data through the Scnet OCR service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill when a user explicitly asks to recognize a bank check image and extract structured financial fields. It is not intended for general OCR or non-check image recognition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bank-check images can contain account numbers, signatures, stamps, and amounts that are uploaded to a third-party OCR service. <br>
Mitigation: Use the skill only with authorization from relevant account holders, review Scnet privacy and retention terms, and submit only files explicitly chosen for check recognition. <br>
Risk: The script can send any supplied local file and OCR type to the third-party API without code-enforced limits. <br>
Mitigation: Review the file path and requested OCR type before execution, keep API keys out of chat logs, and limit use to the BANK_CHECK workflow. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API documentation summary](references/api-docs.md) <br>
- [Bank check field summary](assets/templates/fields-summary.md) <br>
- [Scnet website](https://www.scnet.cn) <br>
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/bank-check-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, text] <br>
**Output Format:** [Structured JSON on standard output, with human-readable error messages when requests fail] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the selected file to Scnet's OCR API.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
