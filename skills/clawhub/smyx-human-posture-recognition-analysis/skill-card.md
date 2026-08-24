## Description:

Recognizes standing, sitting, lying down, bending, raised hands, running, falling, and abnormal posture patterns for security monitoring and elder-care scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze uploaded or URL-based monitoring media for human posture recognition, fall detection, abnormal posture alerts, structured reports, and cloud history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted videos may include private people, homes, care settings, or security footage and are sent to remote services.

Mitigation: Review the publisher's remote destinations, data retention, access controls, and deletion process before using sensitive media.

Risk: The skill creates or reuses an internal identity, persists tokens locally, and can retrieve cloud report history.

Mitigation: Run it in an isolated workspace, review token storage and revocation behavior, and clear local state when the skill is no longer needed.

Risk: The package includes dev/private endpoint configuration and API documentation that does not fully match the posture-recognition use case.

Mitigation: Ask the publisher to document production endpoints and remove or explain unrelated pet-health API references before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-human-posture-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown and JSON-like structured analysis reports, with optional saved text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud history lists returned by the remote service.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
