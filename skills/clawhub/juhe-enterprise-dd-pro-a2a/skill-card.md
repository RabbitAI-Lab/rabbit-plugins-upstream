## Description: <br>
Generates a paid standard enterprise due-diligence report that combines Chinese business registration details with public risk signals such as abnormal operations, enforcement records, dishonesty records, and consumption restrictions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill for paid pre-cooperation due diligence, supplier or customer risk checks, and checks for public enforcement, dishonesty, consumption restriction, or abnormal-operation records for a specific Chinese enterprise. The skill requires a full registered company name, registration number, or unified social credit code and returns a structured report for reference rather than legal or credit advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can return public legal and business records that may include identifiers and sensitive context. <br>
Mitigation: Avoid unnecessary logging, redistribution, or broad display of returned identifiers and legal details. <br>
Risk: A paid query sends the enterprise name, registration number, or unified social credit code to Juhe and uses Alipay for payment. <br>
Mitigation: Present the fee, payment flow, and data-transfer notice before requesting payment or sending the query. <br>
Risk: Risk modules return only the first page and the report caps displayed rows, so the report is not a complete historical record. <br>
Mitigation: State that the report shows partial recent records and advise verification against official registries for important decisions. <br>
Risk: A due-diligence summary could be mistaken for legal, credit, or cooperation advice. <br>
Mitigation: Keep conclusions factual, use the red/yellow/green signal as a reference aid only, and avoid advice such as whether to cooperate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Skill execution policy](artifact/SKILL.md) <br>
- [Report output format](artifact/OUT_FORMAT.md) <br>
- [Product scope](artifact/PRODUCT.md) <br>
- [Returned data reference](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with structured tables, risk-light summary, concise factual findings, and payment/request guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports are limited to returned public data, show only the first page of risk modules, cap displayed rows for readability, and must avoid legal or cooperation recommendations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
