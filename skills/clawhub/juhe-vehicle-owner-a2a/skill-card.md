## Description: <br>
This skill lets an agent query Juhe Data for vehicle transfer-history records by VIN through a paid Alipay A2M/HTTP 402 flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check vehicle transfer-history records for a provided VIN, including transfer month, prior and current cities, and total transfer count. It is aimed at second-hand vehicle transaction, finance, and insurance review workflows that need a paid third-party data lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill initiates a paid VIN lookup through an Alipay payment flow. <br>
Mitigation: Before payment, verify the VIN, price, Alipay order details, and that the request is for a Juhe vehicle transfer-history query. <br>
Risk: The VIN is sent to a third-party vehicle-data API for lookup. <br>
Mitigation: Collect only the VIN after user confirmation and send it only to the fixed Juhe endpoint documented for this skill. <br>
Risk: Vehicle transfer-history data may be delayed or incomplete. <br>
Mitigation: Present results as reference information and advise users not to rely on the lookup as the sole basis for transaction, insurance, finance, or legal decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-owner-a2a) <br>
- [Juhe vehicle lookup endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown tables with short payment, validation, and status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid VIN and paid Alipay confirmation; final records are rendered only from Juhe API response fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
