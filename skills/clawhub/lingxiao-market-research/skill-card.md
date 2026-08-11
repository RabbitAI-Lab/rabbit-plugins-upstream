## Description: <br>
Helps cross-border e-commerce sellers research category-country demand, competition, price bands, and keyword purchase intent using Lingxiao market-research tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External e-commerce sellers, marketers, and market researchers use this skill to evaluate whether a category-country market is worth pursuing and to break keywords into actionable purchase-intent groups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market-research queries are sent to Lingxiao's external MCP service. <br>
Mitigation: Avoid sending confidential product, customer, or strategy details unless the user accepts the external service exposure. <br>
Risk: Unavailable category-country combinations, partial coverage, or free-tier limits can be mistaken for evidence that a market has no demand. <br>
Mitigation: Check available options and coverage indicators before drawing conclusions, and treat missing or partial data as a data limitation. <br>
Risk: Some keyword-intent tools require an optional paid key. <br>
Mitigation: Use normal credential handling in the MCP client and do not expose paid keys in prompts, logs, or public outputs. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mikeli20221102-ux/skills/lingxiao-market-research) <br>
- [Lingxiao MCP service](https://www.lingxiaochuhai.com/mcp) <br>
- [Lingxiao market research](https://www.lingxiaochuhai.com/market-research) <br>
- [Lingxiao service pricing](https://www.lingxiaochuhai.com/service-pricing) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, markdown] <br>
**Output Format:** [Markdown with JSON configuration snippets and MCP tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call Lingxiao MCP tools and summarize market demand, competition, pricing, and keyword-intent findings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
