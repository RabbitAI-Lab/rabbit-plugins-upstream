## Description: <br>
Brevo (formerly Sendinblue) email marketing API for managing contacts, lists, sending transactional emails, and campaigns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yujesyoga](https://clawhub.ai/user/yujesyoga) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to ask an agent for Brevo API guidance, example requests, and safe patterns for managing contacts, lists, transactional email, campaigns, and email automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email and contact-management examples can make real business changes, including importing contacts, updating lists, deleting contacts, or sending email. <br>
Mitigation: Keep the Brevo API key scoped appropriately, review recipient lists and contact changes before execution, and require explicit confirmation before bulk email, import, update, or delete actions. <br>
Risk: Contact imports can accidentally include unsubscribed or blacklisted recipients. <br>
Mitigation: Check Brevo blacklist status before imports and preserve unsubscribe decisions when creating or updating contacts. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with endpoint tables, bash examples, Python snippets, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples are intended for review before execution because Brevo API calls can change contacts, lists, campaigns, and email delivery.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
