## Description:

Analyzes aquarium video to identify fish that remain separated from their school and provide behavior alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists and aquaculture operators use this skill to review video for persistent fish isolation, receive behavior alerts, and consult past analysis reports. Its observations are not a disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or video URLs are sent to the publisher's cloud service.

Mitigation: Obtain explicit user confirmation before uploading or submitting a video URL.

Risk: The skill can create or reuse an identity and store access tokens locally.

Mitigation: Review identity and token storage before installation; restrict workspace access to trusted users.

Risk: History queries can access cloud-stored, account-scoped reports.

Mitigation: Confirm user intent before querying report history.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-isolation-detection-analysis)
- [Fish isolation API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Text and Markdown summaries of structured analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include fish isolation alerts, suggested checks, and links to cloud-stored reports.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
