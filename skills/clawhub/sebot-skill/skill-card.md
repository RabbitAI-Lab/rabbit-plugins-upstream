## Description: <br>
Guides agents in connecting to and operating a commercial service robot over SSH and ROS topics for chat, ordering, visual observation, and status checking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gittxbb](https://clawhub.ai/user/gittxbb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a commercial service robot on a trusted local network, send supported natural-language commands through ROS topics, and validate robot replies and task state. It covers conversation, food ordering, visual observation, checkout, and troubleshooting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using this skill may gain root-level SSH control over a physical robot even though the workflow only needs scoped ROS messaging. <br>
Mitigation: Use a dedicated least-privilege robot account or broker limited to the documented /agent/cmd, /agent/reply, and /audio operations, and avoid shared root credentials. <br>
Risk: Robot-control commands can affect physical task execution during ordering, navigation, and visual workflows. <br>
Mitigation: Install only on a trusted robot and network, supervise execution, and wait for documented idle or completion signals before sending additional commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gittxbb/skills/sebot-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, ROS topic examples, and a Python SSH client example] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational constraints for robot busy states, topic usage, network setup, timeouts, and success or failure checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
