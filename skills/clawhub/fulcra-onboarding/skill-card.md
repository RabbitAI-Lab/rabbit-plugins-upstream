## Description: <br>
Guides a new user or agent through the initial setup, configuration, and capabilities of the Fulcra environment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their agents use this skill to connect to Fulcra, authenticate with the Fulcra CLI or MCP connector, choose a useful onboarding direction, and create an initial view, coordination structure, or project dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects an agent to a Fulcra account that may contain sensitive personal data such as health, location, calendar, activity, and agent artifacts. <br>
Mitigation: Use it only when the user wants Fulcra account access, request explicit consent before authentication or sensitive data access, and keep actions scoped to the user's stated goal. <br>
Risk: Authentication uses a browser login flow and can store Fulcra credentials on the local filesystem. <br>
Mitigation: Use the documented device-code flow, keep the device code private, and make local credential storage clear before completing setup. <br>
Risk: The skill may create persistent records or upload local files to Fulcra. <br>
Mitigation: Confirm with the user before uploading files or creating persistent records, and explain what will be stored in Fulcra. <br>


## Reference(s): <br>
- [Fulcra CLI](references/fulcra-cli.md) <br>
- [Fulcra Getting Started: Authentication](references/fulcra-onboarding-auth.md) <br>
- [Fulcra MCP documentation](https://fulcradynamics.github.io/developer-docs/mcp-server/) <br>
- [Context Web](https://context.fulcradynamics.com/) <br>
- [Fulcra Cookbook](https://www.fulcradynamics.com/resources/cookbook) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Conversational Markdown with links, inline shell commands, and setup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide browser-based authentication, Fulcra CLI setup, data views, project files, and persistent Fulcra records with user consent.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
