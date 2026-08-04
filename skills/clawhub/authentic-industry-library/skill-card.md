## Description: <br>
牛股王独家研发的A股正宗产业库，收录历史上所有题材的完整数据，展示每个题材的涨幅、涨停个数、上涨/下跌个数等整体表现，并将每个题材拆解为上游、中游、下游产业链，展示各环节的相关股票及具体分工，帮助投资者全景把握题材强弱与产业链传导逻辑。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External investors and market researchers use this skill to query A-share industry-theme performance, compare topic strength, and inspect upstream, midstream, and downstream stock roles from Niuguwang public data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill returns stock-industry data that a reader could mistake for investment advice. <br>
Mitigation: Keep the required AI disclaimer in relevant answers and do not present outputs as authority to trade or modify accounts. <br>
Risk: The skill makes public Niuguwang API requests for market and industry-chain data. <br>
Mitigation: Install only where outbound public API requests to Niuguwang are acceptable and review returned data before using it in decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/authentic-industry-library) <br>
- [Niuguwang industry chain plate list API](http://apicore.niuguwang.com/askstock/IndustryChain/GetIndustryChainPlates) <br>
- [Niuguwang industry chain stock list API](http://apicore.niuguwang.com/askstock/IndustryChain/GetIndustryChainStks?plateInnerCode=2000047) <br>
- [Niuguwang app download and metrics](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Shell commands, Markdown] <br>
**Output Format:** [Markdown with optional shell command examples and source/disclaimer footer] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should append the required Niuguwang data-source footer and AI investment disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
