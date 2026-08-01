## Description: <br>
Daily (daily.co). Use this skill for ANY Daily request - reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to manage Daily rooms, meeting tokens, and domain configuration through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Daily resources by creating rooms, updating rooms, and creating meeting tokens. <br>
Mitigation: Review the exact payload and expected effect with the user before approving write actions. <br>
Risk: The skill can delete Daily rooms. <br>
Mitigation: Confirm the target room name and obtain explicit approval before running destructive actions. <br>
Risk: The setup path may install or invoke the oo CLI. <br>
Mitigation: Install the oo CLI only from a trusted source and run setup steps only after an authentication or connection failure. <br>


## Reference(s): <br>
- [Daily homepage](https://www.daily.co/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Daily skill on ClawHub](https://clawhub.ai/oomol/skills/oo-daily) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
