## Description: <br>
基于聚合数据企业信息精确查询 API，根据企业全名、注册号或统一社会信用代码查询企业详细工商信息，包括法人、注册资本、经营范围、股东、主要人员、分支机构、变更记录、经营异常等，并通过支付宝 AI 付按次付费获取结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve detailed business registration information for a named enterprise, registration number, or unified social credit code after confirming paid access. It supports business verification, due diligence, and risk review workflows where returned data should be treated as reference information rather than the sole basis for a decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Each enterprise lookup can require payment through the Alipay AI payment flow. <br>
Mitigation: Show the paid-service notice and obtain explicit user confirmation before collecting the query parameter or starting the payment flow. <br>
Risk: The company name, registration number, or unified social credit code is sent to Juhe's external API. <br>
Mitigation: Send only the requested enterprise identifier to the fixed Juhe endpoint and avoid unrelated personal-data searches. <br>
Risk: Third-party enterprise information may be delayed, incomplete, or unsuitable as the only basis for business decisions. <br>
Mitigation: Present results as reference information and advise users to verify important decisions against official registration sources. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/juhemcp/skills/juhe-enterprise-details-a2a) <br>
- [Juhe A2A enterprise query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown tables and sections generated from the paid API response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes enterprise profile, registration details, people, shareholders, branches, change records, abnormal-operation records, and a reference-data disclaimer when fields are available.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
