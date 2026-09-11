## Description:

RDK YOLO Toolkit helps agents guide YOLO training, ONNX export, hb_mapper quantization, RDK X5 BPU inference, and optional TROS ROS2 detection deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxma615](https://clawhub.ai/user/maxma615)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and robotics engineers use this skill to move YOLO models through training, BPU quantization, RDK X5 validation, and ROS2 integration with stage-by-stage commands and checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to run broad local and remote shell commands, including package installation and SSH operations.

Mitigation: Use a dedicated non-production host or least-privilege account, review commands before execution, and avoid sharing passwords.

Risk: The skill includes persistent background execution patterns for training and ROS2 nodes.

Mitigation: Use tmux or nohup only for intended long-running jobs, log their output, and clean up background processes after validation.

Risk: The artifact contains examples that may loosen device-node permissions on RDK hardware.

Mitigation: Prefer root-only access or a properly scoped device group, and avoid chmod 666 on device nodes unless explicitly accepted for a controlled test system.

Risk: The environment setup downloads installers and packages from external package repositories.

Mitigation: Pin or verify installers and dependencies where possible, and review package sources before running installation scripts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/maxma615/skills/rdk-yolo-toolkit)
- [Official YOLO ROS documentation](https://developer.d-robotics.cc/rdk_doc/Robot_development/boxs/detection/yolo)
- [Official RDK X5 toolchain manual](https://developer.d-robotics.cc/api/v1/fileData/x5_doc-v126cn/index.html)
- [Official RDK X5 hbm_runtime Python API](https://developer.d-robotics.cc/rdk_x_doc/Basic_Application/multi_media_sp_dev_api/RDK_X5/pydev_multimedia_api_x5/ai-python-api)
- [D-Robotics ultralytics_yolo sample](https://github.com/D-Robotics/rdk_model_zoo/tree/rdk_x5/samples/vision/ultralytics_yolo)
- [D-Robotics ultralytics_yolo26 sample](https://github.com/D-Robotics/rdk_model_zoo/tree/rdk_x5/samples/vision/ultralytics_yolo26)
- [HobotDnn changelog](https://github.com/D-Robotics/hobot_dnn/blob/develop/dnn_node/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local or SSH command sequences, environment checks, dataset and HobotDnn configuration examples, and validation checkpoints.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
