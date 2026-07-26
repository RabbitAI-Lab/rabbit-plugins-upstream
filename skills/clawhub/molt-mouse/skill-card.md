## Description: <br>
Local mouse control via ydotool wrapper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oguzhaslak](https://clawhub.ai/user/oguzhaslak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to let an agent move, click, hold, and drag the local Linux mouse through the reviewed molt-mouse command wrapper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move and click the local Linux mouse, which may affect focused applications or sensitive dialogs. <br>
Mitigation: Install it only when intentional, avoid leaving payment screens or administrative prompts focused, and verify actions before use. <br>
Risk: Incorrect or ambiguous coordinates may trigger unintended pointer actions. <br>
Mitigation: Give explicit coordinates or deltas, and rely on the skill's prompt-for-clarification behavior when numerical input is missing or unclear. <br>
Risk: Using an unexpected local wrapper could change the reviewed behavior. <br>
Mitigation: Verify that the local molt-mouse command is the reviewed wrapper before enabling the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oguzhaslak/skills/molt-mouse) <br>
- [Publisher profile](https://clawhub.ai/user/oguzhaslak) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance] <br>
**Output Format:** [Text with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Linux-only; requires the local molt-mouse command and ydotool socket.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
