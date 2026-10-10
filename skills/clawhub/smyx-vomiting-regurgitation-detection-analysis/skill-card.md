## Description:

Analyzes pet-area camera video for vomiting or regurgitation behaviors and visible vomit, then reports observed events and characteristics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, caregivers, and veterinary staff use this skill to review indoor footage for possible vomiting or regurgitation events, track their frequency, and consult historical reports. Results are visual observations, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet-area footage or video URLs are sent to Life Emergence cloud services.

Mitigation: Share only footage you are comfortable sending to the service, and review its privacy terms before use.

Risk: The skill silently creates or reuses an account and stores an internal identity and tokens in a local workspace database.

Mitigation: Review account creation and local credential storage before installation; restrict access to the workspace.

Risk: History-report lookup may automatically retrieve sensitive past reports when prompted.

Mitigation: Confirm the intended account and whether cloud history access fits your privacy expectations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-vomiting-regurgitation-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Reports, Guidance]

**Output Format:** [JSON or Markdown text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event observations, timestamps, frequency, vomit characteristics, and cloud report history when requested.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
