## Description: <br>
Kiln lets AI agents design, slice, print, monitor, and recover physical 3D printing jobs through MCP and CLI control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codeofaxel](https://clawhub.ai/user/codeofaxel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, makers, and print-farm operators use Kiln to let AI agents generate or find 3D models, slice them, control printer queues, and monitor physical prints with human supervision for high-risk actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent control of real 3D printers can heat hardware, move motors, start or cancel prints, or send G-code without adequate supervision. <br>
Mitigation: Keep printers supervised, require explicit approval before physical actions, and limit printer/API credentials to the minimum access needed. <br>
Risk: Camera, webhook, cloud sync, plugin, or self-update features can expand the exposure of printer access or workspace data. <br>
Mitigation: Disable camera, webhooks, cloud sync, plugins, and self-update paths unless they are intentionally required and reviewed. <br>
Risk: Model generation, marketplace search, slicing, and fulfillment can produce unsafe, incorrect, infringing, or costly physical outcomes. <br>
Mitigation: Review models, slicer settings, material choices, costs, and fulfillment orders before execution. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/codeofaxel/skills/kiln) <br>
- [Kiln website](https://kiln3d.com) <br>
- [Kiln documentation](https://kiln3d.com/docs) <br>
- [PyPI package](https://pypi.org/project/kiln3d/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text with shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger physical printer actions through configured credentials; require operator approval for heating, printing, canceling, sending G-code, and fulfillment.] <br>

## Skill Version(s): <br>
1.2.0 (source: server evidence release and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
