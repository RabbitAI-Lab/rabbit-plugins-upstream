## Description: <br>
Install and use GrayMatter as an OpenClaw skill that provides primary durable memory, shared object-graph state, and authenticated access to the live api-docs schema via api-0. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[valklaw](https://clawhub.ai/user/valklaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use GrayMatter to persist durable memory, query shared graph state, inspect live organizational schemas, and operate through RBAC-scoped GrayMatter/api-0 access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security verdict flags suspicious posture because the skill can perform remote self-update behavior and uses broad authenticated business-data authority. <br>
Mitigation: Install only after trusting ValkyrLabs and reviewing or disabling self-update behavior where possible; prefer pinned versions or checksummed releases. <br>
Risk: Authenticated GrayMatter/api-0 access may expose or mutate durable memory and business objects available to the current account. <br>
Mitigation: Use an account with RBAC permissions limited to the memory and business objects the agent actually needs. <br>


## Reference(s): <br>
- [ClawHub GrayMatter skill page](https://clawhub.ai/valklaw/skills/graymatter) <br>
- [GrayMatter product page](https://valkyrlabs.com/graymatter) <br>
- [GrayMatter GitHub repository](https://github.com/ValkyrLabs/GrayMatter) <br>
- [Architecture docs](https://github.com/ValkyrLabs/GrayMatter/blob/main/docs/architecture.md) <br>
- [Server capabilities](https://github.com/ValkyrLabs/GrayMatter/blob/main/docs/server-capabilities.md) <br>
- [GrayMatter Light docs](https://github.com/ValkyrLabs/GrayMatter/blob/main/docs/graymatter-light.md) <br>
- [MCP server docs](https://github.com/ValkyrLabs/GrayMatter/blob/main/mcp-server/README.md) <br>
- [Hosted API base](https://api-0.valkyrlabs.com/v1) <br>
- [Live API docs](https://api-0.valkyrlabs.com/v1/api-docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, endpoint names, configuration guidance, and operational instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may depend on authenticated GrayMatter/api-0 access and the current account's RBAC permissions.] <br>

## Skill Version(s): <br>
0.2.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
