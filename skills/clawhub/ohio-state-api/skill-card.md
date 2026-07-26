## Description: <br>
Access public Ohio State University campus data from services like bus, dining, events, buildings, parking, and more via OSU Content APIs in JSON format. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sichengchen](https://clawhub.ai/user/sichengchen) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, agents, and OSU data users use this skill to fetch, inspect, and summarize public campus data across transportation, dining, buildings, events, classes, libraries, parking, recreation, student organizations, athletics, food trucks, and BuckID merchants. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled Node-based MCP server makes outbound requests for public OSU data. <br>
Mitigation: Run it in a normal user account, prefer documented OSU service/path fetch mode, and restrict use to expected OSU API endpoints. <br>
Risk: Long-running or shared deployments may inherit dependency and runtime exposure from the Node MCP server. <br>
Mitigation: Pin or update dependencies before deployment and rebuild from the reviewed artifact. <br>
Risk: Campus data such as events, parking, bus locations, and hours can be time-sensitive. <br>
Mitigation: Include query windows and retrieval timestamps when returning time-based data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sichengchen/skills/ohio-state-api) <br>
- [OSU API reference](references/OSU_API.md) <br>
- [OSU Content API endpoints](references/endpoints.md) <br>
- [OSU MCP server README](mcp-server/README.md) <br>
- [OSU Content APIs](https://content.osu.edu) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include retrieval timestamps and raw JSON from public OSU endpoints.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
