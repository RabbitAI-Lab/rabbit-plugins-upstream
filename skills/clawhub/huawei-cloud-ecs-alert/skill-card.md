## Description: <br>
Automates batch creation and management of Huawei Cloud CES alarm rules for ECS instances using hcloud CLI v7.2.2+. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations teams use this skill to query Huawei Cloud ECS resources, create CES alarm rules in batches, configure SMN notifications, and inspect metrics or alarm state through hcloud-based shell workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make persistent Huawei Cloud alert and notification changes, including recipient removal. <br>
Mitigation: Require explicit review of the operation, target resources, and recipients before any create, update, remove, unsubscribe, or delete-subscription action. <br>
Risk: Huawei Cloud hcloud credentials can authorize cloud changes across ECS, CES, and SMN. <br>
Mitigation: Use a least-privileged custom IAM policy or temporary credentials, and do not paste long-lived AK/SK values into chat or command history. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ecs-alert) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Related APIs](references/related-apis.md) <br>
- [SMN Subscription Guide](references/smn-subscription-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Huawei Cloud IAM documentation](https://support.huaweicloud.com/iam/index.html) <br>
- [Huawei Cloud IAM policy management](https://support.huaweicloud.com/usermanual-iam/iam_01_003.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation or update of Huawei Cloud CES alarms and SMN subscriptions; write operations require explicit user review before execution.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
