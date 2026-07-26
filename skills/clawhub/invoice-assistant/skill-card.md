## Description: <br>
Read and analyze local Little Beaver Invoice Assistant data through the app's localhost Skill API, including invoice ledgers, invoice items, companies, customer, supplier, and product rankings, monthly invoice trends, tax invoice summaries, and archived electronic invoice attachment metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[littlebeaverstudio](https://clawhub.ai/user/littlebeaverstudio) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent connect to a locally running 小河狸发票助手 desktop app, read invoice data through a localhost API, and produce invoice ledger, ranking, trend, tax-summary, and attachment-metadata analysis. It is intended for read-only extraction and analysis; attachment opening should happen only after an explicit user request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can return sensitive invoice, tax, company, counterparty, item, and attachment metadata from a local business ledger. <br>
Mitigation: Use it only with intentional access to the local app, scope requests to the needed company and date range, and avoid sharing returned data outside the approved workflow. <br>
Risk: The open-attachment action launches a local PDF, OFD, or XML file in the user's default application. <br>
Mitigation: Open attachments only after an explicit user request and when the user is comfortable launching the local file. <br>
Risk: Invoice and tax summaries are invoice-ledger calculations and may not match final tax payable or filing results. <br>
Mitigation: State the company, date range, and whether voided invoices were excluded, and treat results as analysis inputs rather than final tax advice. <br>


## Reference(s): <br>
- [小河狸发票助手本机 Skill API](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/littlebeaverstudio/skills/invoice-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/littlebeaverstudio) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-backed analysis with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads from a localhost API and returns scoped invoice, company, ranking, summary, item, and attachment metadata; it does not import, modify, delete, or upload invoice data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
