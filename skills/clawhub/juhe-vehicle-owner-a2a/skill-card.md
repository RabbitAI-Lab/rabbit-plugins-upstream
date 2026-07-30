## Description: <br>
This skill lets an agent run paid vehicle transfer-history lookups by VIN through Juhe Data and return transfer dates, cities, and total transfer counts for vehicle-risk review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to query a vehicle's ownership-transfer history from a valid VIN after payment. It supports used-car transactions, finance, and insurance workflows where transfer count and transfer cities help assess vehicle risk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The lookup is paid and sends the submitted VIN to Juhe's API. <br>
Mitigation: Disclose the fee, payment flow, data recipient, and VIN-only data use before payment, and proceed only after explicit user consent. <br>
Risk: Invalid or missing VIN input could trigger an inappropriate paid lookup attempt. <br>
Mitigation: Require a valid 17-character VIN, normalize input, and block requests that lack a concrete vehicle-transfer lookup intent. <br>
Risk: Vehicle transfer data may be delayed, incomplete, or insufficient for a final transaction decision. <br>
Mitigation: Present results as reference information and tell users to confirm against actual vehicle registration records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-owner-a2a) <br>
- [Publisher profile](https://clawhub.ai/user/juhemcp) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, API Calls] <br>
**Output Format:** [Markdown report rendered from API JSON after the paid lookup flow] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid 17-character VIN and successful payment; output should only use fields returned by the API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
