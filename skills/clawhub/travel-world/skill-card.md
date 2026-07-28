## Description: <br>
Search flights, hotels, rental cars, travel insurance, and experiences, and plan trips through Travel World's hosted MCP server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[prosy](https://clawhub.ai/user/prosy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use Travel World to search and compare travel options, check flight status, discover promotions and destination guides, and plan trips before completing bookings on Travel World. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel searches and trip details are sent to Travel World's hosted MCP server using the user's API key. <br>
Mitigation: Confirm before sharing sensitive itinerary details and send only the information needed for the travel task. <br>
Risk: The hosted service's available providers and tools may change over time. <br>
Mitigation: Use tools/list for the current capability set and verify final travel details on Travel World before booking. <br>


## Reference(s): <br>
- [Travel World homepage](https://travel.augworlds.ai) <br>
- [Travel World MCP server](https://travel.augworlds.ai/mcp) <br>
- [Travel World API key page](https://travel.augworlds.ai/mcp-token) <br>
- [ClawHub skill page](https://clawhub.ai/prosy/skills/travel-world) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls] <br>
**Output Format:** [Markdown guidance with MCP connection details and hosted tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Travel World API key and an MCP-capable runtime; available tools should be discovered with tools/list.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
