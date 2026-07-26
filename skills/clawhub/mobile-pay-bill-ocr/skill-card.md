## Description: <br>
Recognizes mobile payment bill screenshots for Alipay and WeChat Pay when the user explicitly asks for payment-bill OCR, then extracts transaction time, merchant, amount, and income or expense type into structured data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to OCR selected mobile payment bill images and obtain structured transaction fields for downstream review or processing. It is intended for payment bill screenshots, not general OCR or non-payment receipt recognition. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment bill screenshots are uploaded to Scnet's remote OCR service and may contain sensitive financial, identity, and relationship data. <br>
Mitigation: Use only files the user explicitly chooses, avoid unrelated personal or identity documents, and review the provider's privacy and retention terms before use. <br>
Risk: The file-upload behavior is broader than the stated payment-only purpose. <br>
Mitigation: Confirm the requested OCR type is MOBILE_PAYMENT_BILL and that the selected file is a mobile payment bill before execution. <br>
Risk: The required Scnet API key could be exposed if pasted into chat or stored insecurely. <br>
Mitigation: Keep the API key in a protected local config file or environment variable and do not share it in conversation. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API docs](references/api-docs.md) <br>
- [Mobile payment bill field summary](assets/templates/fields-summary.md) <br>
- [Scnet website](https://www.scnet.cn) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text] <br>
**Output Format:** [Structured JSON on success, with human-readable error text on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns OCR data from the service response with confidence fields removed by the wrapper script.] <br>

## Skill Version(s): <br>
1.0.1 (source: SKILL.md frontmatter, skill.yaml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
