## Description: <br>
Controls, checks, and troubleshoots an XRRobot running ROS 2 Jazzy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceoifung](https://clawhub.ai/user/ceoifung) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and robot operators use this skill on an XRRobot host to inspect ROS 2 state, run bounded robot-control commands, manage navigation waypoints, and troubleshoot camera, lidar, navigation, grasping, vision, voice, and orchestration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Robot motion, navigation, grasping, following, lane-keeping, autopilot, and orchestration actions can move physical hardware. <br>
Mitigation: Use only on the intended XRRobot host, keep the area clear, supervise the robot locally, keep a stop path available, require explicit authorization for physical actions, and use bounded motion durations followed by stop commands. <br>
Risk: Multiple controllers can compete for the base command topic or other exclusive robot resources. <br>
Mitigation: Check robot mode, readiness, nodes, topics, and conflicting command publishers before starting motion; run one base-control mode at a time. <br>
Risk: Navigation and grasping can fail or act on an unintended target if localization, map state, model classes, depth data, or target pose are not ready. <br>
Mitigation: Run navigation readiness checks, verify named waypoints or poses, observe targets first, confirm supported model classes, and use dry-run checks before real grasping. <br>
Risk: Camera capture, YOLO data collection, model training, and local web interfaces can expose sensitive image data or control surfaces. <br>
Mitigation: Expose web interfaces only on trusted networks and collect or process camera data only in appropriate spaces with consent from affected people. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ceoifung/skills/xrrobot-ros2) <br>
- [Operations](references/operations.md) <br>
- [Orchestration](references/orchestration.md) <br>
- [Base drive](references/base.md) <br>
- [Navigation](references/navigation.md) <br>
- [Mapping](references/mapping.md) <br>
- [Camera](references/camera.md) <br>
- [Lidar](references/lidar.md) <br>
- [Grasping](references/grasp.md) <br>
- [Task orchestrator](references/task_orchestrator.md) <br>
- [YOLO](references/yolo.md) <br>
- [Vision](references/vision.md) <br>
- [Autopilot](references/autopilot.md) <br>
- [Lane keeping](references/lanekeeping.md) <br>
- [Follower](references/follower.md) <br>
- [Guard](references/guard.md) <br>
- [Voice](references/voice.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce bounded local ROS 2 command suggestions or invocations, status summaries, troubleshooting guidance, and waypoint configuration updates.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
