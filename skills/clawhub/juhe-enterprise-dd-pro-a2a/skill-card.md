## Description: <br>
Generates a paid enterprise due diligence report from a company name, registration number, or unified social credit code, combining business registration details with public risk signals from Juhe Data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill for paid pre-cooperation due diligence or supplier/customer risk checks when they have a specific Chinese company name, registration number, or unified social credit code. <br>

### Deployment Geography for Use: <br>
Global, for Chinese enterprise public-record lookups <br>

## Known Risks and Mitigations: <br>
Risk: The queried company name, registration number, or unified social credit code is sent to Juhe and payment is completed through Alipay. <br>
Mitigation: Confirm user consent before payment, send only the required company keyword, and avoid unnecessary sharing of generated reports. <br>
Risk: Risk modules show partial recent public records and may omit complete history or the latest official status. <br>
Mitigation: State that the report is a quick-reference public-record compilation and direct users to official channels for complete or current verification. <br>
Risk: Brand names, short names, or incomplete company names can trigger a paid lookup for the wrong entity. <br>
Mitigation: Require the full registered company name, registration number, or unified social credit code before initiating payment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a) <br>
- [Artifact README](artifact/README.md) <br>
- [Product definition](artifact/PRODUCT.md) <br>
- [Output format](artifact/OUT_FORMAT.md) <br>
- [Business registration fields](artifact/docs/工商主体信息.md) <br>
- [Business abnormality fields](artifact/docs/企业经营异常信息.md) <br>
- [Enforcement record fields](artifact/docs/企业被执行人信息.md) <br>
- [Dishonest judgment debtor fields](artifact/docs/企业失信被执行人信息.md) <br>
- [High-consumption restriction fields](artifact/docs/企业限制高消费.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown report with structured tables, summary indicators, and concise risk notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a specific company keyword and successful payment; risk modules are partial recent records, not a complete legal or credit report.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
