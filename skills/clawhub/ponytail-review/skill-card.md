## Description:

Reviews code changes for bugs, security risks, load issues, missing tests, performance problems, and unnecessary code, with concrete fixes for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dietrichgebert](https://clawhub.ai/user/dietrichgebert)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review repository changes and receive prioritized, actionable findings without modifying code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review requires reading repository changes and related files, which may contain sensitive information.

Mitigation: Limit repository access to the intended review scope and avoid reproducing secrets in the report.

Risk: A review may overlook defects or report an issue that does not occur.

Mitigation: Check each finding against the changed lines, callers, and tests before acting on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dietrichgebert/skills/ponytail-review)
- [Project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown review report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prioritized, numbered findings with concrete examples and fixes; no code changes.]

## Skill Version(s):

5.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
