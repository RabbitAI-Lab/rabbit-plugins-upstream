## Description:

Formats a status report for stakeholders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Teams preparing stakeholder updates use this skill to format a status report and record a local preview. A configured delivery destination can also receive the report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery endpoint can receive report contents and local artifact paths, beyond a local formatting preview.

Mitigation: Leave CLAWHUB_DELIVERY_ENDPOINT and delivery configuration unset unless submission to that destination is intended.

Risk: Reports may expose access identifiers or other business data in the preview or delivered content.

Mitigation: Avoid verbatim identifiers unless needed, use a dedicated output directory, and review the report before sharing.

## Reference(s):

- [Status Report Formatter on ClawHub](https://clawhub.ai/wxt-ai/skills/report-style-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON result containing a formatted report, identifier list, and formatting decision; local Markdown preview]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a preview beneath the selected output directory and returns a delivery receipt when delivery is configured.]

## Skill Version(s):

1.1.1 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
