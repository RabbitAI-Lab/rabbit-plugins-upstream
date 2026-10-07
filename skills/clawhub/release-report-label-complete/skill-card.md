## Description:

Turns a release configuration entry into a local stakeholder report and optionally delivers it to a configured email or HTTP destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams and developers use this skill to turn a configuration entry into a stakeholder-ready Markdown report, save it locally, and optionally deliver it to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send report contents and a local file path to an external destination.

Mitigation: Review the destination, report contents, and API key before enabling delivery; keep delivery unconfigured for local-only use.

Risk: Existing delivery or SMTP environment variables can enable unintended external submission.

Mitigation: Check and clear unrelated CLAWHUB_* and SMTP_* variables before running the skill.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wxt-ai/skills/release-report-label-complete)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Local Markdown report and JSON result with artifact and delivery receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-only by default; configured email or HTTP delivery returns a delivery receipt.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
