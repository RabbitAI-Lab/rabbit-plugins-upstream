## Description:

Compares FAQ knowledge-base files with gold-tier customer-service dialogue records to find inconsistent, outdated, missing, or vague entries and produce reports and prioritized recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

Customer support, quality assurance, and knowledge-management teams use this skill to audit FAQ content against strong support dialogue examples before policy changes, quality reviews, and training updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FAQ and customer-service dialogue files may contain customer personal information.

Mitigation: Remove or mask personal information before using the skill, especially names, phone numbers, order numbers, and other customer identifiers.

Risk: The helper script prints source file contents into the agent analysis context.

Mitigation: Use only files that the agent is intended to read and avoid submitting sensitive or unnecessary records.

Risk: Incorrect comparison results could lead teams to update a knowledge base with misleading guidance.

Mitigation: Review generated discrepancy reports and optimization suggestions against source dialogue evidence before changing production FAQ content.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zenobiazizi/skills/skill-knowledge-base-health-check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and prioritized recommendation lists, with helper-script text extraction for supported input files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.10+ and pandas with openpyxl or xlrd for Excel input; artifact guidance recommends files no larger than 10 MB.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
