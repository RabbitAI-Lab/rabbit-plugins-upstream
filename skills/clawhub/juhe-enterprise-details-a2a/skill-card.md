## Description: <br>
Looks up detailed enterprise registration information from Juhe Data by company name, registration number, or unified social credit code after a paid Alipay AI payment flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve paid enterprise registration details for company verification, business due diligence, risk review, and checks of shareholders, officers, changes, and operating anomalies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Each successful lookup may require payment. <br>
Mitigation: Show the price and payment details before confirmation and continue only after the user accepts the paid lookup. <br>
Risk: The company name, registration number, or unified social credit code is sent to Juhe's enterprise-information service. <br>
Mitigation: Send only the query keyword required for the lookup and avoid collecting unrelated personal or device information. <br>
Risk: Third-party enterprise data may be delayed, incomplete, or unsuitable as the sole basis for commercial or legal decisions. <br>
Mitigation: Present results as reference information and direct users to verify important facts with official registration sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-details-a2a) <br>
- [Output format evidence](artifact/OUT_FORMAT.md) <br>
- [Juhe enterprise query API endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown enterprise information report with tables and payment-flow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only returned API fields, suppresses raw JSON/HTML, and includes a third-party-data disclaimer.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
