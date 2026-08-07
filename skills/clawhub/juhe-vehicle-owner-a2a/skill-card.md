## Description: <br>
This skill uses Juhe Data's vehicle transfer-history API to query paid VIN-based transfer records, including transfer dates, origin and destination cities, total transfer count, and related result details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check a vehicle's historical ownership-transfer records from a VIN before used-car, finance, or insurance decisions. The skill is designed for paid lookups that disclose the payment requirement and send only the VIN needed for the query. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Each lookup is a paid request that uses an external payment flow. <br>
Mitigation: Show the payment amount, order details, and payment options before the user approves payment. <br>
Risk: The query sends the vehicle VIN to Juhe Data for the lookup. <br>
Mitigation: Disclose VIN transmission before payment and send only the VIN required for the current query. <br>
Risk: Vehicle transfer-history data may be delayed, incomplete, or unsuitable as the sole basis for a transaction decision. <br>
Mitigation: Present results as reference information and include a reminder to verify against official vehicle registration records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vehicle-owner-a2a) <br>
- [Publisher profile](https://clawhub.ai/user/juhemcp) <br>
- [Juhe vehicle transfer query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Renders paid query results from returned vehicle-transfer fields only, with a VIN summary, transfer-record table, and data-source disclaimer.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
