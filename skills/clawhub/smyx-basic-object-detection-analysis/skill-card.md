## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels appearing in the target area, with support for video stream and image detection in general security surveillance scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security teams use this skill to analyze images, local videos, or media URLs for common object categories and retrieve structured detection reports or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media or media URLs may be sent to external cloud services for object detection.

Mitigation: Use only approved, non-sensitive media unless cloud processing by the configured service is acceptable for the deployment.

Risk: The skill can create or reuse a local identity and persist access tokens in the workspace data directory.

Mitigation: Review local workspace data handling, restrict workspace access, and clear persisted identity or token state when the skill is removed or rotated.

Risk: Historical report queries can retrieve cloud-stored activity associated with the resolved identity.

Mitigation: Limit installation and use to environments where cloud history lookup is expected and authorized.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or structured JSON text, with optional saved output files and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; output may include cloud-generated report links.]

## Skill Version(s):

1.0.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
