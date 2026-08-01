## Description: <br>
ArcGIS Online helps agents search and read ArcGIS Online data through OOMOL-connected geocoding, reverse geocoding, and autocomplete actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to look up ArcGIS Online addresses and places, reverse geocode coordinates, and request autocomplete suggestions through an OOMOL-connected ArcGIS account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ArcGIS account access is handled through OOMOL-connected credentials. <br>
Mitigation: Use this skill only when the OOMOL account, oo CLI, and ArcGIS Online connection are trusted; do not handle raw ArcGIS tokens directly. <br>
Risk: Connector action schemas can change. <br>
Mitigation: Inspect the live action schema before constructing each connector payload. <br>
Risk: First-time CLI, authentication, connection, or billing setup affects the user's local environment or account state. <br>
Mitigation: Run setup steps only after the matching command failure indicates they are needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-arcgis-online) <br>
- [ArcGIS Online homepage](https://www.arcgis.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live action schema inspection before connector action execution; command responses are JSON from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
