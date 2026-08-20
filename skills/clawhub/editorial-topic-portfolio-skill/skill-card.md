## Description:

Evaluates technology, AI, data, cloud, and enterprise-software topic portfolios by normalizing inputs, applying factual and editorial gates, scoring eligible topics, selecting one primary topic plus two backups, and preparing guarded Notion writeback previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, editors, and content strategists use this skill to review a batch of candidate topics, separate lifecycle status from recommendation priority, choose the current writing cycle's primary and backup topics, and produce reviewed change previews for a Notion topic database or local files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Standing Notion synchronization could update unintended pages or fields if credentials and authorization scope are too broad.

Mitigation: Limit the Notion token to the intended topic database, name the target database and allowed fields in any standing instruction, and use the default two-confirmation flow unless there is a clear operational reason for standing authorization.

Risk: Incorrect facts, stale status, or unclear editorial boundaries could promote an unsuitable topic into the primary or backup set.

Mitigation: Apply hard gates before scoring, require source/date/status verification, block factual or privacy-boundary failures from primary and backup choices, and record residual risk in the round report.

## Reference(s):

- [Evaluation Gates](references/evaluation-gates.md)
- [Scoring Model](references/scoring-model.md)
- [Portfolio Rules](references/portfolio-rules.md)
- [Notion Adapter Interface](references/notion-adapter-interface.md)
- [Replay Evaluation](references/replay-evaluation.md)
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/editorial-topic-portfolio-skill)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON records and change sets, inline shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default outputs include normalized topic records, gate results, scores, portfolio decisions, change previews, validation results, writeback results, and readback verification.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
