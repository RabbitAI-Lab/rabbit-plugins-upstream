## Description: <br>
Control a Reachy Mini robot by Pollen Robotics / Hugging Face via its REST API and SSH for movement, camera snapshots, audio direction sensing, volume, app management, status checks, and other physical robot interactions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[afalk42](https://clawhub.ai/user/afalk42) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and robot operators use this skill to let an agent control and inspect a Reachy Mini robot, including head, body, and antenna motion, expressions, dances, camera snapshots, microphone direction sensing, app management, and daemon status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can move a physical robot and trigger expressive behaviors. <br>
Mitigation: Install only for robots you own or administer, keep motors and motion commands supervised, and verify the robot is in a safe physical area before allowing agent-triggered movement. <br>
Risk: The skill can use the robot camera and microphone-derived speech direction, including patrol snapshots. <br>
Mitigation: Use camera patrol and audio direction features only with explicit consent from nearby people, and avoid enabling snapshot behavior in private or shared spaces without notice. <br>
Risk: The skill supports SSH-backed snapshot capture, default credentials, app management, daemon restarts, and raw robot API calls. <br>
Mitigation: Prefer SSH keys, change default credentials, verify host keys, avoid password-based sshpass use, and review raw API or service-management commands before execution. <br>


## Reference(s): <br>
- [Reachy Mini REST API Reference](references/api-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/afalk42/skills/reachy-mini) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to run robot-control shell scripts, REST API calls, SSH-backed snapshot capture, and contextual reaction commands.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
