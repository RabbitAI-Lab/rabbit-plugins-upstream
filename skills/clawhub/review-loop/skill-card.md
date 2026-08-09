## Description:

Run a bounded review-and-fix loop with fresh, read-only reviewer subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wufei-png](https://clawhub.ai/user/wufei-png)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run a bounded delegated code review loop, verify reviewer findings, apply accepted fixes, rerun relevant tests, and summarize remaining risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reviewer findings or accepted fixes may be incorrect or incomplete.

Mitigation: The primary agent verifies each finding before accepting it and reports unaccepted findings, unverified items, and residual risk.

Risk: Applied fixes may introduce regressions.

Mitigation: The workflow reruns relevant tests after each accepted fix and summarizes verification results.

## Reference(s):

- [Review Loop on ClawHub](https://clawhub.ai/wufei-png/skills/review-loop)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown summary with findings, decisions, fixes, verification results, and remaining risks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code edits and test commands when accepted fixes are applied.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
