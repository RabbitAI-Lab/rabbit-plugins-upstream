## Description:

帮个人投资者把持仓未来数月已披露或可由适用法条明确确认的日期整理成可追溯日历。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

个人投资者可用它整理持仓未来几个月的财报、解禁、股东大会等确定日期，并查看每条日期的公告或法条出处。它不提供交易择时或事件影响判断。

### Deployment Geography for Use:

China (A-share market)

## Known Risks and Mitigations:

Risk: Calendar dates or their supporting evidence may be incomplete or unreliable.

Mitigation: Check each date against its cited official announcement or applicable statute, and run the included calendar checker before relying on the calendar.

Risk: Holdings information and API credentials may be exposed during use.

Mitigation: Share only the holdings information needed for the task, keep the Cue API key in a local credential store, and never paste it into chat.

Risk: Optional Cue research requires an account and may consume paid credits; the skill also describes account and promotional flows.

Mitigation: Use optional research only after checking the service response and obtaining explicit authorization before any credit-consuming action.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-catalyst-calendar)
- [Event taxonomy](references/event-taxonomy.md)
- [Cue service setup](https://cuecue.cn/api-key?src=clawhub-catalyst-calendar)

## Skill Output:

**Output Type(s):** [Markdown, JSONL, Text]

**Output Format:** [A date-sorted Markdown calendar with a source ledger and progress log]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Files: calendar.md, sources.jsonl, and progress.md]

## Skill Version(s):

0.1.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
