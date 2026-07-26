## Description: <br>
Generate professional PDF invoices from JSON data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tmigone](https://clawhub.ai/user/tmigone) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, employees, and developers use this skill to generate billing documents or payment-request PDFs from structured invoice JSON with company, client, invoice, item, and totals data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes invoice data and writes generated PDFs to local disk. <br>
Mitigation: Set INVOICE_DIR to a private, intended storage location and review generated files before sharing. <br>
Risk: The artifact expects an assets/invoice.hbs template that is not present in the provided artifact files. <br>
Mitigation: Review or supply the invoice.hbs template before relying on generated invoice output. <br>
Risk: The skill depends on local Node.js dependencies, jq, weasyprint, and Handlebars. <br>
Mitigation: Use deterministic installs, verify required binaries are available, and keep Handlebars updated if security advisories apply. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tmigone/skills/invoice-generator) <br>
- [Invoice Data Schema](references/data-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated PDF files and a text path on success] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node, jq, weasyprint, npm-installed dependencies, and INVOICE_DIR; reads JSON from stdin, a file path, or a saved config and writes PDFs under INVOICE_DIR/invoices.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
