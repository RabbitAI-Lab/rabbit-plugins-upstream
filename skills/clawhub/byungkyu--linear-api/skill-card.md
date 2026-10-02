## Description:

Connects an agent to Linear through Maton to query and manage issues, projects, teams, cycles, labels, and comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Linear users can ask an agent to find, create, and update issues and inspect projects, teams, and cycles in an authorized Linear account. With separate approval, they can also configure ongoing event-based or scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account grants access to its authorized Linear data.

Mitigation: Obtain approval before connecting; use only necessary accounts and scopes, prefer read-only access, and revoke unused connections.

Risk: Writes may change or delete Linear records or trigger downstream actions.

Mitigation: Verify the account and target, then confirm the exact mutation and its effect with the user before execution.

Risk: Triggers, hosted functions, or destinations can persist and forward future event data.

Mitigation: Review each workflow and destination separately, including recipient, payload, frequency, and persistence; require explicit approval and remove unneeded automations.

Risk: Raw API keys or sensitive responses could be exposed in logs, files, or destination payloads.

Mitigation: Prefer CLI OAuth, never print or embed credentials, and limit returned or forwarded data to what the task requires.

## Reference(s):

- [Linear skill release](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Linear GraphQL documentation](https://linear.app/developers/graphql)
- [Linear trigger reference](references/linear/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Natural-language responses with optional Markdown, commands, or code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may summarize data from the connected Linear account; workflows can continue running after the conversation ends.]

## Skill Version(s):

1.2.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
