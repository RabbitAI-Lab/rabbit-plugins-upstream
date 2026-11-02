## Description:

Analyzes videos for mental-health and behavioral tendencies and returns structured reports with suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People seeking a video-based mental-health reference can use the skill to request a structured analysis or retrieve prior reports. Its results are informational and do not replace assessment or care from a qualified mental-health professional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive footage may be uploaded even when the no-analysis option is used.

Mitigation: Use test footage until this behavior is resolved, and obtain permission from people shown before uploading identifiable footage.

Risk: Account enrollment, credential storage, and destination safeguards are unclear.

Mitigation: Restrict credentials to approved HTTPS destinations and clarify enrollment, token storage, and deletion controls before use.

Risk: The remote service's behavior and retention policy have not been verified.

Mitigation: Confirm the provider's data handling and retention terms before submitting identifiable footage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports and history results as text or JSON; report lists can be presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes analysis findings, suggestions, warnings, and report links when returned by the service.]

## Skill Version(s):

1.0.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
