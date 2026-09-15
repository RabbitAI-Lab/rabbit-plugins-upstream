## Description:

Agent Loop Guard helps developers and agent operators detect runaway loops by checking step caps, repeated actions, and no-progress traces, then producing a circuit-breaker recommendation and diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to guard agent runs against infinite loops, repeated tool calls, and token waste. It can review action traces, recommend when to stop execution, and return a concise diagnosis for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install instructions recommend an unpinned global npx command that can execute mutable third-party code.

Mitigation: Inspect and copy the specific agent-loop-guard files manually, or pin the installer and repository commit, and avoid running installation from an elevated shell.

Risk: Loop decisions are based on trace patterns and may not capture every task-specific reason for repeated actions.

Mitigation: Use the diagnosis as a guardrail signal and have a human review critical stop or continue decisions.

## Reference(s):

- [Agent Loop Guard on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-loop-guard)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD Theory](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Analysis]

**Output Format:** [Markdown guidance with optional plain-text or JSON CLI diagnostics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local trace analysis; no third-party runtime dependencies in the loop checker.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
