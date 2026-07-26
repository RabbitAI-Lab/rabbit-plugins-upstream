## Description: <br>
Guides a new user or agent through the initial setup, configuration, and capabilities of the Fulcra environment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to connect to Fulcra, authenticate the Fulcra CLI or MCP connector, and choose a task-driven or recommended onboarding path for Fulcra capabilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication or CLI actions may connect an agent to sensitive Fulcra life data. <br>
Mitigation: Require explicit user consent before checking authentication state or initiating login, and present the authentication URL and user code directly to the user. <br>
Risk: Fulcra CLI capabilities can access sensitive data, create schemas, and manage remote files when directed. <br>
Mitigation: Review prompts and proposed commands before approval, especially actions involving data access, schema creation, file upload, or remote file management. <br>
Risk: Network-restricted environments may fail during CLI authentication. <br>
Mitigation: Use the documented MCP connector path when CLI network access is unavailable. <br>


## Reference(s): <br>
- [Fulcra Onboarding on ClawHub](https://clawhub.ai/fulcra/skills/fulcra-onboarding) <br>
- [Fulcra publisher profile](https://clawhub.ai/user/fulcra) <br>
- [Fulcra CLI reference](references/fulcra-cli.md) <br>
- [Fulcra onboarding authentication reference](references/fulcra-onboarding-auth.md) <br>
- [Fulcra MCP connector documentation](https://fulcradynamics.github.io/developer-docs/mcp-server/) <br>
- [Fulcra Context iOS app](https://apps.apple.com/app/id1633037434) <br>
- [Context Web](https://context.fulcradynamics.com/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts for user consent before authentication and presents task-driven next steps.] <br>

## Skill Version(s): <br>
0.1.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
