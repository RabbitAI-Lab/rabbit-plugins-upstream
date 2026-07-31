## Description: <br>
PixelLab lets an agent operate PixelLab through an OOMOL-connected account for reading, creating, updating, and deleting PixelLab data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and creative teams use this skill to operate PixelLab through OOMOL for pixel-art generation, conversion, editing, animation, asset management, and account balance checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can operate a PixelLab account with broad authority, including creating, editing, exporting, selecting, and deleting saved assets. <br>
Mitigation: Require explicit user confirmation for any action that changes assets, selects or discards candidates, starts jobs, exports data, deletes data, or may consume credits. <br>
Risk: Some state-changing actions may not be tagged as write or destructive in the artifact. <br>
Mitigation: Review the specific action and live schema before execution, and treat ambiguous actions as requiring confirmation. <br>
Risk: PixelLab operations may consume paid credits or fail due to billing limits. <br>
Mitigation: Check balance or billing errors before retrying credit-consuming work, and ask the user before running generation or Pro workflows. <br>


## Reference(s): <br>
- [ClawHub PixelLab Skill Page](https://clawhub.ai/oomol/skills/oo-pixellab) <br>
- [PixelLab Homepage](https://www.pixellab.ai/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects that may include returned data and an execution ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
