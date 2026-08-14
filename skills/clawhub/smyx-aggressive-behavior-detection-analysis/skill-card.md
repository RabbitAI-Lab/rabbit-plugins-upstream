## Description:

Detects aggressive interactions in livestock and poultry from continuous barn videos, including fighting, biting, chasing and butting, and outputs behavior type, intensity level and alert level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, farm operations teams, and livestock monitoring teams use this skill to analyze barn images or videos for aggressive animal interactions and retrieve structured reports with behavior type, intensity, alert level, affected positions, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn images, videos, or supplied media URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Install only when cloud processing is acceptable, use a dedicated workspace or account for testing, and avoid providing sensitive non-livestock footage or private URLs.

Risk: The skill creates or reuses an internal identity, can query cloud history, and stores local authentication tokens in the workspace.

Mitigation: Review the skill before installation, use a dedicated workspace or account when testing, and limit access to workspaces containing service tokens.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-aggressive-behavior-detection-analysis)
- [API Documentation](artifact/references/api_doc.md)
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file or URL input, historical report listing, detail-level selection, and optional output-file writing.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
