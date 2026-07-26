## Description: <br>
Search OneHome (CoreLogic) portal listings, get property details, photos, schools, saved searches. Use when the user asks about real estate listings shared by their agent, OneHome links, portal.onehome.com properties, or specific addresses / MLS numbers they want to look up. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and real-estate buyers use this skill to have an agent search OneHome portal listings, inspect listing details, retrieve photos and school information, compare shared listings, and run local affordability calculations from their own OneHome access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OneHome tokens, magic links, or signed-in browser captures can expose the user's private portal listing data. <br>
Mitigation: Use the skill only in the intended environment, avoid sharing tokens or magic links, and refresh or remove access when it is no longer needed. <br>
Risk: The raw GraphQL escape hatch can retrieve more account data than a normal listing lookup needs. <br>
Mitigation: Use structured OneHome tools first and limit raw GraphQL requests to fields that are necessary for the user's current task. <br>
Risk: Expired tokens or inactive browser capture sessions can cause failed or hanging portal-backed calls. <br>
Mitigation: Run the health check before portal lookups and refresh the token or trigger a portal interaction when capture mode has not observed a GraphQL request. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/onehome-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Text, Markdown] <br>
**Output Format:** [Markdown or structured tool-call guidance summarizing OneHome listing data and local calculator results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided OneHome access through a token, magic link, or signed-in browser capture for portal-backed data.] <br>

## Skill Version(s): <br>
0.12.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
