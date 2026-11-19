## Description:

Maintain the GitLab agent profile page and static contribution performance chart.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to update a GitLab agent profile with monthly contribution charts and public proof records, including anonymized totals for private activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marked this release suspicious because an automatic package fallback may run while GitLab credentials are available, and scan coverage is incomplete.

Mitigation: Review the package fallback and granted tool scope before running; use a least-privilege GitLab token and resolve the unmatched local references.

## Reference(s):

- [GitLab Agent Profile on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent-profile)

## Skill Output:

**Output Type(s):** [Files, JSON, SVG, WebP]

**Output Format:** [Static SVG and WebP contribution charts plus a JSON proof file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers the last 12 completed months by default; public proof records omit identifying details for private and internal activity.]

## Skill Version(s):

1.148.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
