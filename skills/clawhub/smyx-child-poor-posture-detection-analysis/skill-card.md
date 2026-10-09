## Description:

Analyzes children's seated posture in camera footage and provides estimated posture measurements, reminders, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, guardians, and developers of study-area monitoring tools can analyze a child's posture video, receive reminder text, and view current or historical posture reports. Results are visual estimates, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's posture media and report history are processed through Life Emergence cloud services.

Mitigation: Obtain guardian consent and confirm retention, deletion, and access controls for reports and snapshot links before use.

Risk: The skill silently creates or reuses persistent user identities and stores tokens locally.

Mitigation: Review whether local token storage in the workspace database is acceptable and restrict access to that storage.

Risk: Camera-derived spinal-angle estimates may be mistaken for clinical measurements.

Mitigation: Use results for posture reminders only, not diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis)
- [Posture analysis API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Report links]

**Output Format:** [Text or Markdown containing structured results and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file and present historical reports as a Markdown table.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
