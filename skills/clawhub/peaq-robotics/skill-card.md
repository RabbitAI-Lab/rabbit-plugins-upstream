## Description: <br>
Core peaq-robotics-ros2 runtime for OpenClaw. Start/stop ROS 2 nodes and call DID, storage, and access-control services. Use when requests are about running an existing peaq ROS2 workspace, not installing, building, or sending funds. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lavish0000](https://clawhub.ai/user/lavish0000) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and robotics engineers use this skill to operate an already-built peaq Robotics ROS 2 workspace from an agent session. It supports node lifecycle actions and DID, storage, identity-card, and access-control service calls while leaving installation, build setup, and value transfers outside the core workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start background ROS 2 nodes and leave them running after the immediate task. <br>
Mitigation: Use the matching stop commands for launched nodes and review log and PID locations before long-running operation. <br>
Risk: DID, storage, and access-control service calls can change robot identity or permission state in the configured peaq ROS 2 workspace. <br>
Mitigation: Review requested DID metadata, storage keys and values, roles, permissions, and user identifiers before approving service calls. <br>
Risk: JSON payloads may contain sensitive information that will be sent through ROS 2 service calls or stored by the workspace. <br>
Mitigation: Avoid placing secrets in JSON arguments or @json files and keep payload files within the documented allowed roots. <br>
Risk: Commands require an already-built workspace and externally initialized ROS environment. <br>
Mitigation: Confirm ros2, python3, PEAQ_ROS2_ROOT, configuration YAML, and the ROS workspace overlay are ready before using runtime commands. <br>


## Reference(s): <br>
- [peaq-robotics-ros2 service map](references/peaq_ros2_services.md) <br>
- [ClawHub skill page](https://clawhub.ai/lavish0000/skills/peaq-robotics) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON] <br>
**Output Format:** [Markdown or plain text with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ros2, python3, PEAQ_ROS2_ROOT, an initialized ROS environment, and an existing built peaq-robotics-ros2 workspace.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
