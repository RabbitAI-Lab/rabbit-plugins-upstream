## Description:

Helps agents and members check their ~alter account status, key validity, scopes, trust tier, portfolio, and remaining privacy budget before sensitive queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, members, and operators use this skill to understand what an authenticated ~alter account can currently do, diagnose authentication or scope failures, review trust standing, and check privacy-budget posture before sensitive trait queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an Alter API key to query account status and portfolio information from the hosted MCP service.

Mitigation: Configure only an ALTER_API_KEY intended for use with this service, and keep the key in the agent environment rather than in prompts or shared text.

Risk: Privacy-budget checks can involve another person's allocation before sensitive trait queries.

Mitigation: Use the skill's privacy-budget guidance before sensitive reads and treat budget classes as coarse planning signals rather than private counter values.

## Reference(s):

- [~Alter Skill Page](https://clawhub.ai/true-alter/skills/alter-my-standing)
- [~Alter MCP Endpoint](https://mcp.truealter.com/api/v1/mcp)
- [~Alter Publisher Profile](https://clawhub.ai/user/true-alter)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, text]

**Output Format:** [Markdown with inline tool names, endpoint configuration, and credential-handling guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the ALTER_API_KEY environment variable and the configured ~alter MCP server when an agent follows the skill.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
