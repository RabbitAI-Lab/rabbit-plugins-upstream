## Description:

Analyzes bathroom doorway video to track occupancy and flag stays exceeding a 30-minute threshold for caregiver review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care teams use the skill to review occupancy alerts and historical monitoring reports for older adults. Alerts prompt a human check rather than a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bathroom-monitoring video may expose highly sensitive personal details when sent to cloud services.

Mitigation: Obtain explicit consent from the monitored person or authorized caregiver; prefer doorway-only or pre-blurred footage and avoid uploading raw private bathroom video.

Risk: Cloud report history and locally stored identity or tokens may be accessed or retained beyond the user's expectations.

Mitigation: Confirm the publisher's retention and access controls, and restrict access to the workspace data directory.

Risk: An occupancy alert cannot establish whether a person needs medical attention.

Mitigation: Have a caregiver promptly verify urgent alerts directly; do not treat the result as a medical diagnosis.

## Reference(s):

- [API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-toilet-time-abnormal-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text and Markdown report links, with JSON data in reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Occupancy alerts, report summaries, and cloud history links]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
