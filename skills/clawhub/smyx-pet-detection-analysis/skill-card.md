## Description:

Detects cats, dogs, and birds appearing in the target area; supports video stream and image detection for home pet monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze household pet images, video files, or media URLs for cats, dogs, and birds. It returns structured detection results, report links, and cloud history lookups associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household pet images, videos, submitted URLs, and account-linked identifiers may be sent to the publisher's cloud service.

Mitigation: Use only with explicit consent for cloud processing and confirm the publisher's retention, deletion, and access-control practices before installation.

Risk: The skill can silently create or reuse a remote account and persist identity or token data in the local workspace.

Mitigation: Review identity initialization, local SQLite token storage, workspace identity-file use, and cleanup steps before running in shared or sensitive environments.

Risk: Cloud history lookup may expose prior analysis reports associated with the resolved identity.

Mitigation: Limit use to trusted workspaces and clear local identity and token state when transferring, sharing, or decommissioning the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet health analysis API documentation](artifact/references/api_doc.md)
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text containing structured pet-detection results, history lists, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write output to a user-specified file when the output path option is used.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
