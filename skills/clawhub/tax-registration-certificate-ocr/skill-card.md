## Description:

Recognizes tax registration certificate documents with SCNET OCR and returns structured fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to send an authorized local tax registration certificate image, PDF, or archive to SCNET OCR and receive structured registration fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads tax registration documents to SCNET for OCR processing, and those files or extracted fields may contain sensitive business or personal data.

Mitigation: Use it only for documents the user is authorized to process, and confirm that SCNET's handling and retention terms meet the user's compliance requirements before uploading.

Risk: The skill requires an SCNET API key and can read credentials from config/.env.

Mitigation: Protect config/.env with local file permissions, avoid sharing API keys in chat, and rotate the key if it may have been exposed.

Risk: Changing SCNET_API_BASE can redirect document uploads to a different endpoint.

Mitigation: Keep SCNET_API_BASE at the documented SCNET endpoint unless the organization has approved the alternate service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/tax-registration-certificate-ocr)
- [SCNET website](https://www.scnet.cn)
- [SCNET OCR API endpoint](https://api.scnet.cn/api/llm/v1/ocr/recognize)
- [Sugon-Scnet OCR API docs](artifact/references/api-docs.md)
- [Tax registration certificate field summary](artifact/assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [json, text]

**Output Format:** [JSON on stdout with human-readable error text on failure]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The JSON contains the API data array after OCR recognition; the script removes confidence fields before printing.]

## Skill Version(s):

0.1.1 (source: server release evidence; artifact frontmatter and changelog show 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
