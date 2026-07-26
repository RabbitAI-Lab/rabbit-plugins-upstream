## Description: <br>
Visual AI activity indicator using Philips Hue lights. Pulse red when thinking, green when done. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jesserod329](https://clawhub.ai/user/jesserod329) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI assistant users use this skill to expose assistant activity through Philips Hue lights, such as pulsing red while work is in progress and turning green when the assistant is done. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The reviewed bundle references a hue executable that is not included. <br>
Mitigation: Verify the actual hue executable before installation or use. <br>
Risk: Hue Bridge credentials are stored in ~/.config/philips-hue/config.json. <br>
Mitigation: Keep the configuration file private and use restrictive file permissions. <br>
Risk: The skill controls local Philips Hue lights through a Hue Bridge. <br>
Mitigation: Use it only with a Hue Bridge and lights that the assistant is intended to control. <br>
Risk: Adding untrusted directories to PATH could cause an unintended hue executable to run. <br>
Mitigation: Avoid untrusted PATH entries and confirm which hue command is being invoked. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jesserod329/skills/philips-hue-thinking) <br>
- [README.md](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local hue executable, a Philips Hue Bridge, Philips Hue color bulbs, curl, and Bash 4.0 or newer.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
