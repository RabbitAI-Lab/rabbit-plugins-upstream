## Description:

Creates audience-specific QA test reports that summarize progress, defects, quality metrics, and risks for teams and decision-makers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and project teams use this skill to turn test execution and defect data into daily, weekly, iteration, or specialized reports tailored to developers, managers, and stakeholders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Release or delay recommendations could be mistaken for authorization to act.

Mitigation: Treat them as report fields and require an authorized decision before changing release plans.

Risk: Broad report-related phrases may activate the skill outside a QA context.

Mitigation: Confirm that the request concerns testing, defects, coverage, or release quality before using it.

Risk: Example metrics or conclusions may not reflect actual project data.

Mitigation: Check report figures and conclusions against the provided test and defect records, and mark missing coverage.

## Reference(s):

- [ClawHub qa-test-reporting release](https://clawhub.ai/kokxi/skills/qa-test-reporting)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown reports and templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include a report ID, linked case and defect IDs, quantitative metrics, risk assessments, and release recommendations.]

## Skill Version(s):

1.7.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
