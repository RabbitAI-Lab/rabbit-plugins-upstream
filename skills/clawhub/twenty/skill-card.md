## Description:

Helps agents work with Twenty CRM companies, people, opportunities, notes, tasks, and workflows through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a Twenty CRM workspace use this skill to look up and update customer records, track deals and activities, and set up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton connection grants access to customer and contact data.

Mitigation: Prefer OAuth, authorize only needed scopes, and limit displayed records to fields needed for the task.

Risk: Writes and new connections can change CRM data or expand access.

Mitigation: Start with read-only requests and obtain explicit user confirmation before every write or new connection.

Risk: Hosted functions, triggers, and destinations can persist and forward data after setup.

Mitigation: Require explicit approval, scope automation narrowly, and remove it when no longer needed.

Risk: A long-lived API key used without the CLI can leak through process environments or logs.

Mitigation: Use OAuth through the CLI where possible; never print or persist the API key.

## Reference(s):

- [Twenty CRM skill release](https://clawhub.ai/byungkyu/skills/twenty)
- [Twenty API documentation](https://docs.twenty.com/developers/extend/api)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CRM data summaries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CRM responses may contain personal data; disclose only fields needed for the request.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
