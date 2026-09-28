## Description:

Detects common rose pests and diseases from rose images or videos, returning the suspected issue, severity, general control suggestions, and report links or history when available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, growers, and agents assisting them use this skill to analyze rose leaf, shoot, bud, image, video, or URL inputs for common rose pests and diseases. It returns structured findings, severity, general care guidance, and can retrieve account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload user-provided plant media or URLs to a third-party cloud service.

Mitigation: Use only media and URLs that are acceptable to process through the service, and avoid sensitive images or private URLs.

Risk: The skill may silently create or reuse an account identity and fetch account-linked report history.

Mitigation: Run it only in the intended workspace and account context, and review whether account linkage and history access are acceptable before use.

Risk: The skill may persist authentication tokens or related identity data in the workspace data directory.

Mitigation: Protect the workspace data directory, avoid shared workspaces for sensitive use, and remove persisted data when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-rose-pest-disease-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown or JSON text, with an optional saved output file when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or public media URLs; history listing returns account-linked report records.]

## Skill Version(s):

1.0.7 (source: server release metadata; SKILL.md frontmatter states 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
