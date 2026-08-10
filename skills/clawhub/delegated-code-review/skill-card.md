## Description:

Perform a single review with a fresh, read-only subagent, then verify findings and apply accepted fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wufei-png](https://clawhub.ai/user/wufei-png)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run a structured delegated code review, verify reported findings, apply accepted fixes, rerun relevant tests, and summarize remaining risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reviewer subagent may report incorrect or low-value findings.

Mitigation: The main agent verifies each finding before accepting it, records rejected findings with reasons, and only applies accepted fixes.

Risk: Accepted fixes can introduce regressions if they are not checked after implementation.

Mitigation: The skill instructs the agent to rerun relevant tests after each accepted fix.

## Reference(s):

- [Delegated Code Review on ClawHub](https://clawhub.ai/wufei-png/skills/delegated-code-review)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown summary with findings, decisions, fixes, verification results, unverified items, and remaining risks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code edits and test commands when accepted review findings require fixes]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
