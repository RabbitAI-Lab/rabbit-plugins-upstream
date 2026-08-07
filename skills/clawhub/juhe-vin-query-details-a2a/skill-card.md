## Description: <br>
This skill looks up detailed vehicle profile and configuration information from a user-provided VIN, using Juhe's paid VIN query service after payment and privacy confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve vehicle make, model, year, powertrain, dimensions, tire specifications, emissions standard, and other record details for a specific VIN. It is suited to vehicle profile checks where the user has explicitly agreed to the paid lookup and VIN transmission. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Each lookup is a paid service and transmits the provided VIN to Juhe's service. <br>
Mitigation: Require explicit payment and privacy confirmation before collecting the VIN or initiating the lookup. <br>
Risk: Vehicle records from a third-party data provider may be incomplete or delayed. <br>
Mitigation: Present results as reference information and direct users to verify important decisions against official vehicle records or manufacturer sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-vin-query-details-a2a) <br>
- [Juhe VIN query endpoint](https://apis.juhe.cn/a2a/query) <br>
- [Output format](artifact/OUT_FORMAT.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Guidance] <br>
**Output Format:** [Markdown vehicle information report after a paid API lookup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses only returned API fields, includes a no-records path, and appends a third-party data disclaimer.] <br>

## Skill Version(s): <br>
1.0.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
