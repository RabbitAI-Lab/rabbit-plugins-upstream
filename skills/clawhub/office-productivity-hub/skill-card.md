## Description: <br>
办公效率中枢 helps agents automate common office workflows including document processing, data cleanup, email management, scheduling, report generation, and workflow orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and business teams use this skill to automate recurring document, spreadsheet, email, scheduling, and reporting work. It is most relevant for HR, finance, sales, administrative, and operations workflows that need batch processing, formatting checks, and sensitive-data handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Command execution can modify local office files or run broad batch operations. <br>
Mitigation: Require dry runs, scoped input and output paths, backups, and explicit user confirmation before execution. <br>
Risk: Office workflows may handle HR, finance, customer, or personal data. <br>
Mitigation: Apply PII masking, least-privilege access, local processing where possible, and human review before export or sharing. <br>
Risk: Email sending, scheduled jobs, database access, cloud storage, and webhooks can create external side effects. <br>
Mitigation: Require explicit approval for each external action, use test recipients or staging targets first, and keep audit logs. <br>
Risk: Credentials for SMTP, databases, webhooks, or cloud storage may be exposed if placed in files. <br>
Mitigation: Store credentials in environment variables or a secrets manager, avoid plaintext configuration, and rotate exposed tokens. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/thcjp/skills/office-productivity-hub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and task reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local file operations, email actions, scheduled jobs, database access, webhook calls, and dry-run or resume commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
