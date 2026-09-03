## Description:

Audits changes for additive bias and Iron Law compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and code reviewers use this skill after implementation or before merging to audit local git diffs for additive bias, test expectation changes, and minimal-intervention justification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can appear in general code-review situations and push for strict justification of added code and test changes.

Mitigation: Use it where a quality-gate reviewer is desired, or narrow triggers to explicit invocation for lighter workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-justify)
- [Declared homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review guidance over a single code-change delta.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
