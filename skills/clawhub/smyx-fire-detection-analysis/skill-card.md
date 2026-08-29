## Description:

Detects flames and smoke in image, video, local file, or URL inputs and returns structured fire-risk analysis for early warning workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, facility operators, and developers use this skill to submit surveillance images, videos, local files, or public media URLs for cloud fire and smoke analysis. The skill returns structured detection results, risk guidance, report links, and account-linked historical report listings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted images, videos, URLs, identity data, and account-linked report history may be processed by configured cloud services.

Mitigation: Install only when cloud processing is acceptable, use approved media, and inspect endpoint configuration before use.

Risk: The skill may create or reuse local identities, perform remote login or registration, and store tokens in a workspace data database.

Mitigation: Run the skill in an isolated workspace, avoid shared workspaces for sensitive media, and review local identity or token storage after use.

Risk: Configuration evidence includes dev or private HTTP endpoint options.

Mitigation: Replace endpoints with approved production services before operation and block unapproved network destinations.

Risk: Fire and smoke detection output is advisory and may be incomplete or incorrect.

Mitigation: Use results as early warning support only; confirm suspected fire events through trained personnel and emergency procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis and report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media paths or public media URLs; supports optional file output and historical report listing.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
