## Description: <br>
Email Ledger parses .eml files or ZIP archives of email messages, extracts reporting fields, and generates an Excel ledger with optional template append and deduplication. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smallkeyboy](https://clawhub.ai/user/smallkeyboy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users who need to organize reporting emails use this skill to convert .eml files or ZIP archives into an Excel ledger, optionally appending to an existing workbook and highlighting fields that need manual completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles sensitive email-derived data and may upload the generated spreadsheet for download. <br>
Mitigation: Generate the workbook locally first, review the contents, and upload it only after explicit user approval. <br>
Risk: Supplier, channel, and approver extraction can be incomplete or uncertain. <br>
Mitigation: Review highlighted manual-completion fields in the Excel ledger before using it as an authoritative record. <br>


## Reference(s): <br>
- [Parsing rules reference](artifact/references/parsing_rules.md) <br>
- [ClawHub skill page](https://clawhub.ai/smallkeyboy/skills/email-ledger) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, markdown, guidance] <br>
**Output Format:** [Excel workbook plus concise Markdown status report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated workbook may include parsed sender, recipient, subject, body summary, supplier/channel, approval, deduplication, and highlighted manual-completion fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
