## Description:

Helps agents access Zoho CRM to search, manage, and automate CRM records through an authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and developers use this skill to find and manage Zoho CRM records, inspect organization settings and metadata, and set up approved CRM automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized CRM actions can change or delete records and enable automations.

Mitigation: Start with read-only actions, use the narrowest Zoho scopes, and confirm each write, deletion, or automation with the user.

Risk: Sending trigger data to an unapproved third-party destination can expose information.

Mitigation: Use third-party destinations only after the user approves the exact host and data flow.

Risk: Handling a long-lived API key directly increases the chance of credential exposure.

Mitigation: Prefer the CLI's OAuth device flow; never log, display, or persist API keys.

## Reference(s):

- [Zoho CRM skill release](https://clawhub.ai/byungkyu/skills/zoho-crm)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Zoho CRM API v8 documentation](https://www.zoho.com/crm/developer/docs/api/v8/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, JSON, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM responses may contain personal data; limit output to fields needed for the task.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
