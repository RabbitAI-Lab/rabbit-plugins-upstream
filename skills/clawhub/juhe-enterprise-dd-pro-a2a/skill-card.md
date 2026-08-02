## Description: <br>
This skill runs a paid enterprise due-diligence query for Chinese companies, combining business registration details with public risk signals and rendering a concise Markdown report with a summary traffic light. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill for cooperation screening, supplier or customer checks, and enterprise risk quick reviews when they have a full company name, registration number, or unified social credit code. It is not a credit report, legal opinion, or automatic cooperation recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The paid workflow sends the queried company name or registration code to Juhe and uses Alipay for payment. <br>
Mitigation: Show the payment and privacy notice, obtain explicit user confirmation, and send only the minimum required enterprise query keyword. <br>
Risk: The report can contain sensitive public-record data such as credit codes, certificate numbers, legal representative names, addresses, and court-record details. <br>
Mitigation: Avoid unnecessary logging, caching, redistribution, or reuse of report content outside the current user-requested due-diligence task. <br>
Risk: Risk modules return only the most recent page and the rendered report intentionally displays capped rows, so the report may omit older records. <br>
Mitigation: Preserve the partial-record notice, show total counts versus displayed rows, and direct users to official public record channels for complete and current verification. <br>
Risk: Users may overinterpret the summary traffic light as a legal, credit, or cooperation decision. <br>
Mitigation: Keep the output factual, state that it is not a credit report or legal opinion, and avoid recommendation language such as whether to cooperate. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-dd-pro-a2a) <br>
- [Juhe A2A Query Endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Skill Execution Rules](artifact/SKILL.md) <br>
- [Product Definition](artifact/PRODUCT.md) <br>
- [Output Format](artifact/OUT_FORMAT.md) <br>
- [Return Data Reference](artifact/README.md) <br>
- [Business Registration Fields](artifact/docs/工商主体信息.md) <br>
- [Business Abnormality Fields](artifact/docs/企业经营异常信息.md) <br>
- [Enforcement Fields](artifact/docs/企业被执行人信息.md) <br>
- [Dishonest Judgment Debtor Fields](artifact/docs/企业失信被执行人信息.md) <br>
- [Consumption Restriction Fields](artifact/docs/企业限制高消费.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown report from a paid JSON response, with payment and API workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only returned data, limits displayed risk rows, preserves partial-record notices, and avoids legal or cooperation recommendations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
