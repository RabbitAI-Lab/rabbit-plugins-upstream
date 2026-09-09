## Description:

This skill helps agents work with AllTrails hiking and trail data, including trail search, trail details, reviews, photos, weather, saved lists, completed trails, and activity feed information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect an agent to read-only AllTrails trail discovery and signed-in account data for planning hikes, reviewing trail context, and summarizing personal hiking history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the signed-in browser session and can expose account-linked AllTrails data such as saved lists, completed trails, and activity feed information.

Mitigation: Install only when that read-only account data access is acceptable, and invoke personal-data tools only for users who understand the session dependency.

Risk: Setup uses an unpinned `npx -y alltrails-mcp` command.

Mitigation: Review or pin the npm package version before deployment in controlled environments.

Risk: The AllTrails integration depends on a signed-in browser tab and reverse-engineered internal AllTrails behavior that may change or be subject to AllTrails terms.

Mitigation: Use the integration at the account owner's discretion, keep the browser session explicit, and run the healthcheck when AllTrails requests fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/alltrails)
- [npm package: alltrails-mcp](https://www.npmjs.com/package/alltrails-mcp)
- [Source repository listed by artifact](https://github.com/chrischall/alltrails-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AllTrails data access; compact results are the default unless full records are requested.]

## Skill Version(s):

2.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
