## Description:

Analyzes pet feeding videos to estimate eating duration and speed, provide slow-feeding recommendations, and retrieve past reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, caregivers, and developers can assess feeding videos for rapid eating, review historical reports, and consider slow-feeding interventions. Results are informational and do not diagnose disease or directly control devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet feeding videos or URLs are processed by a provider cloud service.

Mitigation: Use only media you are authorized to share; confirm the provider's media retention and deletion practices before submitting it.

Risk: The skill silently creates or reuses an identity and stores authentication tokens locally.

Mitigation: Review identity and authentication behavior before installation, and protect the workspace and locally stored credentials.

Risk: History requests automatically retrieve cloud reports tied to that identity.

Mitigation: Confirm account access and review report contents before sharing or relying on the returned history.

Risk: Feeding thresholds and intervention suggestions may be mistaken for clinical advice or direct device control.

Mitigation: Treat the output as advisory, confirm any device action separately, and seek veterinary advice for health concerns.

## Reference(s):

- [Pet eating-speed analysis API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown history table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports estimated feeding speed, timing, and advisory slow-feeding actions; does not diagnose disease or operate devices.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
