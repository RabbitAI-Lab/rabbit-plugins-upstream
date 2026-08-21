## Description:

Temu EU Tax API skill that helps agents call seven LinkFox-forwarded Partner EU temu.pay.tax interfaces for report export, Galerie signatures, invoice lookup and download, merchant report download, and invoice upload.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu EU sellers, operators, and developers use this skill to perform tax workflows through LinkFox, including VAT invoice queries, invoice upload, signed PDF download, Galerie signatures, and monthly tax report export or download.

### Deployment Geography for Use:

Europe, for Temu Partner EU tax workflows

## Known Risks and Mitigations:

Risk: The release security summary flags broader proxying, credential storage and reveal, billing/payment onboarding, and retention of sensitive tax results.

Mitigation: Review before production use, prefer specific tax scripts over generic proxy or file-download scripts, and restrict access to trusted workspaces.

Risk: Temu and LinkFox credentials and saved tax outputs may expose invoices, order identifiers, reports, or tokens.

Mitigation: Use dedicated least-privilege credentials, protect or disable the local token store, avoid exposing endpoint override environment variables, and regularly clean the linkfox response-output directory.

## Reference(s):

- [Skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-tax-eu)
- [API reference](references/api.md)
- [Temu access token guide](references/access-token.md)
- [Authorization flow](references/authorization-flow.md)
- [Partner EU catalog](references/partner-eu-catalog.md)
- [Tax API index](references/apis/README.md)
- [temu.pay.tax.apply.export.report](references/apis/temu-pay-tax-apply-export-report.md)
- [temu.pay.tax.get.galerie.signature](references/apis/temu-pay-tax-get-galerie-signature.md)
- [temu.pay.tax.invoice.detail.query](references/apis/temu-pay-tax-invoice-detail-query.md)
- [temu.pay.tax.invoice.info.query](references/apis/temu-pay-tax-invoice-info-query.md)
- [temu.pay.tax.invoice.pdf.download](references/apis/temu-pay-tax-invoice-pdf-download.md)
- [temu.pay.tax.merchant.report.download](references/apis/temu-pay-tax-merchant-report-download.md)
- [temu.pay.tax.merchant.upload.invoice](references/apis/temu-pay-tax-merchant-upload-invoice.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, JSON files]

**Output Format:** [Markdown guidance with shell commands and JSON request or response artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts save complete API responses under the workspace linkfox output directory and may print either full JSON or summaries depending on response size.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
