## Description:

Calls Scnet's online OCR service to extract invoice numbers, dates, amounts, issuer details, letters of credit, contract numbers, and price terms from commercial invoice images or PDFs uploaded to Scnet's cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and developers use this skill to send approved commercial invoice images or PDFs to Scnet's OCR API and receive structured invoice fields for downstream review or processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commercial invoices may contain sensitive business information and are uploaded to Scnet's cloud OCR service.

Mitigation: Use the skill only when the organization allows transfer of the selected invoice to Scnet and the user understands the file will leave the local environment.

Risk: The API key can be exposed if pasted into chat logs or committed to source control.

Mitigation: Keep SCNET_API_KEY out of chat and repositories, store it in environment variables or a restricted config/.env file, and use restrictive file permissions.

Risk: A mistaken file path could upload the wrong local invoice or another sensitive document.

Mitigation: Confirm the exact file path before each run and avoid broad or ambiguous paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/commercial-invoice-ocr)
- [Sugon-Scnet OCR API summary](artifact/references/api-docs.md)
- [Commercial invoice field summary](artifact/assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON OCR results with text status or error messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCNET_API_KEY and uploads the specified local file to Scnet's cloud OCR service.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
