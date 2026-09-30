## Description:

Helps agents send transactional email and manage Resend domains, contacts, templates, broadcasts, and webhooks through a Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can direct an agent to send email, manage Resend resources, and configure approved automations through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends and changes to domains, contacts, templates, or broadcasts can affect real recipients and account data.

Mitigation: Default to read-only actions and obtain explicit approval for writes after checking the connection, recipients, and affected domains.

Risk: Webhooks, trigger destinations, and hosted functions can forward data or run actions persistently.

Mitigation: Confirm destination URLs and the specific task before enabling them, and remove them when no longer needed.

Risk: API-key creation can grant ongoing access to the connected account.

Mitigation: Approve keys only when needed for a specific task and remove them when no longer needed.

## Reference(s):

- [ClawHub Resend skill](https://clawhub.ai/byungkyu/skills/resend-api)
- [Maton](https://maton.ai)
- [Resend API documentation](https://resend.com/docs/api-reference/introduction)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command examples and API request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report results of authorized Resend actions; requires network access and a connected Maton account.]

## Skill Version(s):

1.2.4 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
