## Description:

Guides developers through D-Robotics OpenExplorer v1.2.8 post-training quantization workflows for converting ONNX models into RDK X5 .bin and .hbm deployable artifacts, including environment setup, calibration data, YAML configuration, compilation, accuracy checks, performance evaluation, and troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxma615](https://clawhub.ai/user/maxma615)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and deployment engineers use this skill when converting ONNX models for RDK X5 boards with the D-Robotics OpenExplorer toolchain. It helps prepare calibration data, author hb_mapper YAML, compile deployable artifacts, and diagnose accuracy or performance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup material includes a reusable private registry credential.

Mitigation: Prefer the public Docker Hub image path or offline public downloads when available; if private registry access is required, use a user-managed secret and avoid copying credentials into logs, shell history, or automation.

Risk: The workflow asks users to download and run third-party D-Robotics toolchain images, SDKs, and model conversion utilities.

Mitigation: Pin the OpenExplorer version, verify downloaded artifacts independently where possible, and run the toolchain in a dedicated container or workspace.

Risk: Container examples mount local workspaces and generated commands may read or write model, calibration, and build artifacts.

Mitigation: Use a dedicated project directory and avoid mounting sensitive directories into the conversion container.

Risk: Post-training quantization can produce deployable artifacts with degraded accuracy or unacceptable latency for a target model.

Mitigation: Validate converted models with hb_verifier, hb_mapper infer, hb_perf, board-side hrt_model_exec tests, and task-level metrics before deployment.

## Reference(s):

- [RDK X5 OpenExplorer PTQ workflow](SKILL.md)
- [OE v1.2.8 environment setup](references/setup.md)
- [hb_mapper makertbin YAML reference](references/yaml-reference.md)
- [Calibration data guide](references/calibration.md)
- [Accuracy evaluation](references/accuracy.md)
- [Accuracy tuning](references/accuracy-tuning.md)
- [Performance evaluation and tuning](references/performance.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [D-Robotics OpenExplorer SDK v1.2.8](https://d-robotics-aitoolchain.oss-cn-beijing.aliyuncs.com/oe_x5/1.2.8/horizon_x5_open_explorer_v1.2.8-py310_20240926.tar.gz)
- [D-Robotics OpenExplorer v1.2.8 Chinese documentation](https://d-robotics-aitoolchain.oss-cn-beijing.aliyuncs.com/oe_x5/1.2.8/x5_doc-v1.2.8-py310-cn.zip)
- [D-Robotics OpenExplorer v1.2.8 English documentation](https://d-robotics-aitoolchain.oss-cn-beijing.aliyuncs.com/oe_x5/1.2.8/x5_doc-v1.2.8-py310-en.zip)
- [D-Robotics OpenExplorer v1.2.8 release notes](https://d-robotics-aitoolchain.oss-cn-beijing.aliyuncs.com/oe_x5/1.2.8/release_note_CN.txt)
- [D-Robotics custom operator forum reference](https://developer.horizon.cc/forumDetail/710365256928810)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, Python, and YAML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for toolchain commands, calibration scripts, YAML settings, validation checks, and troubleshooting steps; it does not execute conversion tools itself.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
