## Description:

Analyzes videos of vehicle drivers to identify unsafe driving behaviors and generate professional analysis reports to help enhance road safety awareness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Drivers and road safety educators use the skill to review driving videos for unsafe behaviors such as fatigue, distraction, or missing seatbelts, and receive a structured assessment with safety suggestions. The report is for safety education and does not replace professional driver training.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private footage may still be uploaded when the no-analysis option is used.

Mitigation: Require this behavior to be fixed and verified before using private footage, and confirm the service's upload, retention, and report-access terms.

Risk: Account tokens remain locally after use, creating a credential privacy risk.

Mitigation: Review and protect local token storage before using sensitive credentials.

Risk: The --api-url option currently does not redirect uploads.

Mitigation: Do not rely on this option to control the upload destination; confirm the service endpoint before sending footage.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured driving behavior assessment with identified risks, safety suggestions, and report links; available as JSON or Markdown text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports concise, standard, and JSON detail levels.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
