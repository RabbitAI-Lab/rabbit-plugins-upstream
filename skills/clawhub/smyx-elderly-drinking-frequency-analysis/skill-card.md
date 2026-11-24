## Description:

Analyzes fixed-camera video of a water-cup area to estimate cup pickups and produce drinking-frequency summaries and dehydration-risk reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and elder-care staff use it to review cup-pickup patterns from video and receive reminders when observed activity is low. The resulting counts are behavioral estimates, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and identity details may be sent to a remote provider.

Mitigation: Confirm the provider and destination, understand what data will be sent, and use only authorized footage; the skill documentation recommends silhouette mode for privacy-sensitive scenes.

Risk: Automatic identity and account handling, including credential storage, may expose personal or account data.

Mitigation: Review identity and account behavior and credential handling before use, and proceed only if those practices are acceptable.

Risk: Security evidence reports capabilities beyond the stated drinking-frequency analysis, and the scan was partial.

Mitigation: Review the skill's behavior against the intended use and complete the security review, including the missing reference, before deployment.

Risk: Cup-pickup counts may be mistaken for actual water intake or a medical diagnosis.

Mitigation: Present results as visual behavior estimates and directional reminders only; seek appropriate care for symptoms or ongoing concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured drinking-frequency report with observed counts, timing, risk reminders, and suggested caregiver actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cup pickups are an indirect proxy for drinking; the skill states it does not provide medical diagnoses.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
