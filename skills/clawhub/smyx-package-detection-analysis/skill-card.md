## Description:

Detects delivery packages in surveillance images or video and returns analysis reports and account-linked report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check surveillance images or video for packages at delivery stations, entrances, and reception areas, and to retrieve previous detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images and video are sent to external services for analysis.

Mitigation: Confirm service ownership, media retention, and access controls before submitting footage; avoid sensitive footage without approval.

Risk: The skill creates or reuses a local identity, stores account tokens, and queries account-linked report history.

Mitigation: Review who controls the account and history, restrict access to the workspace data directory, and establish token cleanup procedures.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Package detection API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Markdown]

**Output Format:** [Text with structured analysis results and Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be saved to a local file.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata; artifact frontmatter states 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
