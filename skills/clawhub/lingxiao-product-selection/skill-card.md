## Description: <br>
Guides cross-border e-commerce product selection by classifying category demand drivers, checking market demand, estimating cross-border and overseas-warehouse profitability, and separating candidates into launch, test, or hold decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, marketplace sellers, and e-commerce teams use this skill to evaluate product-category opportunities, supplier product lists, market fit, and launch readiness with Lingxiao MCP tools and manual evidence review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends product categories, pricing, countries, and related business inputs to the external Lingxiao MCP service. <br>
Mitigation: Use the skill only when those business inputs can be shared with Lingxiao, and review the service and subscription terms before using higher-tier tools. <br>
Risk: API keys for higher usage limits could be exposed if pasted into shared prompts or files. <br>
Mitigation: Keep keys in the MCP client's normal secret or header configuration and avoid committing or sharing key-bearing configuration. <br>
Risk: Profit and market outputs can be misleading when inputs are placeholders or when refund and after-sales costs are excluded. <br>
Mitigation: Use real cost, price, weight, and country inputs, then review profitability with refund rate, support cost, and manual market evidence before launch decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mikeli20221102-ux/skills/lingxiao-product-selection) <br>
- [Lingxiao MCP service](https://www.lingxiaochuhai.com/mcp) <br>
- [Lingxiao Product Scout web tool](https://www.lingxiaochuhai.com/tools/product-scout) <br>
- [Lingxiao service pricing](https://www.lingxiaochuhai.com/service-pricing) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown] <br>
**Output Format:** [Markdown guidance with JSON MCP configuration snippets and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lingxiao MCP for category classification, market research, and profit estimation; higher usage limits and advanced tools may require an API key or paid subscription.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
