## Description:

Connects an agent to Linear to find and manage issues, projects, teams, cycles, labels, and comments through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using Linear can ask an agent to look up work, update issues, and set up approved automations for their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected account may grant access beyond the immediate task.

Mitigation: Review requested Linear OAuth scopes, prefer read-only access where possible, and approve new connections explicitly.

Risk: Issue changes or automations may modify Linear data.

Mitigation: Confirm the target and intended effect before every mutation or automation.

Risk: Trigger destinations can continuously forward issue or comment data.

Mitigation: Review the destination and event scope, approve each destination separately, and remove it when no longer needed.

## Reference(s):

- [Linear skill on ClawHub](https://clawhub.ai/byungkyu/skills/linear-api)
- [Maton](https://maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Linear GraphQL documentation](https://linear.app/developers/graphql)
- [Linear API and Webhooks](https://linear.app/docs/api-and-webhooks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with Linear results, commands, and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and an authorized Linear connection.]

## Skill Version(s):

1.2.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
