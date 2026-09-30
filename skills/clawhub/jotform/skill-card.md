## Description:

Helps agents access JotForm forms and submissions through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People using JotForm can ask an agent to list forms, inspect submissions, and, with explicit approval, create forms or manage webhooks and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing a connection or writing to JotForm may affect forms and submissions.

Mitigation: Use read-only actions by default and obtain explicit approval for each new connection or write.

Risk: Webhooks and trigger destinations can continuously forward future submission or event data.

Mitigation: Confirm the exact destination, data, and persistence with the user before creation; review existing forwarding and remove it when no longer needed.

Risk: JotForm access passes through Maton as an OAuth/API gateway.

Mitigation: Use only connections and scopes the user authorizes, and do not expose access tokens or API keys.

## Reference(s):

- [JotForm skill release](https://clawhub.ai/byungkyu/skills/jotform)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Scheduled trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON responses]

**Output Format:** [Text and Markdown with command examples and API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account, network access, and authorization for the requested JotForm actions.]

## Skill Version(s):

1.2.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
