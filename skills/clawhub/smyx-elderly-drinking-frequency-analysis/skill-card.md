## Description:

Analyzes video of a water-cup area to count cup pickups as an indirect proxy for older adults’ drinking frequency and flag low counts for caregiver follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Families and care staff can use it to review fixed-camera footage of an older adult’s cup area, track pickup counts and timing, and decide when to check in about drinking. Counts are a visual proxy, not a measurement of fluid intake or a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unclear account creation, token storage, network destinations, video-processing behavior, and persistent account data for review.

Mitigation: Before use, review account and token handling, identify the network endpoints and data handling, and confirm that the video-processing behavior is appropriate for the footage.

Risk: The security review notes insecure HTTP configuration, broad triggers, and unclear behavior for the analysis-free option.

Mitigation: Verify the configured endpoints and transport security, inspect what the analysis-free option does, and limit activation to the intended camera-analysis or history-query tasks.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [Skill usage introduction](https://lifeemergence.com/sample.html)
- [API reference (release artifact)](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured report with pickup counts, timing, risk alerts, recommendations, and report links; JSON or Markdown depending on detail level.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cup pickups are an indirect behavioral proxy and do not establish actual fluid intake or diagnose a medical condition.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
