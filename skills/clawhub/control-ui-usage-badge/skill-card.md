## Description:

Shows per-message token usage, cache details, duration, throughput, model, and cost under assistant messages in the OpenClaw Control UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xhughyn](https://clawhub.ai/user/xhughyn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use this skill to patch the local Control UI so browser chat messages display token usage and related runtime metrics. It is useful when Control UI webchat usage is not covered by deliverable-channel usage footers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persistently patches installed Control UI files and can reapply itself after updates.

Mitigation: Inspect the scripts before use, run only on an intended Control UI installation, and avoid the optional recurring re-apply unless persistent patching is desired.

Risk: The apply and remove scripts may use sudo automatically when the Control UI directory is not writable.

Mitigation: Prefer a user-writable OpenClaw installation path or set OPENCLAW_CONTROL_UI_DIR deliberately so privilege boundaries are clear before execution.

Risk: The browser patch intercepts Control UI WebSocket message frames to annotate displayed assistant messages.

Mitigation: Deploy only where local UI modification is acceptable, then verify status with scripts/status.sh and use scripts/remove.sh to roll back.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xhughyn/skills/control-ui-usage-badge)
- [Publisher profile](https://clawhub.ai/user/xhughyn)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown instructions with bash commands and JavaScript configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local UI patching guidance and status or rollback commands; no model output artifacts are generated.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
