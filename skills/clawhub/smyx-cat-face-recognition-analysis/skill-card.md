## Description:

Identifies individual cats in images or videos by comparing their faces against a registered cat database and returns recognition reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to distinguish cats in photos or videos and retrieve past recognition reports after registering their cats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, URLs, and report-history requests are sent to a cloud service.

Mitigation: Submit only authorized media and review the cloud service's handling of submitted data before use.

Risk: Automatic identity management and local token storage could mix or expose report history in shared workspaces.

Mitigation: Avoid shared or multi-user workspaces until identity isolation, token storage, and report-history access have been reviewed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-cat-face-recognition-analysis)
- [Cat recognition API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured recognition results or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links; recognition requires previously registered cats and clear images.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
