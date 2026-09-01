## Description:

Detects delivery packages in surveillance images or videos and returns structured reports for package counts, locations, unattended alerts, and report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to analyze fixed-camera images, videos, or media URLs for package detection at community stations, residential entrances, and office lobbies. It helps count packages, identify package locations, flag long-uncollected packages, and retrieve cloud-hosted report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided surveillance images, videos, or URLs may be sent to LifeEmergence cloud services.

Mitigation: Require explicit user confirmation before uploading sensitive media or URLs, and avoid sensitive footage unless retention, deletion, and authorization terms are documented by the publisher.

Risk: The skill silently manages a cloud account identity and stores account tokens in a local workspace database.

Mitigation: Deploy only where local token storage is acceptable, restrict workspace access, and follow publisher guidance for token rotation or deletion.

Risk: Cloud report history can be queried with limited user control.

Mitigation: Require confirmation before history queries and make clear that report lists are retrieved from cloud-hosted history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Package detection API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown-style progress messages and structured JSON/text analysis with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video files or media URLs; documented media limit is 10 MB, and results can optionally be written to a file.]

## Skill Version(s):

1.0.13 (source: server release metadata; SKILL.md frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
