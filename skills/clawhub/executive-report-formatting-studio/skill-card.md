## Description:

Set report style guidance and format stakeholder status reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and business teams use this skill to select executive report style guidance and apply it to stakeholder status reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous user requests could select the wrong reporting stage or produce formatting that does not match stakeholder expectations.

Mitigation: State whether the task is style selection or report formatting, then review the returned format_mode or applied_format before sharing the report.

Risk: Formatted executive reports may overemphasize, omit, or misplace supplied identifiers when the source brief is incomplete.

Mitigation: Review rendered_report, included_identifiers, and format_decision against the original brief before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/executive-report-formatting-studio)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [String or structured object containing rendered_report, included_identifiers, and format_decision]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces format_mode for style guidance and applied_format for formatted stakeholder reports.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
