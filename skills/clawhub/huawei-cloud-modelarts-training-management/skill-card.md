## Description: <br>
Manage Huawei Cloud ModelArts training jobs and related resources through the hcloud CLI, including job lifecycle operations, algorithms, experiments, model import, hyperparameter tuning, and image-save tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations teams use this skill to inspect and manage Huawei Cloud ModelArts training resources through CLI commands. It supports training job, algorithm, experiment, event, model import, auto-search, and training image-save workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes an unsafe curl-to-bash CLI installation path. <br>
Mitigation: Review the official CLI installation path before installing and avoid piping downloaded content directly into a shell. <br>
Risk: The skill can propose commands that mutate or delete Huawei Cloud resources. <br>
Mitigation: Require explicit user approval before create, update, stop, delete, agency creation, or other write operations. <br>
Risk: Broad ModelArts, IAM, and OBS permissions can expand the impact of mistakes. <br>
Mitigation: Use least-privilege Huawei Cloud credentials and narrow IAM and OBS permissions to the exact project, resource, and bucket prefixes needed. <br>
Risk: Agency creation and delete operations can have account-level cloud impact. <br>
Mitigation: Approve agency creation or deletion only after confirming the target project, resource IDs, and operational effect. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-modelarts-training-management) <br>
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts) <br>
- [CLI Command Examples](references/cli-command-examples.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Known Issues and Workarounds](references/known-issues.md) <br>
- [API Paths](references/api-paths.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline bash, JSON, and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Huawei Cloud region, authenticated hcloud or SDK credentials, relevant resource IDs, and explicit confirmation before write operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
