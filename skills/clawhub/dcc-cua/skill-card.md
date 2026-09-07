## Description:

Project-owned DCC-CUA routing skill for bounded application UI automation with a fail-closed provider boundary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a task explicitly requires the DCC-CUA route for application or browser UI control. It keeps observation, input, target binding, and final-state verification on the DCC-MCP UI-control path rather than substituting a generic computer-use provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route an agent to drive application or browser UI through DCC-CUA.

Mitigation: Install and use it only for trusted UI tasks that intentionally require the DCC-CUA/DCC-MCP UI-control route.

Risk: Repair or installation may fetch or reconcile the DCC-CUA runtime component.

Mitigation: Allow component repair or installation only when the DCC-MCP component source is trusted and the action is authorized.

Risk: UI actions against the wrong process, window, tab, or stale observation could affect the wrong target.

Mitigation: Bind the exact PID, native window handle, and browser target when available, refresh observations before state-dependent actions, and verify the destination state after mutations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/loonghao/skills/dcc-cua)
- [Project homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exact target binding, fresh observations before state-dependent actions, and final-state verification.]

## Skill Version(s):

0.19.100 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
