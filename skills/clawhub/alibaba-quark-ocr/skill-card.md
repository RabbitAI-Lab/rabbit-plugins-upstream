## Description: <br>
Alibaba Quark OCR helps agents extract and structure text from images, screenshots, photos, and scanned documents using Quark Scan OCR service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yescan-ai](https://clawhub.ai/user/yescan-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to recognize, extract, and structure text from single image inputs, including handwriting, tables, formulas, identity documents, invoices, tickets, medical reports, business licenses, exercises, product images, and general OCR tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Images submitted to the skill, including IDs, invoices, and medical documents, are sent to Quark's remote OCR service. <br>
Mitigation: Use the skill only for documents you are authorized to share with Quark, and review the provider's retention and privacy terms before processing sensitive content. <br>
Risk: The skill depends on the SCAN_WEBSERVICE_KEY credential to call the OCR service. <br>
Mitigation: Store the key in agent environment configuration, restrict access to it, and rotate it if exposure is suspected. <br>


## Reference(s): <br>
- [Quark Scan business homepage](https://scan.quark.cn/business) <br>
- [ClawHub skill page](https://clawhub.ai/yescan-ai/skills/alibaba-quark-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [JSON responses and command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SCAN_WEBSERVICE_KEY; accepts one image URL, local image path, or base64 image input per run.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
