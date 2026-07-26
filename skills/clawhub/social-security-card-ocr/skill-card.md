## Description: <br>
Recognizes social security or medical insurance cards only when the user explicitly asks for that card type, extracting core fields such as name, social security number, ID number, card number, bank card number, issue date, and validity period. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to send an authorized social security or medical insurance card image to Scnet OCR and receive structured card-field extraction. It is not intended for general OCR or unrelated identity documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Social security and medical insurance card images can contain sensitive identity, social-security, bank-card, and photo data, and this skill sends those images to Scnet's external OCR service. <br>
Mitigation: Use only for documents the user is authorized to process, confirm third-party processing is acceptable, protect the API key, and delete local images or cached copies when they are no longer needed. <br>
Risk: The security evidence reports that scope controls are broader than the stated social-security-card-only purpose. <br>
Mitigation: Invoke the skill only for explicit social security or medical insurance card requests, and avoid using it for general OCR or unrelated documents. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API documentation](references/api-docs.md) <br>
- [Social security card field summary](assets/templates/fields-summary.md) <br>
- [Scnet website](https://www.scnet.cn) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text] <br>
**Output Format:** [Structured JSON on standard output, with friendly text errors on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local card image path and SCNET_API_KEY; sends the image to Scnet's external OCR API.] <br>

## Skill Version(s): <br>
1.0.4 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
