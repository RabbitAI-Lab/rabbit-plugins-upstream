## Description: <br>
Provides paid enterprise registry lookups through Juhe Data using a company name, registration number, or unified social credit code, returning structured business profile details after Alipay payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to verify company registration profiles, shareholders, personnel, branches, change records, and abnormal-operation records before business cooperation, due diligence, or risk review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may incur a paid third-party lookup or send a company query term to Juhe without understanding the transaction. <br>
Mitigation: Show the price, order details, and privacy notice, then require explicit user confirmation before sending the keyword or invoking payment. <br>
Risk: Enterprise registry data may be delayed, incomplete, or unsuitable as the sole basis for business or legal decisions. <br>
Mitigation: Present results as reference information and direct users to verify important decisions against official registration sources. <br>
Risk: Payment integrity could be affected if order details, price, resource ID, or the 402 payment response are changed. <br>
Mitigation: Pass the original 402 response to the Alipay payment skill and do not edit the submitted request JSON or payment fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-enterprise-details-a2a) <br>
- [Juhe enterprise lookup API endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown tables and sections generated from the paid lookup response] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs only returned enterprise fields and includes a disclaimer that third-party registry data is for reference.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
