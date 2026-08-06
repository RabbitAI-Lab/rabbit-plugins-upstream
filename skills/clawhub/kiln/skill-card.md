## Description: <br>
Kiln lets AI agents design, slice, queue, monitor, and manage 3D printing workflows through an MCP server and CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codeofaxel](https://clawhub.ai/user/codeofaxel) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers, makers, and operations teams use Kiln to let MCP-capable agents search or generate 3D models, slice files, operate local printers, monitor jobs, and coordinate fulfillment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can control physical 3D printers and queue print jobs. <br>
Mitigation: Use printer allowlists, scoped API keys, pre-flight checks, and explicit operator confirmation before starting or queueing prints. <br>
Risk: Camera access and printer monitoring can expose sensitive workspace information. <br>
Mitigation: Disable or restrict camera access where privacy matters and limit access to trusted operators. <br>
Risk: Fulfillment workflows can place external orders or create spending exposure. <br>
Mitigation: Require explicit confirmation for fulfillment orders and enforce scoped credentials, spend limits, and approved providers. <br>
Risk: Self-update and MCP installation commands can change the local agent environment. <br>
Mitigation: Do not allow agents to run self-update or MCP installation commands without operator approval. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/codeofaxel/skills/kiln) <br>
- [Kiln GitHub repository](https://github.com/codeofaxel/Kiln) <br>
- [Kiln PyPI package](https://pypi.org/project/kiln3d/) <br>
- [Kiln website](https://kiln3d.com) <br>
- [Kiln documentation](https://kiln3d.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON snippets, shell commands, configuration examples, and agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include printer-control recommendations, MCP configuration, CLI usage, generated model workflow guidance, and JSON-formatted command output.] <br>

## Skill Version(s): <br>
1.3.2 (source: server evidence release.version and artifact server.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
