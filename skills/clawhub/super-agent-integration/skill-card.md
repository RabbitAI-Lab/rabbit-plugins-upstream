## Description:

Runs a local end-to-end autonomous agent loop that coordinates planning, execution, verification, reflection and replanning, memory, and regression evaluation, then reports whether the loop is usable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent engineers use this skill to run self-tests and custom task runs that measure an autonomous agent loop across verification, replanning, memory coverage, regression status, and health scoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create durable local memory about usage, failures, notes, and preferences without clearly documented limits or consent.

Mitigation: Review before installing, avoid storing secrets or sensitive task details in learner notes, and disable or remove learner writeback behavior unless cross-session memory is explicitly wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/super-agent-integration)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON health reports and Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports verification gate, replan count, reason verification rate, evaluation pass rate, regression status, memory coverage, health score, and verdict.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
