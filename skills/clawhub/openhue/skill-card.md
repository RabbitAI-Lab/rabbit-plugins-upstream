## Description: <br>
Control Philips Hue lights/scenes via the OpenHue CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to install and operate the OpenHue CLI so an agent can discover, read, and change Philips Hue lights, rooms, and scenes through a Hue Bridge. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and using the OpenHue Homebrew package executes third-party CLI software. <br>
Mitigation: Install only if you trust the OpenHue Homebrew package and intend the agent to control your Philips Hue Bridge. <br>
Risk: The skill can change physical Philips Hue lights, rooms, and scenes. <br>
Mitigation: Pair only with your own bridge, and have the agent confirm specific lights, rooms, or scenes before making changes. <br>


## Reference(s): <br>
- [OpenHue CLI documentation](https://www.openhue.io/cli) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/openhue) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the OpenHue CLI and a paired Philips Hue Bridge.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
