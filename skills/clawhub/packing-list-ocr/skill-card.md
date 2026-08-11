## Description:

Recognizes packing-list documents and extracts goods categories, weight and volume, sender and recipient information, and document numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and operations teams can use this skill to send local packing-list images or PDFs to Scnet's OCR API and receive structured extraction results for shipping-document workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected packing-list files are uploaded to Scnet's hosted OCR service and may contain sensitive trade, personal, or regulated data.

Mitigation: Use only on documents approved for that data flow, avoid confidential or regulated records unless authorized, and keep SCNET_API_BASE set to a trusted endpoint.

Risk: The skill requires an SCNET_API_KEY credential.

Mitigation: Store the API key in the configured environment or local config file, restrict file permissions, and do not paste the key into chat sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/packing-list-ocr)
- [Publisher profile](https://clawhub.ai/user/scnet-sugon)
- [Server-resolved source repository](https://github.com/SCNet-sugon/packing_list_ocr)
- [Scnet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API documentation](references/api-docs.md)
- [Packing-list field summary](assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON on stdout with human-readable error text on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ocrType value, a local file path, and SCNET_API_KEY; the selected document is uploaded to Scnet's hosted OCR service.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
