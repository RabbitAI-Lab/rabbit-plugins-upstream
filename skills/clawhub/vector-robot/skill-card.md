## Description: <br>
Control an Anki Vector robot through wire-pod, including speech, camera snapshots, movement, eye color changes, and animations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bogorman](https://clawhub.ai/user/bogorman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and robot operators use this skill to control a local Anki Vector robot running wire-pod, including speech output, camera capture, movement, settings changes, and OpenClaw voice-command proxy setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Physical robot control and camera access can affect the local environment, and behavior control disables cliff sensors during movement. <br>
Mitigation: Operate the robot under supervision, keep it away from edges or hazards, use conservative wheel commands, and release behavior control when finished. <br>
Risk: The speech helper handles text for URL encoding before sending it to wire-pod. <br>
Mitigation: Patch or replace the helper before passing untrusted text, and review generated speech commands before execution. <br>
Risk: The optional proxy and LaunchAgent can create an always-on local service for voice-command handling. <br>
Mitigation: Run the proxy only when needed, bind it to localhost with authentication, and install the LaunchAgent only when persistent startup is intentional. <br>
Risk: Prompt files, response files, proxy logs, and camera snapshots may contain private local data. <br>
Mitigation: Store these files in a protected location, limit access permissions, and delete them when no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bogorman/skills/vector-robot) <br>
- [wire-pod SDK API Reference](references/api.md) <br>
- [wire-pod](https://github.com/kercre123/wire-pod) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with bash, curl, JavaScript, JSON, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local wire-pod API calls, helper scripts, proxy setup steps, and safety guidance for physical robot operation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
