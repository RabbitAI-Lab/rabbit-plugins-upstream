## Description:

Sailing Sports Skill helps agents answer natural-language questions about table tennis, football, and motorsport events, schedules, scores, rankings, player or driver updates, and standings through a sports-data MCP service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liyongfen2025](https://clawhub.ai/user/liyongfen2025)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to query live or recent sports data for table tennis, football, and motorsport, including schedules, results, rankings, standings, and participant information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow connects to the sailing.sports.qq.com MCP endpoint.

Mitigation: Confirm that the user trusts sailing.sports.qq.com before installation or configuration.

Risk: Setup may install mcporter globally if it is not already available.

Mitigation: Proceed only after explicit user confirmation, or install mcporter manually according to local package-management policy.

Risk: The Sailing token may be stored in local mcporter configuration as an Authorization header.

Mitigation: Use a scoped or short-lived token when possible, restrict access to local mcporter configuration, and remove the sailing-sports-mcp config when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liyongfen2025/skills/sailing-skill)
- [Sailing Sports MCP endpoint](https://sailing.sports.qq.com/api/tteagent/sport_pub/mcp)
- [Sailing Sports token application](https://sailing.sports.qq.com/open/token-apply)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON tool arguments; MCP responses are JSON sports data presented as tables or lists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SAILING_TAI_IT_TOKEN for authenticated MCP calls.]

## Skill Version(s):

1.0.23 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
