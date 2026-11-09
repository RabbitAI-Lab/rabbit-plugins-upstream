## Description:

Test whether your skills actually fire. Feed it synthetic user messages, it checks which skill SHOULD trigger vs which stays silent, and scores trigger accuracy per skill — catches the silent-failure case the official eval tool misses. 测试你的技能是否真的会触发：喂入模拟用户消息，逐个验证该触发的触发、不该触发的安静，输出每个技能的触发准确率报告——专治官方评测工具测不出的静默失灵。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomaszhou22](https://clawhub.ai/user/thomaszhou22)

### License/Terms of Use:

MIT-0

## Use Case:

Skill developers and teams use Trigger Test to check whether messages should activate or stay silent for installed skills. It produces per-skill and installation trigger scores to guide skill description revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports quote test messages verbatim, which can expose sensitive text.

Mitigation: Use synthetic or redacted messages.

Risk: Suggested description edits can affect future skill selection, and scores are diagnostic estimates.

Mitigation: Review proposed edits before applying them and treat scores as diagnostic estimates.

## Reference(s):

- [ClawHub release](https://clawhub.ai/thomaszhou22/skills/skill-trigger-test)
- [Analysis Protocol](artifact/references/analysis-protocol.md)
- [Report Template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown report with trigger verdicts, per-skill scores, and scorecard tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scores are diagnostic estimates; test messages may be quoted verbatim.]

## Skill Version(s):

1.0.0 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
