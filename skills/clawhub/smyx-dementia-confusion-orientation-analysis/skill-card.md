## Description:

Analyzes dementia-care video and optional audio for signs of confusion or disorientation, and provides orientation-soothing guidance and reports for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and care teams in homes or dementia-care facilities use the skill to review video and optional audio for possible disorientation, receive structured reports, and plan gentle orientation or escalation with human oversight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive dementia-care audio, video, or URLs may be sent to external cloud services.

Mitigation: Obtain explicit consent before deployment and establish clear retention, deletion, and access controls.

Risk: The skill can silently create or reuse an identity, log in, cache tokens locally, and retrieve cloud history.

Mitigation: Review account creation and token storage before installation; restrict tenant and identity access to authorized caregivers.

Risk: Incorrect soothing or escalation could affect a vulnerable person.

Mitigation: Require caregiver review of soothing and escalation workflows before use in real care settings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API and care workflow reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Structured JSON reports or concise text and Markdown summaries with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return cloud-hosted historical report links and optional saved result files.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release metadata; packaged SKILL.md states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
