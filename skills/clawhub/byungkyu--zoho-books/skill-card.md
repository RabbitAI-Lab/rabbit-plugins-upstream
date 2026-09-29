## Description:

Guides agents through user-approved Zoho Books accounting tasks using Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to read and manage invoices, contacts, bills, expenses, and other records in a connected Zoho Books account, with approval before changes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive business and accounting data through the connected account.

Mitigation: Confirm the intended account and scopes; prefer CLI/OAuth authentication over long-lived API keys.

Risk: Incorrect writes or deletes can change financial records.

Mitigation: Confirm resource IDs and payloads with the user before each write or delete.

Risk: Hosted functions, triggers, or destination URLs may continue running or forwarding data.

Mitigation: Review and explicitly approve each automation and destination; remove them when no longer needed.

## Reference(s):

- [Zoho Books skill release](https://clawhub.ai/byungkyu/skills/zoho-books)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Zoho Books API v3 introduction](https://www.zoho.com/books/api/v3/introduction/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Text and Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples and responses; execution depends on the user's authorized connection.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence; skill frontmatter states 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
