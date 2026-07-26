## Description: <br>
Process bank transaction CSV exports (Nordea, ICA), auto-categorize transactions using configurable rules, manage transaction links, and generate analytical database views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patello](https://clawhub.ai/user/patello) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to manage local personal-finance transaction data, categorize bank CSV imports, link transfers and reimbursements, and generate SQLite-backed finance summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool operates on user-selected bank-export CSVs and local SQLite finance databases. <br>
Mitigation: Install and run it only in workspaces where access to those local finance files is intended, and keep private data outside the skill directory. <br>
Risk: Cleanup, linking, auto-discovery, and recurring-payment changes can modify local finance records. <br>
Mitigation: Back up the SQLite database first and prefer dry-run previews where supported before committing changes. <br>
Risk: The security review identified a safety gap for `remove-recurring --hard`, which deletes a recurring-payment configuration immediately without a confirmation prompt. <br>
Mitigation: Use `remove-recurring --hard` only after confirming the target ID and maintaining a current database backup. <br>


## Reference(s): <br>
- [Financial Categorizer on ClawHub](https://clawhub.ai/patello/skills/financial-categorizer) <br>
- [patello publisher profile](https://clawhub.ai/user/patello) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands, configuration examples, and local data-management instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces guidance for local CSV import, SQLite database updates, categorization rules, transaction links, recurring-payment tracking, and reporting workflows.] <br>

## Skill Version(s): <br>
1.10.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
