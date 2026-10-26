## Description:

用 Cue 帮你看清被套的股票上方还有哪几道坎——从筹码分布定位套牢盘、用均线校验阻力强度、推演反弹每一步需要的量能，产出可复核的解套压力线底稿，辅助判断反弹到哪容易卡住、哪里该减仓。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向希望分析个股反弹压力的投资者，整理上方套牢筹码、均线阻力和反弹量能，形成可复核的压力位分析底稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill updates runner code that uses the user's Cue API key, and its instructions about key access are contradictory.

Mitigation: Review and pin the runner version before use; keep the API key in local configuration and do not paste it into chat.

Risk: Stock queries and optional holding costs are sent to Cue, and scheduled runs consume credits.

Mitigation: Avoid sharing unnecessary sensitive details and enable scheduled runs only for stocks and times explicitly chosen by the user.

## Reference(s):

- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-unwind-pressure-line)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Structured Markdown stock-analysis report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an analysis summary, resistance levels, rebound scenarios, and risk notes.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
