## Description:

Evaluates technology and enterprise software topic portfolios, recommends a primary topic and backups, and prepares confirmed Notion change previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Editorial teams and content strategists use the skill to prioritize batches of technology, AI, data, cloud, and enterprise software topics. It evaluates evidence, timeliness, originality, fit, and privacy, then produces a primary recommendation, two backups, other topic decisions, and a confirmed Notion writeback preview.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Derived search terms may expose private editorial topics or unpublished wording to external search services before privacy screening.

Mitigation: Remove or generalize confidential topics and unpublished wording before research; use only terms approved for external search.

Risk: The security scan was partial, including incomplete inspection of one script, and does not verify runtime permissions.

Mitigation: Review the scan limitations and runtime permissions before installing or using the skill with private material.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/haiyangchenbj/skills/editorial-topic-portfolio-skill)
- [Evaluation gates](artifact/references/evaluation-gates.md)
- [Scoring model](artifact/references/scoring-model.md)
- [Portfolio rules](artifact/references/portfolio-rules.md)
- [Notion adapter interface](artifact/references/notion-adapter-interface.md)
- [Replay evaluation](artifact/references/replay-evaluation.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown reports and JSON topic records, scores, and change previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One primary recommendation and two backups, with other topic dispositions; Notion writeback requires confirmation and readback verification.]

## Skill Version(s):

1.0.9 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
