## Description:

Agent Evolution helps OpenClaw agents persist behavior rules, track rule execution and violations, maintain identity-like state, and detect repeated or drifting behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linglin6](https://clawhub.ai/user/linglin6)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to track whether behavioral rules are followed, record violations, persist identity-like state, and surface repeated-operation or debug-loop patterns for OpenClaw agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent behavior rules, pattern logs, and identity-like state may retain sensitive or stale information across sessions.

Mitigation: Review or delete ~/.openclaw/workspace/.agent-evolution/state.json when persistent state is no longer wanted, and avoid storing sensitive or untrusted content through identity updates.

Risk: Automatically extracted behavior rules from AGENTS.md or SOUL.md may capture outdated or inappropriate instructions.

Mitigation: Review generated rules with the stats and report commands, then reset or remove unsuitable state before relying on the skill.

## Reference(s):

- [Agent Evolution on ClawHub](https://clawhub.ai/linglin6/skills/agent-evolution)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON command output with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists local state at ~/.openclaw/workspace/.agent-evolution/state.json.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
