## Description:

Recognizes hygiene license documents with Sugon-Scnet OCR and returns structured JSON fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit a local hygiene-license image, PDF, or archive to the Scnet OCR API and receive structured recognition results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected document content and filename are sent to Scnet for OCR processing.

Mitigation: Use only with documents approved for third-party processing, avoid documents that require local-only handling, and protect SCNET_API_KEY in environment or config files.

Risk: High call volume can trigger the Scnet OCR API rate limit.

Mitigation: Call the skill serially, allow the built-in retry behavior to complete, and reduce request frequency if 429 responses continue.

## Reference(s):

- [Sugon-Scnet OCR API documentation](artifact/references/api-docs.md)
- [Hygiene license output fields](artifact/assets/templates/fields-summary.md)
- [Server-resolved source repository](https://github.com/SCNet-sugon/health_license_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/health-license-ocr)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [JSON data on standard output, with text error messages on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns recognized document fields from the API data payload; confidence values are removed by the script before output.]

## Skill Version(s):

0.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
