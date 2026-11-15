## Description:

Debugging assistant. Analyzes error logs, suggests breakpoints, traces execution flow, and helps identify root causes of issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[michealxie001](https://clawhub.ai/user/michealxie001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to analyze Python and C/C++ errors, identify likely root causes, choose useful breakpoint locations, and inspect function execution paths while debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically imports a sibling c-support/lib parser when present, which may run unreviewed code at startup.

Mitigation: Review or remove the automatic import before installation; package, pin, or explicitly configure any C parser dependency.

## Reference(s):

- [OpenClaw Debugging Assistant on ClawHub](https://clawhub.ai/michealxie001/skills/oc-debugging)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Plain text and markdown-style terminal guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested fixes, file and line locations, breakpoint recommendations, function-call summaries, and GDB commands.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
