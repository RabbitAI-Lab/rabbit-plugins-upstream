## Description:

Extracts core bill-of-lading fields such as ports, shipper and consignee, cargo quantity, bill of lading number, and carrier information from document images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to call the Scnet OCR API for bill-of-lading recognition and return structured extraction results for shipping-document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads bill-of-lading files, which may contain sensitive shipping or business information, to an external OCR API.

Mitigation: Use only on documents the user is authorized to upload, review the provider's data-handling terms, and consider requiring explicit confirmation before each OCR upload.

Risk: The skill requires an API key for Scnet's service.

Mitigation: Store SCNET_API_KEY in an environment variable or protected configuration file, do not paste API keys into chat, and rotate the key if it is exposed.

## Reference(s):

- [Sugon-Scnet OCR API documentation](references/api-docs.md)
- [Bill-of-lading field summary](assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)
- [Scnet OCR API base endpoint](https://api.scnet.cn/api/llm/v1)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [JSON written to standard output, with human-readable error text for failures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the provided local document file to Scnet's remote OCR service.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
