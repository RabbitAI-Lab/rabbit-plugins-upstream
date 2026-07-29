## Description: <br>
ArcGIS Online (arcgis.com) support for searching and reading ArcGIS Online data through the OOMOL ArcGIS Online connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to perform ArcGIS Online geocoding, reverse geocoding, and address or place suggestion lookups through a connected OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Addresses, place queries, and coordinates are sent through the OOMOL ArcGIS Online connector. <br>
Mitigation: Use the skill only for data that is appropriate to send to the connected ArcGIS Online workflow, and avoid submitting sensitive location data unless the account and workflow are approved for that use. <br>
Risk: The skill description covers broad ArcGIS Online requests, while the listed actions are limited to geocoding, reverse geocoding, and suggestions. <br>
Mitigation: Inspect the connector schema before each action and limit use to the available read-only actions unless updated evidence documents broader capabilities. <br>
Risk: ArcGIS Online access depends on the user's OOMOL account connection and available billing credits. <br>
Mitigation: Run setup or billing steps only after an auth, connection, scope, credential, app, or payment error indicates they are needed. <br>


## Reference(s): <br>
- [ArcGIS Online homepage](https://www.arcgis.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-arcgis-online) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON command payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
