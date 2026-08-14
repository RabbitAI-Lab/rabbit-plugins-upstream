## Description:

Enables an agent to coordinate with its own future and concurrent sessions by recording handovers, advisory locks, work offers, structured questions, and event-stream updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[true-alter](https://clawhub.ai/user/true-alter)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to coordinate their own agent sessions across restarts and concurrent runs. It supports handovers, advisory locks, work delegation, event subscription, and structured questions to the user's own principal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The hosted MCP service stores and retrieves agent coordination events.

Mitigation: Install only when this storage model is acceptable, and keep handover bodies and file references free of secrets or sensitive private data.

Risk: Locks, work claims, and coordination frames are advisory rather than enforced safety controls.

Mitigation: Check current state before changing shared files or branches, and treat lock and claim results as coordination signals rather than guarantees.

Risk: All tool use depends on ALTER_API_KEY authentication.

Mitigation: Protect the key, avoid pasting it into prompts or handover bodies, and verify login status before rotating or replacing a live key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/true-alter/skills/alter-agent-channel)
- [~Alter hosted MCP endpoint](https://mcp.truealter.com/api/v1/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, configuration details, and operational caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ALTER_API_KEY. Handover bodies are capped at 8 KiB according to the artifact text.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
