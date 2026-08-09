## Description: <br>
Migrate vision, detection, and segmentation small models to Ascend NPU with model structure analysis, migration verification, performance profiling, and optimization guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate small computer vision models such as ResNet, YOLO, and UNet to Ascend NPU, verify NPU inference and accuracy, profile operator performance, and identify optimization steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags embedded privileged root SSH access, including a concrete-looking password. <br>
Mitigation: Do not use the embedded credential; treat it as exposed, rotate it if it may be real, and use non-root accounts with SSH keys or managed secrets. <br>
Risk: The skill can lead an agent to run Docker, package installation, SSH, and profiling commands against an Ascend server. <br>
Mitigation: Require explicit target confirmation, review commands before execution, and validate on staging or test hosts before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascend-small-model-migrate) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Report Template](references/report-template.md) <br>
- [Profiler SQL](references/profiler-sql.md) <br>
- [Migration Scripts](references/migration-scripts.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash, Python, and SQL code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces migration analysis, verification reports, profiling summaries, optimization recommendations, and helper commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
