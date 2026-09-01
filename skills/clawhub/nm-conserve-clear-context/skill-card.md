## Description:

Manages context overflow by handing off to a fresh subagent at 80% usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to preserve progress during long-running work when context pressure becomes critical. It creates a session-state checkpoint and delegates continuation to a fresh agent so work can continue from documented state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Continuation agents may preserve unattended or dangerous execution mode with limited user checkpoints.

Mitigation: Install only for workflows that intentionally need automated context handoffs, and avoid using it during production changes, credential handling, destructive operations, account or financial actions, or work that should receive fresh approval at each step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-clear-context)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)
- [Session State Module](modules/session-state.md)
- [Session State Schema](modules/session-state-schema.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with checkpoint file templates, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a session-state checkpoint and prompt a continuation agent to resume work.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
