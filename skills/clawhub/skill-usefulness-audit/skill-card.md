## Description:

Review your installed agent skills to see what you actually use, what overlaps, and what may no longer be worth keeping.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to audit installed agent skills for actual usage, overlap, cleanup candidates, runtime burden, static health hints, and optional ablation evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Usage and history files may contain sensitive conversations, local paths, project names, or customer data.

Mitigation: Provide only files that are appropriate for local processing and avoid unnecessary sensitive evidence.

Risk: Cleanup recommendations could lead to accidental loss of useful installed skills if acted on automatically.

Mitigation: Review delete, merge, quarantine, isolate, or disable recommendations manually before changing installed skills.

## Reference(s):

- [Project homepage](https://github.com/gongyu0918-debug/skill-usefulness-audit)
- [Ablation Protocol](references/ablation-protocol.md)
- [Report Delivery Contract](references/report-narration-prompt.md)
- [Scoring Rubric](references/scoring-rubric.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Natural-language report, Markdown evidence, and optional JSON audit artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also produce an ablation plan and write local report files when requested.]

## Skill Version(s):

0.3.22 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
