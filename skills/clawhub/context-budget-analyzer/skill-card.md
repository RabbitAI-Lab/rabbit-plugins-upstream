## Description:

Analyzes agent transcripts to estimate context use, identify compaction risks, and recommend practical ways to preserve important information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use it to understand where conversation context is spent and reduce the risk of losing important constraints during compaction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Transcripts may contain secrets, and raw audit output can quote them.

Mitigation: Provide only transcripts intended for analysis and remove secrets beforehand.

Risk: Compaction and constraint-loss conclusions are heuristic and may be inaccurate.

Mitigation: Review those conclusions against the source context before acting on recommendations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/z-zihan/skills/context-budget-analyzer)
- [Skill-declared homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with budget tables, risk findings, and actionable recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token estimates are labeled approximate; measured usage is reported when available.]

## Skill Version(s):

1.6.0 (source: artifact/SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
