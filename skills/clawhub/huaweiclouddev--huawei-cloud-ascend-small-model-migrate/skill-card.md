## Description: <br>
Migrates vision, detection, and segmentation small models to Ascend NPU with model structure analysis, migration verification, performance profiling, and optimization guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to assess and migrate supported computer vision models such as ResNet, YOLO, and UNet from GPU-oriented workflows to Ascend NPU. It helps produce model analysis, NPU verification, profiling, bottleneck analysis, and optimization recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports exposed root SSH credentials. <br>
Mitigation: Remove the plaintext credential, rotate any affected password, and use authorized least-privilege SSH access. <br>
Risk: The skill normalizes privileged server and container actions. <br>
Mitigation: Run commands only in disposable or approved test environments and review proposed actions before execution. <br>
Risk: The workflow may install packages and load model artifacts. <br>
Mitigation: Pin and review package changes, and load only trusted model artifacts or safer checkpoint formats. <br>
Risk: The security verdict is suspicious for real infrastructure use. <br>
Mitigation: Do not install or use the skill as-is against production or sensitive infrastructure. <br>


## Reference(s): <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Migration Report Template](references/report-template.md) <br>
- [Performance Analysis SQL Query Reference](references/profiler-sql.md) <br>
- [Migration Verification Scripts Reference](references/migration-scripts.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline bash, Python, and SQL snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes model analysis, NPU verification, profiling, troubleshooting, and optimization recommendations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
