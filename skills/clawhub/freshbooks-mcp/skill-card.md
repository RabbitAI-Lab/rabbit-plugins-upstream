## Description:

Helps agents access FreshBooks accounting, project, and time-tracking data from a shell using OAuth-authenticated requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance teams use this skill to query FreshBooks records from a shell without running an MCP server, and to prepare accounting updates when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can create or change live accounting records and send estimates to customers.

Mitigation: Test with a FreshBooks test account first; review and explicitly authorize every POST or PUT command before execution.

Risk: OAuth tokens stored on disk or exposed in shell logs could allow unauthorized account access.

Mitigation: Keep the token state file private and avoid shell tracing or logging around token commands.

## Reference(s):

- [FreshBooks curl recipes](artifact/references/recipes.md)
- [FreshBooks developer portal](https://my.freshbooks.com/#/developer)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/freshbooks-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples can include live FreshBooks write requests.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
