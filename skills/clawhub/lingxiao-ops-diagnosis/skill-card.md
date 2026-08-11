## Description: <br>
Guides cross-border e-commerce operators through net-settlement profitability diagnosis, cancellation/return/delivery-failure bottleneck analysis, and Lingxiao MCP profit-estimation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mikeli20221102-ux](https://clawhub.ai/user/mikeli20221102-ux) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External e-commerce operators and analysts use this skill to diagnose why a store sells but does not retain profit, using net settlement, single-item profit estimates, Etsy fee estimates, and structured return/cancellation/delivery-failure analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may enter product, fee, or store metrics into an external Lingxiao MCP service. <br>
Mitigation: Review the data before submitting it, especially before using login-based whole-store analytics links. <br>
Risk: Single-item profit calculations may omit fixed-cost allocation, capital lockup, long-term exchange-rate movement, and trend context. <br>
Mitigation: Use the results as operational estimates and validate scale decisions with broader store data and at least three months of consistent metrics. <br>
Risk: Free public outputs may provide total fee amounts without detailed fee breakdowns. <br>
Mitigation: Avoid reverse-engineering withheld details from totals; use the login-based tools when itemized cost analysis is required. <br>


## Reference(s): <br>
- [Lingxiao MCP endpoint](https://www.lingxiaochuhai.com/mcp) <br>
- [Lingxiao operations analytics](https://www.lingxiaochuhai.com/tools/analytics) <br>
- [Lingxiao profit calculator](https://www.lingxiaochuhai.com/tools/profit-calc) <br>
- [Lingxiao supply-cost tools](https://www.lingxiaochuhai.com/tools/supply-cost) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with JSON configuration examples and tool-call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Lingxiao's external MCP service for optional profit and fee calculations; anonymous public usage is described as limited to 20 tool calls per IP per day.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
