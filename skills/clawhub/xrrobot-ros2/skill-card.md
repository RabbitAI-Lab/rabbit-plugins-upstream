## Description: <br>
Controls, checks, and troubleshoots XRRobot systems running ROS 2 Jazzy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ceoifung](https://clawhub.ai/user/ceoifung) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and robot operators use this skill on an XRRobot host to inspect ROS 2 state, run bounded robot-control commands, navigate to known locations, capture camera data, and troubleshoot robot workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Robot-control commands can cause physical movement, including navigation, drive, grasp, follow, lane-keeping, or autonomous-driving actions. <br>
Mitigation: Use only on the intended XRRobot host with an operator present, a cleared workspace, verified stop procedures, and explicit authorization for physical actions. <br>
Risk: Camera capture and model-training workflows may include sensitive visual data. <br>
Mitigation: Confirm data handling expectations before capture or training, and keep robot web interfaces on a trusted local network. <br>
Risk: Concurrent robot-control modes can conflict, especially multiple publishers or controllers acting on movement commands. <br>
Mitigation: Check ROS 2 state and mode readiness before movement, avoid overlapping control modes, and stop on failure before continuing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ceoifung/skills/xrrobot-ros2) <br>
- [operations - XRRobot ROS2 robot control](references/operations.md) <br>
- [orchestration - multi-step workflow planning](references/orchestration.md) <br>
- [base - chassis drive](references/base.md) <br>
- [navigation - Nav2 laser navigation](references/navigation.md) <br>
- [mapping - laser SLAM mapping](references/mapping.md) <br>
- [camera - camera capture](references/camera.md) <br>
- [lidar - laser scan](references/lidar.md) <br>
- [grasp - vision grasping](references/grasp.md) <br>
- [task_orchestrator - visual task workflows](references/task_orchestrator.md) <br>
- [yolo - data collection, training, and detection](references/yolo.md) <br>
- [vision - MediaPipe vision dashboard](references/vision.md) <br>
- [voice - offline voice control](references/voice.md) <br>
- [autopilot - vision autopilot](references/autopilot.md) <br>
- [lanekeeping - lane keeping](references/lanekeeping.md) <br>
- [follower - laser following](references/follower.md) <br>
- [guard - laser guard](references/guard.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, ROS 2 command examples, JSON status summaries, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce commands that interact with physical robot hardware and may report camera, lidar, navigation, or waypoint data.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
