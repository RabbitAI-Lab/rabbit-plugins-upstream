## Description: <br>
独行录（opcmenu.com） connects agents to a China one-person-company discovery and collaboration network for reading public marketplace information and, with a user-provided token, managing needs, contacts, messages, profiles, products, onboarding, posts, events, parks, and share cards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yzlee](https://clawhub.ai/user/yzlee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to connect an agent to opcmenu.com, browse public OPC needs and profiles, and perform authenticated collaboration workflows such as creating needs, contacting people, sending messages, updating profiles, and exporting data cards after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A user-provided opcmenu token allows the agent to act on the user's account. <br>
Mitigation: Keep the token out of chat and logs, use anonymous mode for public browsing when possible, and revoke or rotate tokens from opcmenu.com if they are exposed or no longer needed. <br>
Risk: Write actions such as creating needs, sending messages, posting updates, changing profiles, and account-changing requests can affect public or private account state. <br>
Mitigation: Show the proposed content or account change to the user and receive explicit confirmation before sending authenticated write requests. <br>
Risk: The artifact references a one-click install script for macOS and Linux. <br>
Mitigation: Review the install script before running it and install the skill only when the user intends to connect an agent to opcmenu.com. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yzlee/skills/opcmenu) <br>
- [opcmenu MCP endpoint](https://mcp.opcmenu.com/mcp) <br>
- [opcmenu REST API](https://api.opcmenu.com/v1) <br>
- [opcmenu OpenAPI description](https://api.opcmenu.com/openapi.yaml) <br>
- [opcmenu machine-readable navigation](https://opcmenu.com/llms.txt) <br>
- [opcmenu connection guide](https://opcmenu.com/connect) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Markdown, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, REST or MCP call suggestions, and structured data returned from opcmenu.com.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include authenticated account actions when the user supplies an opcmenu token.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
