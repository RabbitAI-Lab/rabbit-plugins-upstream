## Description:

Helps agents post, inspect, cancel, and poll authenticated ~alter standing identity-trait orders while respecting opt-in requirements and priced reveal behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to maintain ongoing requirements for people matching specific identity trait ranges, then collect eligible matches over time. It also guides authenticated management of the caller's own standing orders, existing matches, and opt-in state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create standing identity-match requirements on a remote service.

Mitigation: Use authenticated accounts only, confirm the operator's intent before creating requirements, and cancel requirements when they are no longer needed.

Risk: Polling delivered matches can spend $0.01 per reveal.

Mitigation: Set an explicit budget before polling, avoid unattended polling loops, and stop once the budget or task goal is reached.

Risk: The workflow depends on an authenticated ~alter API key.

Mitigation: Store ALTER_API_KEY securely, do not invent placeholder credentials, and avoid exposing the key in logs or shared output.

## Reference(s):

- [~alter MCP server](https://mcp.truealter.com/api/v1/mcp)
- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-identity-orderbook)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with tool names, configuration details, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ALTER_API_KEY for authenticated ~alter orderbook operations.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
