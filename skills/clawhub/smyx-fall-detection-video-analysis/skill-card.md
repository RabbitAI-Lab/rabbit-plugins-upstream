## Description:

Detects falls in a target area from video input and returns structured monitoring results for home safety scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, and developers use this skill to analyze a local video file or video URL for fall events in monitored home areas and to retrieve structured results or historical reports. Its output supports safety alerting and should be confirmed by a person before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or video URLs are sent to the publisher's remote service for analysis.

Mitigation: Confirm that users and operators are comfortable with remote processing of fall-detection media before installation or use.

Risk: The skill auto-creates or reuses identity-linked remote sessions and report history.

Mitigation: Review how the service creates accounts, stores tokens, retains reports, and supports revocation or deletion of linked history.

Risk: The published artifact includes private or development HTTP endpoint defaults.

Mitigation: Ask the publisher to remove those defaults or explain why they are included, and review endpoint configuration before deployment.

Risk: Fall-detection output may be incomplete or incorrect in safety-critical situations.

Mitigation: Use results as safety alerts only and require human confirmation for suspected falls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON-style structured analysis text with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a file and can list historical reports through the publisher service.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
