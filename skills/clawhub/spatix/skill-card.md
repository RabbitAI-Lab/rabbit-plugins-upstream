## Description: <br>
Create beautiful maps in seconds. Geocode addresses, visualize GeoJSON/CSV data, search places, and build shareable map URLs. No GIS skills needed. Agents earn points for contributions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alde1022](https://clawhub.ai/user/alde1022) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agents use Spatix to create shareable maps, geocode locations, visualize GeoJSON or CSV-style spatial data, search places, and configure optional MCP access for map workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map, geocoding, routing, and dataset inputs may be sent to the Spatix service. <br>
Mitigation: Avoid submitting home addresses, private routes, sensitive facility locations, proprietary GeoJSON or CSV data, confidential prompt text, or customer location data unless service processing is intended. <br>
Risk: The optional MCP install path relies on the spatix-mcp package. <br>
Mitigation: Review the package before use and install it only in environments where that dependency is acceptable. <br>
Risk: Optional agent identifiers can appear in public leaderboard attribution. <br>
Mitigation: Use pseudonymous agent identifiers when public attribution is desired without exposing sensitive names. <br>


## Reference(s): <br>
- [Spatix Website](https://spatix.io) <br>
- [Spatix API Documentation](https://api.spatix.io/docs) <br>
- [spatix-mcp Package](https://pypi.org/project/spatix-mcp/) <br>
- [ClawHub Skill Page](https://clawhub.ai/alde1022/skills/spatix) <br>
- [Publisher Profile](https://clawhub.ai/user/alde1022) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, bash, curl, and MCP configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce shareable Spatix map URLs, embed snippets, API request examples, and optional MCP setup guidance.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
