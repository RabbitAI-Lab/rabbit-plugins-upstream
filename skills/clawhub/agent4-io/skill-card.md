## Description:

Build and run grounded business agents on agent4.io over MCP, including agents, knowledge bases, load-on-demand skills, stateful Storylines, and page playbooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hellojixian](https://clawhub.ai/user/hellojixian)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and builders use this skill to connect an agent client to agent4.io's remote MCP server and create, configure, verify, and operate grounded business agents, knowledge bases, load-on-demand skills, Storylines, and page playbooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This skill sends user-selected agent configurations, knowledge-base material, queries, and related tenant metadata to agent4.io.

Mitigation: Install it only when agent4.io is intended for the workflow, review material before importing it, and avoid sending data that should not leave the user's environment.

Risk: The required AGENT4_API_KEY grants access to the user's agent4.io tenant.

Mitigation: Treat the API key as sensitive, store it only in the intended agent or MCP client configuration, and rotate or revoke it from the console if exposure is suspected.

Risk: Destructive account or tenant actions can affect production agent4.io resources.

Mitigation: Use the agent4.io console for destructive actions such as deletion or key revocation, and review changes before applying them.

## Reference(s):

- [agent4.io Cookbook](https://agent4.io/cookbook)
- [agent4.io](https://agent4.io)
- [agent4.io MCP Endpoint](https://api.agent4.io/v1/mcp)
- [ClawHub Skill Page](https://clawhub.ai/hellojixian/skills/agent4-io)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include agent4.io console links, API endpoint configuration, and instructions for handling AGENT4_API_KEY.]

## Skill Version(s):

1.1.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
