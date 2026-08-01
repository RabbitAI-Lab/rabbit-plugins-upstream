## Description: <br>
Kiln lets AI agents design, slice, print, monitor, and recover physical objects through an MCP server for 3D printers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codeofaxel](https://clawhub.ai/user/codeofaxel) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers, makers, and operators use Kiln to connect AI agents to real 3D printers for model generation, marketplace search, slicing, print queueing, monitoring, and multi-printer management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AI-connected agents can control real 3D printers and affect physical equipment. <br>
Mitigation: Keep printer access scoped, supervise print jobs, verify emergency stop access, and confirm temperature limits before use. <br>
Risk: Unattended first runs can allow unsafe or failed prints to continue without operator intervention. <br>
Mitigation: Avoid unattended first runs and monitor early jobs with camera snapshots or direct observation. <br>
Risk: Printer API credentials and live printer configuration can expose operational control. <br>
Mitigation: Use least-privilege printer credentials, keep API keys secret, and review updates before reconnecting live printers. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/codeofaxel/skills/kiln) <br>
- [Kiln website](https://kiln3d.com) <br>
- [Kiln documentation](https://kiln3d.com/docs) <br>
- [PyPI package](https://pypi.org/project/kiln3d/) <br>
- [Project repository](https://github.com/codeofaxel/Kiln) <br>
- [Release notes v1.3.1](https://github.com/codeofaxel/Kiln/releases/tag/v1.3.1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP server setup, printer-control commands, model search and generation steps, slicing guidance, and print-monitoring guidance.] <br>

## Skill Version(s): <br>
1.3.1 (source: server.json and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
