## Description:

Prepares a release configuration entry and builds a stakeholder configuration report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to turn configuration notes into structured entries and local Markdown reports for stakeholders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downstream operation writes a local Markdown report to the selected output directory.

Mitigation: Review the output directory before running downstream and inspect the generated report.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wxt-ai/skills/release-configuration-report-desk)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [JSON response with a Markdown report entry; local Markdown file when downstream runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upstream returns configuration_entry; downstream returns report_entry and writes a local report in the selected output directory.]

## Skill Version(s):

3.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
