## Description:

Triggers only for explicit bank-check OCR requests and extracts check numbers, dates, amounts, signatures or stamps, and related fields from bank-check images; it is not for general OCR or non-check images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit an explicitly provided bank-check image or PDF to the SCNet OCR service and receive structured fields such as check number, issue date, amounts, account information, and stamps. It should only be used when the requester is authorized to process the check image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bank-check images can contain account numbers, signatures, stamps, names, and amounts, and this skill sends those images to the configured SCNet OCR service.

Mitigation: Use the skill only with authorization from the relevant check or account holders, upload only necessary bank-check files, and confirm the configured OCR endpoint is trusted.

Risk: The SCNET_API_KEY grants access to the OCR service and could be exposed if pasted into chat or stored with broad permissions.

Mitigation: Provide the key through an environment variable or a restricted config file, keep it out of chat transcripts, and rotate it if exposure is suspected.

## Reference(s):

- [Sugon-Scnet OCR API documentation](references/api-docs.md)
- [Bank check field summary](assets/templates/fields-summary.md)
- [SCNet website](https://www.scnet.cn)
- [SCNet OCR API endpoint](https://api.scnet.cn/api/llm/v1/ocr/recognize)

## Skill Output:

**Output Type(s):** [json, text]

**Output Format:** [JSON written to stdout, with friendly text errors on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the explicitly provided bank-check file to the configured SCNet OCR endpoint.]

## Skill Version(s):

1.0.2 (source: server release metadata, frontmatter, skill.yaml, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
