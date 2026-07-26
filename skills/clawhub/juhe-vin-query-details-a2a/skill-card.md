## Description: <br>
Looks up detailed vehicle profile information from a VIN through Juhe Data's paid VIN query service and returns a structured Markdown report after the disclosed Alipay payment flow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to query a paid VIN vehicle-data service for vehicle make, model, year, powertrain, dimensions, tire specifications, emissions standard, announcement number, and related profile fields. It is suited to vehicle-record review and pre-transaction checks where third-party data is acceptable as reference information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A VIN is sent to Juhe's vehicle-data service as part of a paid query. <br>
Mitigation: Show the paid-query and privacy notice before collection, send only the VIN over HTTPS, and avoid collecting phone numbers, identity documents, addresses, bank data, device identifiers, or location. <br>
Risk: Users may treat third-party vehicle profile data as authoritative for registration, legal, insurance, or purchase decisions. <br>
Mitigation: Present results as reference information and direct users to verify important decisions against actual vehicle registration records or manufacturer sources. <br>
Risk: The skill depends on a paid Alipay payment flow before returning query results. <br>
Mitigation: Require explicit user confirmation, preserve the payment response without changing order or resource details, and stop without querying if the user cancels payment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vin-query-details-a2a) <br>
- [Publisher profile](https://clawhub.ai/user/juhemcp) <br>
- [Juhe VIN query API endpoint](https://zxw-apis.juhe.cn/a2a/query) <br>
- [Skill behavior specification](artifact/SKILL.md) <br>
- [Output format specification](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown vehicle report with tabular fields, plus payment-flow guidance and an HTTPS JSON request example] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a single VIN for each paid lookup; outputs only fields returned by the vehicle-data service and avoids raw JSON or HTML in the user-facing result.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
