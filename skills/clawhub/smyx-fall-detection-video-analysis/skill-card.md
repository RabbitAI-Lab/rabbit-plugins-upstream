## Description:

Analyzes supplied video for possible falls and returns detection reports or cloud-stored report history for home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and developers use this skill to check video for possible falls in home-monitoring settings and retrieve past detection reports. Alerts are for safety awareness and require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-monitoring videos and report history may be sent to the publisher's cloud service.

Mitigation: Obtain informed consent and review the service's data handling before uploading real footage or retrieving history.

Risk: The skill silently creates or reuses a persistent identity and stores account tokens and profile data locally.

Mitigation: Use an approved workspace with explicit consent controls; restrict access to stored credentials and clean up tokens after use.

Risk: Automated fall detection may be mistaken or miss an event.

Mitigation: Treat results as alerts, not definitive safety assessments; arrange prompt human confirmation and appropriate assistance.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [Fall detection API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection results and Markdown report links or history tables; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and safety recommendations.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release; bundled skill frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
