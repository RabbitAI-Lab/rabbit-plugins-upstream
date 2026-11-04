## Description:

Provides a local MCP and HTTP/SSE hub for agent messaging, task orchestration, shared memory, experience sharing, and web-based administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to connect agents to a shared hub, exchange messages and files, assign and track tasks, and retrieve shared context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verified flaws may expose private agent data or permit access to resources owned by another agent.

Mitigation: Use an isolated, private test instance without sensitive data until event authentication and resource ownership are fixed.

Risk: Approval verification flaws and AppleScript handling may let task text bypass human review or execute commands.

Mitigation: Do not attach powerful executors; disable command-capable integrations or use a sandboxed, least-privilege executor until these issues are fixed.

Risk: Optional LLM execution sends task context to the selected provider.

Mitigation: Avoid sending sensitive context and configure an LLM provider only when its data handling is acceptable.

Risk: Maintenance or token rotation may affect stored hub data.

Mitigation: Back up data before maintenance or token rotation, and run legacy tests only against disposable databases.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liuboacean/skills/agent-comm-hub)
- [Model Context Protocol specification](https://spec.modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [API Calls, Text, Files, Configuration instructions]

**Output Format:** [MCP tool calls and structured responses, including plain text or Markdown messages and task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a running Hub and configured credentials; results depend on Hub state and any configured host executor.]

## Skill Version(s):

3.0.31 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
