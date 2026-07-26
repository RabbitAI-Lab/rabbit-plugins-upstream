## Description: <br>
Install skills from GitHub repositories into the local skills directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[isaiahmaniac-sketch](https://clawhub.ai/user/isaiahmaniac-sketch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to list available skills from GitHub repositories and install selected skill directories into a local skills directory for future sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installed skills persist locally and can influence future agent behavior. <br>
Mitigation: Install only from trusted GitHub repositories, review the target SKILL.md before installation, and start a new session only after confirming the installed skill is appropriate. <br>
Risk: Private repository installation may involve GitHub authentication tokens. <br>
Mitigation: Use tokens only for trusted repositories and avoid exposing token values in prompts, logs, or shared command output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/isaiahmaniac-sketch/skills/skill-installer) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the user to choose a skill before installation and may reference GitHub authentication tokens for private repositories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
