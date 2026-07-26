## Description: <br>
MCP CLI Manager - Manage MCP servers and call tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maplezzk](https://clawhub.ai/user/maplezzk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to configure MCP servers, run the mcps daemon, inspect available tools, and call tools from configured servers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured MCP servers and commands can run locally and may receive sensitive environment variables. <br>
Mitigation: Install only trusted npm packages and MCP servers, review ~/.mcps/mcp.json before use, and pass secrets through environment variables only when the target server is trusted. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/maplezzk/skills/mcps-skill) <br>
- [npm package @maplezzk/mcps](https://www.npmjs.com/package/@maplezzk/mcps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill guides local MCP server configuration and tool invocation through the mcps CLI.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
