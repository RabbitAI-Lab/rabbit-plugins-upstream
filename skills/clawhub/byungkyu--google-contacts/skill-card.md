## Description:

Helps agents search, read, and manage Google contacts and contact groups through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with a connected Google account can find contacts, manage contact details and groups, and set up approved contact-related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect account selection or unreviewed write could change or delete personal contacts.

Mitigation: Use read-only calls by default and confirm the account, connection, and exact change before writes or deletes.

Risk: Persistent functions, triggers, or destinations could continue processing or forwarding event data.

Mitigation: Enable automation only with explicit approval and review where its event data will flow.

## Reference(s):

- [ClawHub Google Contacts release](https://clawhub.ai/byungkyu/skills/google-contacts)
- [Maton homepage](https://maton.ai)
- [Google People API](https://developers.google.com/people/api/rest)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Plain text or Markdown with optional commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected contact details from the connected account]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata; skill frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
