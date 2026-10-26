## Description:

用 Cue 通常 5-10 分钟（最长约 15 分钟）实时扫描今日 A 股热点板块与近 24h 催化资讯，拆解盘中催化逻辑与受益方向；跑完自动生成「看板图」与「报告长图」，报告全文以 Cue 链接交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

A-share traders and market analysts use this skill to review intraday market hotspots, catalyst news, and money flows, and to receive a concise report with visual summaries. Its output is informational and should not be treated as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to send a secret API key in chat despite saying the agent cannot view it.

Mitigation: Configure the API key locally through Cue login and do not paste it into chat; rotate any key already shared. Review the external runner before execution, and enable scheduling only after accepting recurring credit use and understanding how to disable it.

## Reference(s):

- [ClawHub release](https://clawhub.ai/panting09266-ai/skills/cue-hotspot-tracker)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-hotspot-tracker)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Images, Guidance]

**Output Format:** [Markdown report, dashboard image, report image, and Cue report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intraday A-share market snapshot; timeliness and coverage depend on Cue and external data sources. The output is not investment advice.]

## Skill Version(s):

1.0.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
