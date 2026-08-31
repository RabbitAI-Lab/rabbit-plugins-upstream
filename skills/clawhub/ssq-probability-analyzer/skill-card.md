## Description:

双色球一站看 helps generate entertainment-only SSQ lottery analysis reports, number combinations, expert-view summaries, draw checks, and responsible-play guidance while emphasizing that no selection method improves jackpot odds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create responsible-play SSQ lottery reports, entertainment number combinations, dantuo coverage calculations, randomness checks, expert-comparison summaries, and draw-result verification. It is not suitable for betting guarantees, investment decisions, or claims of positive expected return.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches public lottery data and writes generated reports, cache, and history files locally, including Desktop report delivery.

Mitigation: Install only if local file writes and public-data fetching are acceptable; review generated files before sharing or relying on them.

Risk: The release evidence flags broad host automation, recurring execution, cross-user desktop discovery, and persistent file writes as suspicious behavior.

Mitigation: Do not enable recurring Windows, WorkBuddy, SYSTEM scheduled-task, or local-server behavior unless it is explicitly intended for the deployment.

Risk: Lottery number output can be misread as betting advice or a probability advantage.

Mitigation: Treat all recommendations as entertainment only and preserve responsible-play warnings that no method improves jackpot odds or creates positive expected return.

## Reference(s):

- [双色球诚实分析 · 方法论与数学依据](references/methodology.md)
- [双色球诚实分析 · 运维与三体协同](references/operations.md)
- [双色球算法选号防被骗 · 常见问题 FAQ](references/faq.md)
- [双色球理性购彩 · 负责任科普与防骗指南（2026 版）](references/responsible_play_2026.md)
- [脚本完整索引（scripts/lib/）](references/scripts.md)
- [完整变更历史](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated local HTML/JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May fetch public lottery data, write reports to the user's Desktop, and maintain local cache/history files.]

## Skill Version(s):

2.1.37 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
