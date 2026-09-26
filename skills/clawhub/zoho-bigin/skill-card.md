## Description:

Helps an agent read and manage Zoho Bigin CRM records, including contacts, companies, products, and sales pipelines, through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and their agents use this skill to look up, create, update, and delete Zoho Bigin CRM records and manage pipeline information after connecting an authorized account. Optional Maton functions and triggers can automate approved actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account may authorize access to sensitive CRM records beyond the immediate task.

Mitigation: Confirm the account connection with the user, prefer OAuth, and select only the Zoho scopes needed for the task.

Risk: Creating, changing, or deleting CRM records can affect customer information and sales workflows.

Mitigation: Start with read-only requests and obtain explicit user approval for each write or delete after reviewing its target and payload.

Risk: Functions, triggers, destinations, and non-core CRM modules can introduce broader or ongoing access and downstream effects.

Mitigation: Require specific approval before using these features and review their scope, destinations, and intended effects.

## Reference(s):

- [ClawHub Zoho Bigin skill](https://clawhub.ai/byungkyu/skills/zoho-bigin)
- [Maton homepage](https://maton.ai)
- [Zoho Bigin API documentation](https://www.bigin.com/developer/docs/apis/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with example commands, code, and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Maton connection; CRM responses may contain personal data.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; skill metadata states 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
