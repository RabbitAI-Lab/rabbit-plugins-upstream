## Description:

Compose an account grouping recipe and build a grouped account report from local data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business users and developers can turn an account-report request into a grouping recipe, then generate a grouped report from the bundled local records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the bundled Python scripts creates a local CSV report.

Mitigation: Use a dedicated writable output directory and review the returned effect receipt for the created file path.

## Reference(s):

- [Account Group Reporting Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/account-group-reporting-desk)

## Skill Output:

**Output Type(s):** [JSON, CSV file]

**Output Format:** [JSON recipe or grouped report with an effect receipt; local CSV report for the downstream operation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation writes beneath the caller-selected output directory; Python 3.10 or newer is required.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
