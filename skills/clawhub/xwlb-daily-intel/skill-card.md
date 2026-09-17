## Description:

检索并分析央视《新闻联播》指定日期或当日内容，直采央视官网文字稿并生成按时政、政策、宏观经济产业、民生和国际分类的情报报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[suaifu](https://clawhub.ai/user/suaifu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to collect official Xinwen Lianbo transcripts for a target date and turn them into a concise intelligence report with facts separated from analytical views. It is useful for tracking policy signals, macroeconomic and industry developments, public-affairs items, and international news from the broadcast.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch public CCTV pages and write Markdown reports locally.

Mitigation: Run it only where public web fetches and local report files are acceptable, and review generated files before retention or sharing.

Risk: Optional scheduling or long-term archival can create persistent daily news records.

Mitigation: Enable scheduled runs or note archival only when persistent records are intended, and use clear date-based deduplication.

Risk: Generic news requests could activate the skill unintentionally.

Mitigation: Use explicit Xinwen Lianbo or 新闻联播 wording when invoking the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/suaifu/skills/xwlb-daily-intel)
- [CCTV Xinwen Lianbo day archive URL pattern](https://tv.cctv.com/lm/xwlb/day/YYYYMMDD.shtml)
- [CCTV Xinwen Lianbo index](https://tv.cctv.com/lm/xwlb/index.shtml)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with cited source URLs and optional local transcript archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write date-keyed Markdown transcript or report files locally when the agent has filesystem access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
