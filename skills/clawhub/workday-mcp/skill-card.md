## Description:

Read Workday HR data such as org charts, worker profiles, pay, benefits, compensation, performance, and task or data cards through a user's own signed-in Workday session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and authorized workplace users use this skill to let an agent retrieve Workday information that is visible in their own signed-in session, including people, team, compensation, benefits, performance, and Workday app data. Developers can also use it to configure read-only MCP access to Workday through the fetchproxy browser extension.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive HR information that is visible in the user's signed-in Workday session, including compensation, benefits, and performance records.

Mitigation: Install only in trusted environments, follow the employer's acceptable-use policy, and require explicit user intent before reading sensitive Workday records.

Risk: Broad Workday-related triggers can lead an agent to access Workday data in more situations than the user intended.

Mitigation: Keep the MCP and browser extension limited to trusted agent sessions and review agent requests before allowing reads of people, pay, benefits, or performance data.

Risk: The skill depends on a live browser extension bridge that reuses the user's existing SSO-authenticated Workday session.

Mitigation: Use the extension only on trusted machines and disable or disconnect it when Workday access is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [workday-mcp source repository](https://github.com/chrischall/workday-mcp)
- [fetchproxy extension source repository](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [JSON, Guidance, Configuration]

**Output Format:** [Structured JSON responses with Markdown setup guidance and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday access through a live signed-in browser session; some deep reads default to compact responses that strip media fields.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
