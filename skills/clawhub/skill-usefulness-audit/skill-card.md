## Description:

Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent maintainers use this skill to audit installed agent skills for usage, overlap, cleanup candidates, static health, and optional ablation evidence before deciding what to keep, narrow, merge, or remove.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local skill folders and optional usage or history files that may contain sensitive conversations, paths, project names, or customer data.

Mitigation: Use explicit input paths, limit evidence files to the audit scope, and review generated reports before sharing them.

Risk: Cleanup, deletion, merge, or quarantine recommendations could be mistaken for automatic actions.

Mitigation: Treat those outputs as manual-review recommendations only; confirm evidence before changing or removing any skill.

## Reference(s):

- [Ablation Protocol](references/ablation-protocol.md)
- [Report Narration Prompt](references/report-narration-prompt.md)
- [Scoring Rubric](references/scoring-rubric.md)
- [Project homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Short natural-language report, optional Markdown evidence report, and optional JSON audit or ablation-plan files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations are manual-review guidance; reports are written only when output paths are provided.]

## Skill Version(s):

0.3.21 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
