## Description:

Analyzes surveillance images and videos for delivery packages, providing detection results and reports for inventory checks and unattended monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Operators of parcel stations, residential entrances, and office lobbies can analyze surveillance media for packages and review cloud-hosted detection reports. Developers can integrate the provided command-line workflow into parcel-monitoring tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images or videos may be sent to the publisher's cloud service for analysis.

Mitigation: Use only media approved for third-party processing and confirm the service provider's data-handling terms before installation.

Risk: The skill can automatically query account-linked cloud report history with limited user control.

Mitigation: Review access to cloud reports and limit use to accounts and environments where this retrieval is acceptable.

Risk: The skill creates or reuses a local identity and stores account tokens in a workspace database.

Mitigation: Restrict access to the workspace and use an isolated environment when handling sensitive accounts or media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Package detection API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured text or JSON analysis results; Markdown tables for cloud report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, recommendations, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; bundled SKILL.md declares 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
