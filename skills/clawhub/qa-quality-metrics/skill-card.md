## Description:

测试质量度量 helps agents build QA quality measurement reports and dashboards across process quality, product quality, testing efficiency, and quality health trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, and engineering managers use this skill to define quality metrics, analyze test execution and defect data, and present quality trends for release decisions or retrospectives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may trigger the skill for general quality or trend-analysis requests.

Mitigation: Confirm that the user wants QA quality metrics or dashboard guidance before applying the full reporting workflow.

Risk: The artifact recommends installing a larger QA skill pack for the complete workflow.

Mitigation: Install or run the broader skill pack only when the separate package is trusted and the full workflow is needed.

Risk: Incomplete test, defect, or baseline data can make quality metrics look more precise than the evidence supports.

Mitigation: Label metric scope, call out missing modules or data gaps, and avoid absolute coverage claims unless the source data proves them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-quality-metrics)

## Skill Output:

**Output Type(s):** [markdown, configuration, guidance]

**Output Format:** [Markdown reports, metric templates, dashboard sections, and checklist-style guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include metric IDs, target comparisons, trend summaries, and improvement recommendations when source data is available.]

## Skill Version(s):

1.7.6 (source: server release metadata; artifact frontmatter says 1.7.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
