## Description: <br>
Connect to remote desktops via RDP, VNC, and SSH X11 with secure tunneling and troubleshooting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and system administrators use this skill to choose remote desktop protocols, prepare connection commands, set up SSH tunnels, and troubleshoot RDP, VNC, and SSH X11 display issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Troubleshooting commands may weaken certificate checks when users copy them without review. <br>
Mitigation: Review every generated command before execution and avoid /cert:ignore except as a temporary controlled diagnostic. <br>
Risk: Firewall and audio troubleshooting commands may expose network services. <br>
Mitigation: Restrict firewall openings to trusted source IPs or tunnels and avoid anonymous PulseAudio TCP. <br>
Risk: Connection examples and saved host profiles may expose sensitive infrastructure details or credentials if used carelessly. <br>
Mitigation: Do not put real passwords on command lines, never save passwords, and review or delete saved host profiles that contain sensitive details. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/haidiantoutou/skills/remote-desktop) <br>
- [Skill Homepage](https://clawic.com/skills/remote-desktop) <br>
- [Setup - Remote Desktop](setup.md) <br>
- [Protocols - Remote Desktop](protocols.md) <br>
- [Troubleshooting - Remote Desktop](troubleshooting.md) <br>
- [Memory Template - Remote Desktop](memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose local host profile files under ~/remote-desktop/ with user consent; does not store passwords.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, release evidence, _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
