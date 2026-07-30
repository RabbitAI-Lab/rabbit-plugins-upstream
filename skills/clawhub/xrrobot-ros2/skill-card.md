## Description: <br>
Controls, checks, and troubleshoots an XRRobot running ROS 2 Jazzy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceoifung](https://clawhub.ai/user/ceoifung) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and robot operators use this skill to inspect, control, navigate, and troubleshoot a local XRRobot ROS 2 Jazzy workspace while preserving read-only project sources and requiring explicit authorization for physical actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can initiate real robot motion, grasping, autonomous following, and autonomous driving. <br>
Mitigation: Use only on a supervised XRRobot host with a clear operating area, accessible emergency stop, bounded movement durations, and explicit confirmation before physical actions. <br>
Risk: Motion and navigation may be unsafe if localization, sensors, or controller state are not verified. <br>
Mitigation: Verify localization, sensor status, navigation readiness, and conflicting command publishers before sending movement or navigation commands. <br>
Risk: Robot web UIs, camera captures, and training data may expose sensitive operational data. <br>
Mitigation: Keep web interfaces on a trusted network or behind access controls, and treat captures and training datasets as sensitive. <br>
Risk: Security evidence reports inconsistent safety gates in the instructions. <br>
Mitigation: Review the skill before installation and deployment on hardware, with particular attention to physical action authorization and web-tool exposure. <br>


## Reference(s): <br>
- [XRRobot ROS 2 skill page](https://clawhub.ai/ceoifung/skills/xrrobot-ros2) <br>
- [autopilot](references/autopilot.md) <br>
- [base](references/base.md) <br>
- [camera](references/camera.md) <br>
- [follower](references/follower.md) <br>
- [grasp](references/grasp.md) <br>
- [guard](references/guard.md) <br>
- [lanekeeping](references/lanekeeping.md) <br>
- [lidar](references/lidar.md) <br>
- [mapping](references/mapping.md) <br>
- [navigation](references/navigation.md) <br>
- [operations](references/operations.md) <br>
- [orchestration](references/orchestration.md) <br>
- [task_orchestrator](references/task_orchestrator.md) <br>
- [vision](references/vision.md) <br>
- [voice](references/voice.md) <br>
- [yolo](references/yolo.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local ROS 2 commands, bounded robot actions, status checks, and the user waypoint YAML file.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
