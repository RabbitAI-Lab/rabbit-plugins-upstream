## Description: <br>
牛股王独家研发的A股龙虎榜分析工具，解析机构、一线游资、外资的买卖动向，揭秘主力席位操作思路，展示每日上榜股票背后的资金性质与席位属性，帮助投资者看清异动背后是谁在操作，为次日操作提供资金层面的决策参考。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and finance-focused agents use this skill to retrieve and summarize Chinese A-share Dragon & Tiger list data after market close, including institutional, active trader, and foreign-capital activity for daily review and next-day planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market-data summaries could be mistaken for investment advice. <br>
Mitigation: Preserve the required AI disclaimer and treat outputs as informational market analysis. <br>
Risk: The skill contacts Niuguwang's public data service. <br>
Mitigation: Install only where outbound requests to that public service are acceptable; no credentials are requested. <br>
Risk: Dragon & Tiger list data may be unavailable before post-market publication or on non-trading days. <br>
Mitigation: Follow the documented time-based data strategy and avoid fabricating missing market data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/dragon-and-tiger-list) <br>
- [Niuguwang Dragon & Tiger List API](https://stq.niuguwang.com/taoquant/NewLhb/GetAllStocks?s=_test&version=6.5.1&packtype=1&night=0) <br>
- [Niuguwang App/PC download](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Chinese Markdown text with market-data summaries and a required source and AI disclaimer footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public Dragon & Tiger list data and must avoid fabricated market data.] <br>

## Skill Version(s): <br>
1.0.0 (source: manifest.yaml, _meta.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
