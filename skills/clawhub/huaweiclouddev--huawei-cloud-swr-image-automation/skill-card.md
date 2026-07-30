## Description: <br>
Huawei Cloud SWR (Software Repository for Container) image automation and operations skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to configure Huawei Cloud SWR cross-region image sync, inspect sync status, and manage CCE/CCI auto-deploy triggers with hcloud CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide changes to SWR sync settings and CCE/CCI deployment triggers that affect live workloads. <br>
Mitigation: Review every generated hcloud command before confirming it, and test sync or trigger examples against non-production resources before applying them to live workloads. <br>
Risk: Broad or long-lived Huawei Cloud credentials could expand the impact of a mistaken command. <br>
Mitigation: Use least-privilege IAM credentials, prefer temporary credentials, and avoid exposing AK, SK, or security token values in commands or conversation. <br>
Risk: Image sync with overwrite enabled can replace existing images in the target region. <br>
Mitigation: Confirm the override setting explicitly and keep override disabled unless replacing target images is intended. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-image-automation) <br>
- [Huawei Cloud SWR Quick Start](https://support.huaweicloud.com/qs-swr/index.html) <br>
- [Huawei Cloud KooCLI Updates](https://support.huaweicloud.com/wtsnew-hcli/index.html) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [SWR Automation API Reference Guide](references/swr-automation-api-guide.md) <br>
- [Task: Image Sync](references/task-image-sync.md) <br>
- [Task: Trigger Management](references/task-trigger-management.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls and Solutions](references/common-pitfalls.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline hcloud CLI commands and JSON policy examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may affect Huawei Cloud SWR sync settings and CCE/CCI deployment triggers; write operations require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
