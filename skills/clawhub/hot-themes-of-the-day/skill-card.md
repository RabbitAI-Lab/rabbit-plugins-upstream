## Description: <br>
牛股王独家研发的A股今日题材库，基于牛股王正宗题材库每日更新当天市场炒作的热点题材，快速回答"今天炒什么"这个核心问题。为每个热点题材提供简明摘要与核心逻辑，展示题材下相关股票、最新价、涨幅及关联原因，帮助投资者一站式掌握当日题材热点与活跃标的。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, investors, and market analysts use this skill to ask about the day's Chinese A-share market themes, related stocks, price movement, and linkage reasons. The output is informational market data and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global; content focuses on Chinese A-share markets. <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat stock themes, related stocks, and price movement as investment advice. <br>
Mitigation: Present the information as market data only and keep the required AI disclaimer that it does not constitute investment advice. <br>
Risk: Queries and responses depend on Niuguwang's public data service. <br>
Mitigation: Use the skill only when sending market-theme requests to that public service is acceptable, and avoid including sensitive or private information. <br>
Risk: Responses include branded source text from the data provider. <br>
Mitigation: Preserve the required source attribution so readers can identify the data origin. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/hot-themes-of-the-day) <br>
- [Niuguwang HotSpot GetNews public endpoint](http://apicore.niuguwang.com/askstock/HotSpot/GetNews) <br>
- [StockHN app and PC page](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown responses with market-theme summaries, related stock tables or lists, source attribution, and an AI disclaimer; optional bash curl examples for the public endpoint.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should preserve the skill's required Chinese data-source note and AI disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, manifest.yaml, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
