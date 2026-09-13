## Description:

Bias Auditor scans AI-generated or draft publication text for group terms, stereotyped phrasing, and one-sided attribution, then flags potential bias and suggests de-biased rewrites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, reviewers, and content teams use this skill to run a repeatable fairness pre-check on model outputs or public-facing drafts before publication. It is intended to surface potential group generalizations, stereotype-attribution patterns, and missing-perspective signals for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable or unpinned global installation paths can install changed content before a reviewer has inspected it.

Mitigation: Review the installation path and prefer a pinned package version or reviewed Git commit with a checksum before installation.

Risk: Lexical bias-audit findings can miss context or require judgment before they are used for publication or high-impact decisions.

Mitigation: Use the skill as a screening aid and require human review for regulated, professional, or sensitive decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/bias-auditor)
- [Project Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD Theory Reference](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with optional plain text or JSON CLI audit findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local text or file input; zero third-party runtime dependencies in the inspected audit script.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence; artifact frontmatter reports 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
