## Description: <br>
Memkeeper for OpenClaw installs, configures, verifies, and removes local-first Memkeeper memory with local embedding and reranking defaults, a scoped MCP tool profile, and connection diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[teflon07](https://clawhub.ai/user/teflon07) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw users and developers use this skill to set up local semantic memory as a stdio MCP server, verify the connection, and keep memory storage and model inference local by default. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup runs a GitHub-hosted installer and downloads local models. <br>
Mitigation: Download the installer to a temporary file, inspect it before execution, and run the setup only from the expected public source. <br>
Risk: The MCP server creates a persistent local memory database and includes tools that can write memory. <br>
Mitigation: Use the local store path deliberately, start with the scoped tool profile, and keep direct deletion or graph mutation tools disabled unless the operator explicitly needs them. <br>
Risk: Changing from local embedding or reranking can send memory text to an external provider. <br>
Mitigation: Keep the local defaults unless the operator explicitly requests a non-local provider, and use a separate store or deliberate re-embedding before switching backends. <br>


## Reference(s): <br>
- [Memkeeper for OpenClaw release](https://clawhub.ai/teflon07/skills/memkeeper-mcp-setup) <br>
- [Memkeeper installer script](https://raw.githubusercontent.com/teflon07/memkeeper/main/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports the configured store path, enabled tool count, and probe result without printing stored memory contents, API keys, tokens, or sensitive environment values.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
