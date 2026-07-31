## Description: <br>
牛股王独家研发的A股机构动向追踪工具，涵盖机构关注与机构调研两大维度，展示分析师评级、研报观点、买入/增持次数、关注机构数量、实地调研次数、调研机构数量及调研详情，帮助投资者了解机构资金动向与关注方向。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve and summarize Chinese A-share institutional attention and field-research activity from public Niuguwang endpoints. It supports questions about recently rated sectors and stocks, analyst views, buy or overweight counts, research counts, participating institutions, and related detail records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market data outputs could be mistaken for investment advice. <br>
Mitigation: Treat outputs as informational only and retain the Niuguwang data-source note and AI investment-risk disclaimer. <br>
Risk: The skill is tailored to Chinese A-share market data and may not be suitable for other markets. <br>
Mitigation: Use it only for the stated A-share institutional activity use case and verify applicability before relying on results. <br>
Risk: Public endpoint responses may be empty or unavailable for specific records. <br>
Mitigation: Handle null or empty responses explicitly and avoid presenting missing data as confirmed market activity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/institutional-activity-tracker) <br>
- [Niuguwang app and PC data source](https://www.stockhn.com/#/appDownload) <br>
- [GetFocusPlate API](https://stq.niuguwang.com/taoquant/ResearchReport/GetFocusPlate?packType=2000&version=5.0.16.0&type=3&plateType=4) <br>
- [GetFocusStock API](https://stq.niuguwang.com/taoquant/ResearchReport/GetFocusStock?packType=2000&version=5.0.16.0&code=2000619&type=3) <br>
- [GetStockConcernHisByPeriod API](https://stq.niuguwang.com/taoquant/ResearchReport/GetStockConcernHisByPeriod?packType=2000&version=5.0.16.0&innercode=1796&type=3) <br>
- [GetResearchPlate API](https://stq.niuguwang.com/taoquant/ResearchReport/GetResearchPlate?packType=2000&version=5.0.16.0&type=3&plateType=0) <br>
- [GetResearchStock API](https://stq.niuguwang.com/taoquant/ResearchReport/GetResearchStock?packType=2000&version=5.0.16.0&code=2000989&type=3) <br>
- [GetInvestorRa API](https://stq.niuguwang.com/taoquant/ResearchReport/GetInvestorRa?packType=2000&version=5.0.16.0&innercode=660&period=3) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown with API endpoint examples and required data-source and AI disclaimer footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public Niuguwang GET endpoints; no API key required.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
