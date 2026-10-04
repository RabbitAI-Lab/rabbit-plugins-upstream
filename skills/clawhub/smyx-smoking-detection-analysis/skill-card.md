## Description:

Analyzes images and videos for potential smoking violations and provides detection reports and cloud-based report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Facilities and safety teams use the skill to review images or videos for possible smoking in restricted areas and consult detection reports. Results are advisory and require human review before enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local images, videos, or submitted media URLs may be sent to the vendor's cloud service.

Mitigation: Use only approved media and ask the publisher to document what is transmitted and how it is retained or deleted before installation.

Risk: The skill creates or reuses user identities and retains identifiers and service tokens in a workspace SQLite database.

Mitigation: Review the authentication flow, local data handling, and report-history access controls before approving use.

Risk: The bundled API documentation describes pet-health analysis rather than smoking detection.

Mitigation: Request corrected smoking-detection API documentation and verify endpoints before relying on the integration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference (pet-health endpoints; verify applicability)](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Detection report text or JSON, with Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to cloud-hosted reports]

## Skill Version(s):

1.0.15 (source: ClawHub server release; bundled frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
