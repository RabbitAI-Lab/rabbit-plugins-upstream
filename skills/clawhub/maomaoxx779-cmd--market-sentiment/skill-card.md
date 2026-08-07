## Description: <br>
牛股王独家研发的A股市场情绪指标，基于板块热度、赚钱效应等多维度数据综合评分，提示市场情绪持续向好/向坏、关注度提升/下降的板块，辅助把握结构性机会。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer A-share market sentiment and sector ranking questions by retrieving public 牛股王 market data and summarizing the current market mood. It is intended as an auxiliary market context tool, not as personalized investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market sentiment or sector-ranking requests are sent to 牛股王 endpoints. <br>
Mitigation: Use this skill only for A-share market sentiment or sector ranking questions where public market-data lookup is expected. <br>
Risk: Market summaries may be mistaken for personalized investment advice. <br>
Mitigation: Keep the required AI disclaimer and treat the output as auxiliary market context rather than a trading recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/market-sentiment) <br>
- [Publisher profile](https://clawhub.ai/user/maomaoxx779-cmd) <br>
- [牛股王 market emotion endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetMarketEmotion?plateType=-1) <br>
- [牛股王 plate emotion ranking endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetPlateEmoRank) <br>
- [牛股王 app and PC download page](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Markdown, Guidance] <br>
**Output Format:** [Markdown text with market sentiment, sector ranking details, a data-source line, and an AI disclaimer.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should preserve the required 牛股王 data-source footer and AI disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
