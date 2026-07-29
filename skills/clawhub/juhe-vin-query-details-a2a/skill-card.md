## Description: <br>
Provides paid VIN-based vehicle profile lookups through Juhe Data, returning make, model, year, drivetrain, emissions, body dimensions, tire specifications, and related vehicle archive details after user-confirmed payment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and consumer agents use this skill to query detailed vehicle archive and configuration information for a specific 17-character VIN, including support for second-hand vehicle checks, insurance review, finance review, and model verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends a VIN to Juhe Data for a paid lookup. <br>
Mitigation: Proceed only when the user has provided a valid VIN, reviewed the displayed price and order details, and intentionally confirmed the payment flow. <br>
Risk: Generic affirmative replies can be interpreted as consent to continue a paid lookup. <br>
Mitigation: Show the VIN, price, payment method, and privacy notice before payment, and treat cancellation or missing VIN input as a stop condition. <br>
Risk: Third-party vehicle archive data may be delayed, incomplete, or absent. <br>
Mitigation: Present results as reference information, do not fabricate missing fields, and direct users to verify against official vehicle registration or manufacturer records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vin-query-details-a2a) <br>
- [Juhe A2A VIN query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [VIN query output format](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Guidance] <br>
**Output Format:** [Markdown tables and status messages based on the paid lookup result] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a valid VIN and user-confirmed Alipay payment before returning vehicle details; missing or unrecognized records are reported without fabricating vehicle data.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
