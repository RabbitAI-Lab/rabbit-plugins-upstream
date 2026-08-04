## Description: <br>
Guides cross-border e-commerce product selection by classifying category demand drivers, checking target-market demand, estimating profit, collecting purchase-objection evidence, and deciding whether to launch, test, or pause a product. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, operators, and e-commerce product researchers use this skill to assess product-category fit, market demand, profit potential, evidence from buyer objections, and launch readiness for cross-border e-commerce. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product-selection and pricing inputs may be sent to Lingxiao's external MCP service. <br>
Mitigation: Use the anonymous tier for low-sensitivity checks and avoid submitting confidential product, supplier, margin, or account-linked data unless external service use is approved. <br>
Risk: Optional API-key and paid tools may create account-linked service usage. <br>
Mitigation: Use keys only from approved accounts and confirm that paid or higher-limit tools are authorized for the user's workflow. <br>
Risk: Profit estimates can be incomplete if refund rates, after-sales costs, or withheld fee breakdowns are not considered. <br>
Mitigation: Treat estimates as decision support and review real costs, fee details, and operational assumptions before launch decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mikeli20221102-ux/skills/lingxiao-product-selection) <br>
- [Lingxiao MCP endpoint](https://www.lingxiaochuhai.com/mcp) <br>
- [Lingxiao MCP membership key](https://www.lingxiaochuhai.com/app/membership?from=mcp-trial) <br>
- [Lingxiao service pricing](https://www.lingxiaochuhai.com/service-pricing) <br>
- [Lingxiao Product Scout](https://www.lingxiaochuhai.com/tools/product-scout) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Configuration, API Calls] <br>
**Output Format:** [Markdown with JSON snippets and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide use of an external Lingxiao MCP service for category classification, market research, and profit estimates.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
