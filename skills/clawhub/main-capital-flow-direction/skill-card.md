## Description: <br>
牛股王独家研发的A股主力资金流向监测工具，基于主力资金净流入/流出数据，叠加上证指数走势，实时展示大资金进出方向，帮助投资者识别资金驱动力、捕捉资金与指数的背离信号，辅助择时决策，避免被表面行情误导。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External investors, analysts, and agent users use this skill to query A-share main capital inflow and outflow, compare capital movement with the Shanghai Composite Index, identify divergence signals, and review stock or sector fund-flow rankings. Outputs should be treated as informational market analysis, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends market-data requests to Niuguwang. <br>
Mitigation: Install only when use of the disclosed Niuguwang market-data service is acceptable. <br>
Risk: Financial analysis output could be mistaken for investment advice. <br>
Mitigation: Preserve the skill's source and AI disclaimer footer and treat outputs as informational. <br>
Risk: The skill appends a fixed Chinese source/disclaimer footer to answers. <br>
Mitigation: Review generated responses to ensure the footer is appropriate for the deployment context. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/main-capital-flow-direction) <br>
- [Niuguwang capital flow API endpoint](https://stq.niuguwang.com/taoquant/CapitalFlows/Index?s=_test&version=6.9.5&packtype=1&night=0) <br>
- [StockHN app download](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown responses with optional curl examples and a fixed source/disclaimer footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a disclosed public Niuguwang market-data API; no API key is required.] <br>

## Skill Version(s): <br>
1.0.0 (source: manifest.yaml, _meta.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
