## Description: <br>
Kiln lets agents design, slice, print, monitor, and recover physical 3D-printing jobs through an MCP server and CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codeofaxel](https://clawhub.ai/user/codeofaxel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, makers, and fabrication teams use Kiln to let an MCP-capable agent search or generate printable models, prepare files, control supported 3D printers, monitor jobs, and manage printer fleets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad control over real 3D printers and physical print jobs. <br>
Mitigation: Start with read-only or status operations, supervise first and high-risk prints, keep emergency stop procedures available, and use limited printer credentials where possible. <br>
Risk: Generated models, sliced files, or G-code may be unsuitable or unsafe for a specific printer, material, or environment. <br>
Mitigation: Review generated models and sliced G-code before printing, run pre-flight checks, and keep printer temperature and motion safety limits enabled. <br>
Risk: Install, self-update, raw G-code, fulfillment orders, and fleet-wide actions can create security, cost, or physical safety exposure. <br>
Mitigation: Require explicit approval before allowing agents to run install, self-update, raw G-code, fulfillment, or fleet actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/codeofaxel/skills/kiln) <br>
- [Publisher profile](https://clawhub.ai/user/codeofaxel) <br>
- [Kiln website](https://kiln3d.com) <br>
- [Kiln documentation](https://kiln3d.com/docs) <br>
- [PyPI package](https://pypi.org/project/kiln3d/) <br>
- [Source repository](https://github.com/codeofaxel/Kiln) <br>
- [Release v1.3.0](https://github.com/codeofaxel/Kiln/releases/tag/v1.3.0) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON MCP configuration, and operational status or setup instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide or invoke MCP and CLI workflows that affect physical 3D printers; high-risk operations should require explicit user approval.] <br>

## Skill Version(s): <br>
1.3.0 (source: server evidence release.version and server.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
