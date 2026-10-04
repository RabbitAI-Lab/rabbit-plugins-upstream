## Description:

Analyzes dementia-care video and optional audio for signs of confusion or disorientation and returns structured findings and orientation-soothing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams and family caregivers use this skill to review camera footage and optional audio for possible disorientation, obtain analysis reports, and plan gentle orientation support. Findings are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive dementia-care video, audio, URLs, and identity-linked reports are sent to cloud services.

Mitigation: Obtain resident or legal-guardian consent and confirm the care setting permits this processing before providing media or URLs.

Risk: Identity tokens and account data may be stored locally in the workspace data directory.

Mitigation: Review local storage and access controls before installation, and restrict access to token and database files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [JSON or text report with optional report links and history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a user-specified file; caregiver review is needed before acting on findings.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
