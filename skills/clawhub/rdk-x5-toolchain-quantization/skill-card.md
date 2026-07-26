## Description: <br>
Toolchain-level skill for D-Robotics / Horizon Robotics RDK X5 OpenExplorer v1.2.8 post-training quantization (PTQ), covering ONNX-to-.bin/.hbm conversion, calibration data preparation, YAML configuration, compilation, accuracy verification, performance profiling, and accuracy tuning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shockley6668](https://clawhub.ai/user/shockley6668) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to convert arbitrary ONNX models into RDK X5 deployable .bin or .hbm artifacts and to troubleshoot OpenExplorer PTQ setup, calibration, compilation, accuracy, and performance issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow examples process local models and calibration data inside vendor Docker images. <br>
Mitigation: Review the vendor Docker image before use and mount only the project directory needed for conversion. <br>


## Reference(s): <br>
- [OpenExplorer Setup For RDK X5](references/setup.md) <br>
- [YAML Reference](references/yaml-reference.md) <br>
- [Calibration Data](references/calibration.md) <br>
- [Accuracy Verification](references/accuracy.md) <br>
- [Accuracy Tuning](references/accuracy-tuning.md) <br>
- [Performance Profiling](references/performance.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with bash, Python, YAML, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces workflow guidance for local model conversion, verification, profiling, and troubleshooting.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
