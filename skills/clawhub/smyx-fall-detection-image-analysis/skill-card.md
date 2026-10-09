## Description:

Analyzes images and short videos for possible falls in a target area and provides a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, families, and care-facility staff can screen images or short video clips for possible falls and review past detection reports. Results are advisory and require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive care footage and media URLs are sent to the configured LifeEmergence cloud APIs.

Mitigation: Verify provider privacy, retention, access-control, and consent practices before uploading real footage.

Risk: Report history is tied to a persistent local or remote identity that may be created silently.

Mitigation: Prefer an explicit platform-provided identity and review who can access historical reports.

Risk: A possible-fall assessment may be mistaken for a confirmed emergency decision.

Mitigation: Confirm suspected falls with a person and follow the appropriate emergency response process.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown analysis report with risk notes and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports historical report listings and optional file output.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
