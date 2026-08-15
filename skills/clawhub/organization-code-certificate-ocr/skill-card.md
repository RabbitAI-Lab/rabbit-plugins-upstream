## Description:

Recognizes organization code certificate information from images or PDFs using Scnet OCR and returns structured JSON results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to extract organization code certificate fields from authorized certificate images or PDFs through Scnet's OCR API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Certificate images or PDFs are sent to Scnet's OCR service.

Mitigation: Use only documents you are authorized to process and review Scnet's privacy and retention terms before sending sensitive files.

Risk: SCNET_API_KEY exposure could allow unauthorized API use.

Mitigation: Store the key in a protected environment variable or local config file, keep it out of chat logs and source control, and rotate it if exposed.

Risk: Repeated OCR calls can hit API rate limits.

Mitigation: Invoke the skill serially, respect retry guidance, and reduce request frequency when 429 responses occur.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/SCNet-sugon/organization_code_certificate_ocr)
- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/organization-code-certificate-ocr)
- [Scnet website](https://www.scnet.cn)
- [Sugon-Scnet OCR API docs](references/api-docs.md)
- [Organization code certificate fields](assets/templates/fields-summary.md)

## Skill Output:

**Output Type(s):** [text, JSON]

**Output Format:** [JSON printed to standard output, with text error messages for configuration, API, or file validation failures.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recognition results are returned from the API data payload; artifact behavior removes confidence values before printing.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact frontmatter and changelog report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
