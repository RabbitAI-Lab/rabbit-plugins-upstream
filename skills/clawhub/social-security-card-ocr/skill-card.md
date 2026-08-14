## Description:

Recognizes Chinese social security card or medical insurance card images and extracts core fields such as name, social security number, identity number, card number, bank card number, validity period, and issuing institution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill when a user explicitly requests social security card recognition and provides an authorized local image or PDF path. It is intended for the narrow task of extracting structured social security card fields, not general OCR or other identity-document recognition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Social security card images may contain identity, social security, and bank-card data and are sent to SCNet's remote OCR service.

Mitigation: Use the skill only with authorization from the cardholder, keep SCNET_API_BASE pointed at the trusted default endpoint, and delete local images or cached copies after use.

Risk: API keys can be exposed if pasted into chat, logs, or shared files.

Mitigation: Store SCNET_API_KEY in a protected environment or config file, restrict file permissions, and rotate the token if exposure is suspected.

Risk: Using the skill outside its intended card type can upload unintended personal documents.

Mitigation: Invoke it only for explicit social security card or medical insurance card recognition requests and keep the ocrType fixed to SOCIAL_SECURITY_CARD.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/social-security-card-ocr)
- [Sugon-Scnet OCR API docs summary](references/api-docs.md)
- [Social security card fields summary](assets/templates/fields-summary.md)
- [SCNet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON array on stdout, with text error messages on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ocrType SOCIAL_SECURITY_CARD and an absolute local file path; removes confidence metadata from successful OCR results.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
