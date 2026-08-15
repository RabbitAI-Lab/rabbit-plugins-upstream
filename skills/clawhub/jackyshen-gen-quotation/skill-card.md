## Description:

Generates professional PDF quotations, training proposals, and business documents from natural-language, Markdown, or structured inputs, with support for Chinese and English content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business teams, and consultants use this skill to turn quotation or training-proposal details into branded PDF business documents. It helps collect required customer, pricing, payment, validity, outline, and branding data before rendering the document locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated documents and intermediate output files may contain customer names, pricing, payment terms, or bank account details.

Mitigation: Use an appropriate workspace for sensitive business documents and clean up generated output files when they are no longer needed.

Risk: Quotation and proposal content can affect commercial commitments if customer, pricing, tax, validity, or payment details are inaccurate.

Mitigation: Review generated documents for business and legal accuracy before sharing them externally.

## Reference(s):

- [Server-resolved source repository](https://github.com/mebusw/jackyshen-gen-quotation)
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/jackyshen-gen-quotation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus structured JSON data rendered to local HTML and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces quotation or proposal PDFs in an output directory and may also write intermediate HTML preview files.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
