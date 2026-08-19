## Description:

Code Review helps an agent review diffs, pull requests, or individual files for correctness, security, performance, readability, and test coverage, then return severity-ranked findings and actionable fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to get structured code-review feedback on diffs, pull requests, and individual files. It highlights must-fix and suggested issues with file and line references, including security, correctness, performance, maintainability, and test coverage concerns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes a persistent self-learning script that can write local learning records and may capture sensitive review notes if used carelessly.

Mitigation: Use the learner only when persistent review preferences are explicitly wanted, keep secrets and proprietary details out of learner notes, and remove or disable local learning records when they are not needed.

Risk: Static checklist results and agent review comments may be incomplete or may overstate an issue without full project context.

Mitigation: Treat findings as review guidance, validate blocker and security claims against the relevant code path, and require human approval before applying changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/code-review)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with optional JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity labels, file and line references, actionable remediation steps, and static checklist results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
