## Description:

Detects fire and smoke in images or video streams for early warning use cases such as security surveillance, forest-fire prevention, and industrial monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to submit surveillance images, videos, or media URLs for fire and smoke detection, receive structured analysis results, and query cloud-hosted historical reports tied to the active account identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media files or URL references may be sent to a remote service for fire and smoke analysis.

Mitigation: Use the skill only with media approved for cloud processing, and avoid sensitive camera footage unless the remote service and retention behavior are trusted.

Risk: The skill may automatically create or reuse an internal account identity and store account tokens in the workspace.

Mitigation: Run it in an isolated workspace, review account binding before installation, and clear local token or account data when the workspace is no longer trusted.

Risk: Cloud history retrieval can expose prior analysis reports associated with the active account identity.

Mitigation: Restrict who can run history queries and review report lists before sharing results outside the authorized audience.

## Reference(s):

- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown text and JSON analysis reports, with optional report links and saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include fire or smoke detection results, risk labels, region details, recommendations, report export links, and cloud history lists.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter states 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
