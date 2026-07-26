## Description: <br>
Intiface Direct Control lets OpenClaw agents control Buttplug-compatible intimate devices through Intiface Central using direct Buttplug v4 WebSocket commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chizumystic](https://clawhub.ai/user/chizumystic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Adults using OpenClaw can list, start, loop, pattern, and stop Buttplug-compatible devices through a local Intiface Central server. The skill is intended for agent-assisted device control where the user explicitly sets device, intensity, and duration limits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can keep intimate hardware running through loop commands or generated pattern scripts. <br>
Mitigation: Require explicit duration and intensity limits for every command, and confirm that the user can stop the device with the stop command or by closing Intiface Central. <br>
Risk: Remote WebSocket URLs can expose device control beyond the local machine if the Intiface server is reachable on a network. <br>
Mitigation: Use only a local Intiface server by default and keep remote WebSocket access disabled unless the user intentionally configures and controls it. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chizumystic/skills/intiface-direct-package) <br>
- [Intiface Central](https://intiface.com/central/) <br>
- [Buttplug-compatible device index](https://iostindex.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May run Node.js commands against an Intiface Central WebSocket server when used by an agent.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
