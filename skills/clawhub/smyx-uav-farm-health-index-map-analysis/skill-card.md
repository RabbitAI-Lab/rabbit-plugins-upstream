## Description:

Generates UAV farm health-index heatmaps from multispectral or high-resolution RGB imagery, computing vegetation indices such as NDVI and NDRE and highlighting crop vigor and abnormal zones.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, farm operators, drone service providers, and agricultural analysts use this skill to analyze UAV orthophotos, mosaics, or videos and receive health-index maps, field statistics, abnormal-zone coordinates and areas, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm images, videos, URLs, and account-linked identifiers may be sent to configured lifeemergence.com services.

Mitigation: Use only with data approved for those services, and confirm service configuration, access controls, and retention expectations before execution.

Risk: The skill silently manages identity and may create local users or store service tokens in a workspace SQLite database.

Mitigation: Review or disable the identity flow before use in restricted environments, and avoid shared workspaces unless local token storage is acceptable.

Risk: Cloud history queries may expose account-linked prior analysis records.

Mitigation: Run history-list functions only for authorized accounts and review output before sharing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [UAV farm health API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health-index map links, field statistics, abnormal-zone coordinates and areas, and optional saved result text when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata and target metadata; packaged SKILL.md frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
