## Description:

Automate batch creation and management of Huawei Cloud CES alarm rules for ECS instances using hcloud CLI v7.2.2+, including template-based alarms, SMN notification updates, and ECS metrics or alarm queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to configure Huawei Cloud ECS monitoring alarms in batches, manage SMN notification subscriptions, and query CES metrics or alarm lists through guided hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Huawei Cloud monitoring alarms and notification settings, which may affect operational alerting.

Mitigation: Require explicit confirmation before any create, update, or delete operation and verify results with the provided list or query commands.

Risk: Broad CES or SMN permissions can increase impact if credentials are misused.

Mitigation: Use a narrowly scoped Huawei Cloud IAM user and prefer the custom least-privilege policy over FullAccess.

Risk: Installer downloads and command-line AK/SK handling can create supply-chain or credential exposure risk.

Mitigation: Verify installer downloads before running them, configure credentials with hcloud where possible, and avoid passing AK/SK on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ecs-alert)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Common Commands](references/common-commands.md)
- [IAM Policies](references/iam-policies.md)
- [Memory Monitoring Guide](references/memory-monitoring-guide.md)
- [Related APIs](references/related-apis.md)
- [SMN Subscription Guide](references/smn-subscription-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Huawei Cloud KooCLI install script](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON, table, or ID-list command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run command previews and confirmation prompts for create, update, or subscription deletion operations.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
