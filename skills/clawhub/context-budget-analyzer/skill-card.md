## Description:

Analyzes agent conversation transcripts to estimate context-token use, identify context pollution and compaction risks, and recommend ways to preserve important information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to analyze supplied session transcripts or context inventories, understand token allocation and compaction risks, and plan practical ways to preserve important constraints and state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplied transcripts may contain secrets or information the user does not intend the agent to read.

Mitigation: Remove secrets first and provide only transcripts intended for analysis.

Risk: Constraint-preservation checks may miss lost rules, including rules assessed as low risk.

Mitigation: Manually verify every rule in policy blocks and treat the audit as a screening aid, not a safety guarantee.

## Reference(s):

- [Governance decay research (arXiv:2606.22528)](https://arxiv.org/abs/2606.22528)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with budget tables, findings, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token estimates are marked approximate; supported session-usage analysis can report measured values.]

## Skill Version(s):

1.5.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
