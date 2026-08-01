## Description: <br>
牛股王独家研发的A股涨停全景分析工具，涵盖涨停分析与打板先锋两大模块，提供涨跌分布、涨停/炸板分钟级时序、封板率、晋级成功率、昨日涨停表现、连板矩阵等核心数据，帮助短线投资者全面掌握A股涨停生态。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External investors, market analysts, and agent users can use this skill to query A-share limit-up, board-break, seal-rate, promotion-rate, prior-limit-up performance, and consecutive-board matrix data for market-sentiment analysis. Outputs should be treated as informational market data, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market-data outputs may be stale, incomplete, or unsuitable as a basis for trading decisions. <br>
Mitigation: Treat responses as informational only, preserve the investment disclaimer, and verify important figures against a trusted market-data source before acting. <br>
Risk: The skill calls public Niuguwang market-data endpoints during normal use. <br>
Mitigation: Review outbound network access expectations before installation and avoid sending sensitive user data in endpoint parameters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/limit-up-panorama) <br>
- [Niuguwang app and PC metrics](https://www.stockhn.com/#/appDownload) <br>
- [Limit distribution endpoint](https://stq.niuguwang.com/taoquant/FXB/LimitDistribution?type=0&s=_test&version=6.9.5&packtype=1&night=0) <br>
- [Limit board time-series endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetLimitBoard) <br>
- [Momentum trader core data endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetDBXFShowData?s=_test&version=6.9.5&packtype=1&night=0) <br>
- [Consecutive board matrix endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetLBJZ?s=_test&version=6.7.6&packtype=1&night=0) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown] <br>
**Output Format:** [Markdown with market-data summaries, example curl commands, source attribution, and an AI investment disclaimer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are expected to include the Niuguwang source line and investment-risk disclaimer specified by the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: manifest.yaml, _meta.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
