## Description:

Analyzes submitted window or balcony videos for possible child climbing hazards and returns a structured report with risk information and a report link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and child-safety staff can submit home or childcare-area videos to review possible window or balcony climbing hazards and retrieve prior analysis reports. This is a video analysis aid, not a verified live safety alarm or substitute for adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Child and home surveillance videos or video URLs are sent to a cloud service for analysis.

Mitigation: Obtain guardian consent and confirm the service's access, retention, and deletion practices before uploading sensitive footage.

Risk: Analysis and report history are associated with a silently created or reused local/cloud identity.

Mitigation: Review identity and report access controls before use, especially on shared devices.

Risk: The release describes real-time alerts, but its bundled code does not demonstrate live camera monitoring or alert delivery.

Mitigation: Do not use it as a real-time safety alarm without independently verified monitoring and alert delivery; maintain adult supervision.

## Reference(s):

- [Child Window/Balcony Climbing Detection release](https://clawhub.ai/18072937735/skills/smyx-child-window-climbing-detection-analysis)
- [Skill API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON and Markdown report listings with links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can be saved to a file; historical reports are retrieved through the cloud service.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
