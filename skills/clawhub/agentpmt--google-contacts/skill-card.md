## Description: <br>
Google Contacts connects an agent to AgentPMT-hosted Google Contacts actions for listing, searching, retrieving, creating, updating, and deleting contacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent manage Google Contacts through AgentPMT, including contact lookup, list export, creation, updates, and deletion when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can read and modify Google Contacts. <br>
Mitigation: Use it only for an intended AgentPMT Google Contacts connection and require explicit user direction before listing, exporting, creating, or updating contacts. <br>
Risk: The delete action permanently removes contacts. <br>
Mitigation: Confirm the target contact and the user's intent before calling delete_contact. <br>


## Reference(s): <br>
- [Google Contacts marketplace page](https://www.agentpmt.com/marketplace/google-contacts) <br>
- [ClawHub Google Contacts skill page](https://clawhub.ai/agentpmt/skills/google-contacts) <br>
- [Generated Google Contacts action schema](schema.md) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API calls] <br>
**Output Format:** [Markdown instructions with JSON examples and generated parameter schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides AgentPMT MCP or REST calls that return JSON contact data.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
