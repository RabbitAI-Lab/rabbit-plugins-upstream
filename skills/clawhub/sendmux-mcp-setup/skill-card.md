## Description: <br>
Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sendmux.ai](https://clawhub.ai/user/sendmux.ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to configure OpenClaw and other agent clients for hosted OAuth, local stdio, or local HTTP bearer access to Sendmux mailbox, sending, and management MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured agents can receive operational access to Sendmux mailbox, sending, and management surfaces. <br>
Mitigation: Use scoped tokens for the selected surface and review write or send actions before execution. <br>
Risk: API keys and bearer tokens may be exposed if pasted into chat or committed in MCP configuration files. <br>
Mitigation: Store credentials in the user's secret store or environment variables and keep raw tokens out of checked-in configuration. <br>
Risk: Local HTTP MCP endpoints may be reachable by unintended clients if exposed beyond a private local environment. <br>
Mitigation: Use bearer protection for local HTTP servers and bind private setups to local or otherwise controlled network interfaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup) <br>
- [Sendmux skills homepage](https://github.com/Sendmux/skills) <br>
- [Sendmux hosted MCP endpoint](https://mcp.sendmux.ai/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash, JSON, and TOML examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes client-specific MCP setup patterns and credential handling guidance.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.3.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
