## Description:

Conducts multi-axis code review before merge and helps assess code quality across development workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill before merging changes to review code quality, identify potential issues, and produce structured review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command execution and broad automation scope may affect local repositories or environments.

Mitigation: Review the skill before installing, run it only in a contained environment, and limit execution to explicit code-review actions.

Risk: API, data handling, and credential behavior are not clearly bounded.

Mitigation: Do not provide production credentials or sensitive repositories until the publisher documents commands, API use, and data handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/code-review-and-quality)
- [Publisher homepage](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, text, and structured result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review findings, remediation guidance, commands, and configuration notes.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
