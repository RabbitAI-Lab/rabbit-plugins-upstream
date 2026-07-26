## Description: <br>
The agentmemory HTTP REST API surface is the primary protocol for talking to the memory server when calling agentmemory over HTTP, when MCP is unavailable and a fallback is needed, or when integrating a host that does not speak MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call an agentmemory server over HTTP, especially when MCP is unavailable or when integrating a host that needs REST endpoints for saving, recalling, and searching memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unprotected local REST access could expose or modify memory data when other local users or processes are untrusted. <br>
Mitigation: Use only with memory servers you control and set AGENTMEMORY_SECRET when local access is not fully trusted. <br>
Risk: Saved memories can include secrets or sensitive workflow context if agents store them. <br>
Mitigation: Avoid saving secrets or sensitive context unless the memory server is secured appropriately. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/rohitg00/agentmemory/tree/main/plugin/skills/agentmemory-rest-api) <br>
- [ClawHub skill page](https://clawhub.ai/rohitg00/skills/agentmemory-rest-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with curl examples and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Covers localhost REST endpoints, optional Bearer token authentication, response-code conventions, and port configuration.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
