## Description:

Recognizes enterprise license documents with Scnet OCR and returns structured JSON fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and business users use this skill to extract structured data from enterprise license images or PDFs, including business, food, hygiene, financial, payment, and account-opening licenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enterprise license documents may contain company identifiers, addresses, legal representative names, license numbers, and bank account details.

Mitigation: Use the skill only when the user or organization is allowed to send the selected document to Scnet's OCR service.

Risk: The service uploads the selected local document to an external OCR API.

Mitigation: Confirm vendor approval, data-handling requirements, and the intended document path before execution.

Risk: The OCR API has a documented 10 QPS rate limit.

Mitigation: Run recognition serially or keep request rates below the documented limit; the script retries 429 responses with backoff.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/SCNet-sugon/enterprise_license_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/enterprise-license-ocr)
- [Scnet website](https://www.scnet.cn)
- [Scnet OCR API documentation summary](artifact/references/api-docs.md)
- [OCR output fields summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout with human-readable error text on failure.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the selected license file to Scnet OCR; the script removes confidence fields before printing recognized data.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
