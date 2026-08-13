## Description:

Automates batch creation and management of Huawei Cloud CES alarm rules for ECS instances using hcloud CLI v7.2.2+.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to create, update, query, and verify Huawei Cloud ECS monitoring alarms and SMN notification subscriptions through hcloud CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security summary reports broad cloud privileges and risky credential guidance.

Mitigation: Use a dedicated least-privilege Huawei Cloud identity, prefer interactive hcloud configuration or a protected secret store, and avoid passing AK/SK values directly in command arguments.

Risk: The skill can create or modify alarms, notifications, IAM-related setup, and SMN subscriptions.

Mitigation: Manually confirm target resources, thresholds, topics, endpoints, and subscription URNs before running any write operation; use dry-run or read-only verification flows when available.

Risk: The server security guidance flags installer verification as a review requirement.

Mitigation: Install hcloud only from official signed or checksum-verified Huawei Cloud channels before using the bundled scripts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ecs-alert)
- [Huawei Cloud CLI installation guide](references/cli-installation-guide.md)
- [Common commands reference](references/common-commands.md)
- [IAM policies](references/iam-policies.md)
- [Memory monitoring guide](references/memory-monitoring-guide.md)
- [Related APIs](references/related-apis.md)
- [SMN subscription guide](references/smn-subscription-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Huawei Cloud CLI installer](https://hwcloudcli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON or table outputs from scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose hcloud CLI commands and bundled script invocations; write operations require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
