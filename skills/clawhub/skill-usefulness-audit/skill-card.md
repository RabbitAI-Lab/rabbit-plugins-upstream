## Description:

Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to audit installed agent skills for actual usage, functional overlap, ablation evidence, runtime burden, and cleanup recommendations without automatically disabling or deleting skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage or history files and generated reports may contain sensitive conversations, local paths, project names, or customer data.

Mitigation: Pass only files needed for the audit and review Markdown or JSON reports before sharing them.

Risk: Cleanup recommendations could remove useful capabilities if treated as automatic changes.

Mitigation: Treat delete, merge-delete, and quarantine-review outputs as manual-review recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/skill-usefulness-audit)
- [Homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit)
- [Scoring Rubric](references/scoring-rubric.md)
- [Ablation Protocol](references/ablation-protocol.md)
- [Report Narration Prompt](references/report-narration-prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Natural-language report with optional Markdown and JSON files, plus optional ablation plan output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cleanup results are recommendations for manual review; the skill does not automatically delete, merge, quarantine, isolate, or disable skills.]

## Skill Version(s):

0.3.24 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
