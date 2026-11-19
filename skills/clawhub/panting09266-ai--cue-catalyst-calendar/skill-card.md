## Description:

为个人投资者整理持仓未来数月已有公告或法条依据的日期日历，并附可回查来源；只陈述事件和日期，不评估市场影响。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人投资者可提供最多 10 个 A 股主体和一个前瞻窗口，获取按日期排序的事项日历、未来 30 天关注列表及逐项来源记录。完成日历后可设置事件提醒；深度研究需用户授权。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious, citing reported weaknesses in calendar date checks and workflow concerns about external-query privacy, credential handling, and billing; scan coverage was partial.

Mitigation: Check each calendar date against its cited disclosure or statute, keep API keys in local credentials, avoid sending sensitive holdings in external queries, and authorize any paid research before it runs.

## Reference(s):

- [Event taxonomy](references/event-taxonomy.md)
- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-catalyst-calendar)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-catalyst-calendar)

## Skill Output:

**Output Type(s):** [Markdown, JSONL data]

**Output Format:** [Markdown calendar and progress log, with JSONL source records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One output directory with calendar.md, sources.jsonl, and progress.md; up to 10 subjects and a default 90-day window.]

## Skill Version(s):

0.1.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
