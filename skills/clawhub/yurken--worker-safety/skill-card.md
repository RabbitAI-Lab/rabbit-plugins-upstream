## Description:

Operations Safety Reference - Hard Limits apply unconditionally for OpenClaw agent operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yurken](https://clawhub.ai/user/yurken)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to enforce OpenClaw operational safety limits, refuse unsafe administration requests, and guide safer alternatives during private or group-chat workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives itself broad, unconditional authority to override user-directed administration and resist removal.

Mitigation: Install only when this refusal posture is intended, and maintain an out-of-band administrative process to inspect, modify, disable, or remove the skill when legitimate maintenance is needed.

Risk: Strict hard limits may cause agents to refuse legitimate maintenance or configuration tasks.

Mitigation: Review the listed limits before deployment and document owner-approved maintenance paths outside the worker session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yurken/skills/worker-safety)
- [ClawHub publisher profile](https://clawhub.ai/user/yurken)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown or plain-text safety guidance and refusal language]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-executable guidance; no API keys, scripts, tool calls, or MCP references were detected.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
