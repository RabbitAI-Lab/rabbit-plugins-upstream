## Description:

Generates audience-specific QA test reports, including daily updates, weekly summaries, iteration reports, risk assessments, recommendations, and management-facing quality summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, project managers, and delivery stakeholders use this skill to turn test execution data, defect data, and quality metrics into concise progress, quality, risk, and next-step reports for different audiences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated release or delay recommendations could be mistaken for authorization to make release decisions.

Mitigation: Treat release and delay recommendations as report content only, and require the appropriate owner to approve any release action.

Risk: Broad report-related triggers may activate the skill for non-QA daily or weekly reports.

Mitigation: Narrow or override the trigger in workspaces that contain many non-QA reports.

Risk: Reports may be produced in an unintended language or for the wrong audience.

Mitigation: Specify the desired report language and target audience when requesting the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-reporting)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown test reports and structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports adapt depth, metrics, and sections to the intended audience.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
