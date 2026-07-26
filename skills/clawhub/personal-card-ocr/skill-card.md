## Description: <br>
Extracts structured OCR data from images and document files for text and personal documents such as identity cards, bank cards, household registers, passports, driver licenses, education certificates, and related credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to submit a selected local image or document file to Scnet OCR and receive structured recognition results for supported personal-document types. It is intended for user-selected files where OCR extraction of identity, credential, banking, vehicle, property, or education fields is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected document images and extracted personal data are sent to Scnet's OCR service. <br>
Mitigation: Use the skill only for files the user intentionally selects, avoid unnecessary identity or financial documents, and confirm the API endpoint and provider terms before use. <br>
Risk: The skill requires an API key for an external OCR service. <br>
Mitigation: Store SCNET_API_KEY in the configured environment or local .env file and do not paste the key into chat. <br>
Risk: Privacy disclosure and user-confirmation guidance are limited for sensitive personal documents. <br>
Mitigation: Confirm user consent before processing personal documents and review the returned JSON for sensitive fields before sharing or storing it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/scnet-sugon/skills/personal-card-ocr) <br>
- [Sugon-Scnet OCR API Documentation Summary](references/api-docs.md) <br>
- [OCR Field Summary](assets/templates/fields-summary.md) <br>
- [Scnet Website](https://www.scnet.cn) <br>
- [Scnet OCR API Base](https://api.scnet.cn/api/llm/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [JSON recognition data on standard output, with text error messages for configuration, network, authentication, rate-limit, or API failures.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCNET_API_KEY and accepts an OCR type plus a local file path.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata, SKILL.md frontmatter, skill.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
