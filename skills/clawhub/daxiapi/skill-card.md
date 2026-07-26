## Description: <br>
大虾皮(daxiapi.com)金融数据API服务入口，负责路由分发到具体分析skill，用于识别A股市场、板块、个股、财报、消息面和资金流向等数据需求并给出相应的专业skill或CLI命令。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ksky521](https://clawhub.ai/user/ksky521) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill as a routing entry point for A-share financial data requests, including market review, stock analysis, sector analysis, financial-report analysis, news and announcement interpretation, and capital-flow queries. It maps user intent to specialized ClawHub skills when available and otherwise provides daxiapi CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask users to configure or pass a daxiapi API token. <br>
Mitigation: Treat the token as a secret and prefer temporary environment variables or a secure credential store. <br>
Risk: The skill may suggest npx daxiapi-cli@latest commands, which execute a package fetched from the npm ecosystem. <br>
Mitigation: Review each command before running it and install only when intending to use daxiapi and related market-data services. <br>
Risk: Financial market data and analysis outputs may be stale, incomplete, or unsuitable as standalone investment advice. <br>
Mitigation: Use outputs for research support and verify data, assumptions, and decisions against authoritative market and professional sources. <br>


## Reference(s): <br>
- [大虾皮 API 详细参考文档](artifact/references/api-reference.md) <br>
- [数据字段说明](artifact/references/field-descriptions.md) <br>
- [大虾皮 API Service](https://daxiapi.com) <br>
- [大虾皮 API Base URL](https://daxiapi.com/coze) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls] <br>
**Output Format:** [Markdown with inline bash commands and routing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route the agent to related skills or propose daxiapi CLI/API calls; the skill itself does not produce persistent files.] <br>

## Skill Version(s): <br>
3.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
