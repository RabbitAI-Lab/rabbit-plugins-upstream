## Description: <br>
Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly, including ad-hoc servers, config edits, and CLI/type generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[livvux](https://clawhub.ai/user/livvux) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage MCP server configuration, authenticate with configured servers, call MCP tools, and generate CLI or type wrappers through the mcporter command line. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authentication and configuration commands may store credentials or alter local mcporter settings. <br>
Mitigation: Review auth and config commands before running them, and use trusted credential storage and least-privilege server credentials. <br>
Risk: Tool calls may send local inputs or generated arguments to configured local or remote MCP servers. <br>
Mitigation: Use only trusted MCP servers and inspect command arguments before invoking tools, especially when handling sensitive data. <br>
Risk: Ad-hoc server creation can connect the agent to new server processes or endpoints. <br>
Mitigation: Confirm the server command or URL and its permissions before adding or running an ad-hoc server. <br>


## Reference(s): <br>
- [mcporter GitHub repository](https://github.com/pdxfinder/mcporter) <br>
- [ClawHub skill page](https://clawhub.ai/livvux/skills/mcporter-skill) <br>
- [Livvux publisher profile](https://clawhub.ai/user/livvux) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that read or update local mcporter configuration and interact with configured MCP servers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
