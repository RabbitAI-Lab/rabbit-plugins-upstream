## Description: <br>
Automates batch creation and management of Huawei Cloud CES alarm rules for ECS instances using hcloud CLI v7.2.2+. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to configure Huawei Cloud ECS monitoring alarms, manage SMN notification subscriptions, and query CES metrics or alarm state for operational review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can require broad Huawei Cloud permissions for CES and SMN alarm management. <br>
Mitigation: Use a least-privilege IAM policy where possible and grant access only to users who intentionally need agent-assisted ECS/CES alarm management. <br>
Risk: Credential handling guidance involves Huawei Cloud access keys. <br>
Mitigation: Prefer temporary credentials, configure credentials through hcloud or environment variables, and avoid pasting AK/SK values into chat or shell history. <br>
Risk: Installer guidance may involve downloading and running an external installer. <br>
Mitigation: Verify any downloaded installer before execution and prefer trusted package-manager installation paths when available. <br>
Risk: Notification subscription changes can remove or silence alert paths. <br>
Mitigation: Require explicit confirmation before creating, updating, removing, or deleting notification paths, and verify alarms and subscriptions after changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ecs-alert) <br>
- [CLI Installation Guide](artifact/references/cli-installation-guide.md) <br>
- [IAM Policies](artifact/references/iam-policies.md) <br>
- [Related APIs](artifact/references/related-apis.md) <br>
- [SMN Subscription Guide](artifact/references/smn-subscription-guide.md) <br>
- [Memory Monitoring Guide](artifact/references/memory-monitoring-guide.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>
- [Huawei Cloud IAM Documentation](https://support.huaweicloud.com/iam/index.html) <br>
- [Huawei Cloud CES Console](https://console.huaweicloud.com/ces) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with bash command examples and scripts that can emit table, JSON, or ID-list output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write operations should be confirmed before execution; generated shell commands depend on hcloud CLI credentials and region configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
