## Description: <br>
Control Nanoleaf light panels through the Picoleaf CLI for power, brightness, color, and color temperature changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rstierli](https://clawhub.ai/user/rstierli) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to set up and operate Nanoleaf light panels from an agent through Picoleaf CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing Picoleaf from third-party package sources can introduce package-source trust risk. <br>
Mitigation: Install only if you trust the Picoleaf package source, prefer Homebrew when available, and keep the CLI updated. <br>
Risk: The Nanoleaf access token is stored in ~/.picoleafrc and can allow local device control if exposed. <br>
Mitigation: Keep ~/.picoleafrc private with restrictive permissions such as 600 and regenerate the Nanoleaf token if the file is exposed or shared. <br>


## Reference(s): <br>
- [Nanoleaf Skill on ClawHub](https://clawhub.ai/rstierli/skills/nanoleaf) <br>
- [Picoleaf Project](https://github.com/tessro/picoleaf) <br>
- [Picoleaf Linux Binary Download](https://github.com/tessro/picoleaf/releases/latest/download/picoleaf_1.4.0_linux_amd64.tar.gz) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the picoleaf binary and a local ~/.picoleafrc containing the Nanoleaf host and access token.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
