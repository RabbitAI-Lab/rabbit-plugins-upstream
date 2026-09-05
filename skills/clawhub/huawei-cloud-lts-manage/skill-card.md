## Description:

Huawei Cloud LTS (Log Tank Service) full lifecycle management via hcloud CLI for log groups, log streams, indexes, transfer tasks, keyword and SQL alarm rules, log search, and diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to administer Huawei Cloud LTS resources, inspect logs, configure transfers and alarms, and diagnose incidents through hcloud CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete Huawei Cloud LTS resources, including log groups, streams, transfer tasks, alarm rules, and retention settings.

Mitigation: Require explicit human approval before any create, update, alarm-status, TTL, transfer, or delete action in production.

Risk: Delete operations can remove important logging resources, and deleting a log group can affect streams under that group.

Mitigation: Allow only single-resource delete requests with a specific resource ID, confirm cascade impact, and prohibit wildcard or batch deletion.

Risk: The documented setup and IAM permissions are broad enough to administer production logging resources.

Mitigation: Use the read-only IAM policy for search and diagnosis when mutation is not required, and otherwise scope permissions to the smallest project and resource set available.

Risk: The CLI installation flow downloads and executes an external installer script.

Mitigation: Verify the hcloud installer source and integrity before execution and install only in environments intended for Huawei Cloud LTS administration.

## Reference(s):

- [Huawei Cloud LTS Manage on ClawHub](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-lts-manage)
- [Huawei Cloud CLI installer](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [LTS Alarm Rule Configuration Reference](references/lts-alarm-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with hcloud CLI command examples and JSON result expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query operations return summarized JSON results; create, update, and delete operations should return a resource configuration snapshot or verification result.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
