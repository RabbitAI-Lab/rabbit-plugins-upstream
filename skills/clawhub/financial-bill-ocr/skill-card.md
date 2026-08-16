## Description:

Recognizes supported financial bills and trade documents through Scnet OCR and extracts key fields as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to submit local images, PDFs, or supported archives of financial documents to Scnet OCR and receive structured extraction results for review or downstream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected financial documents to Scnet's OCR service.

Mitigation: Use it only when the environment permits third-party processing of those documents and the user or administrator has explicitly approved the upload.

Risk: Financial documents can contain sensitive, regulated, or customer data.

Mitigation: Avoid using the skill on highly sensitive or regulated data unless vendor approval, retention, and data-residency reviews are complete.

Risk: The Scnet API key can be exposed if pasted into chat or stored with weak file permissions.

Mitigation: Keep the API key out of chat, store it in config/.env or an environment variable, and protect config/.env with restrictive permissions.

Risk: Changing SCNET_API_BASE can redirect document uploads to an untrusted endpoint.

Mitigation: Leave SCNET_API_BASE at the documented default unless the alternate endpoint has been reviewed and trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/financial-bill-ocr)
- [Scnet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API documentation summary](artifact/references/api-docs.md)
- [Financial document field summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON written to standard output, with human-readable error text on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY; optionally accepts SCNET_API_BASE for a trusted alternate endpoint.]

## Skill Version(s):

1.0.2 (source: frontmatter, skill.yaml, changelog, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
