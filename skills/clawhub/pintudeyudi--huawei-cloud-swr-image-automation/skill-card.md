## Description:

Huawei Cloud SWR Image Automation helps agents guide cross-region image synchronization, sync job checks, and CCE/CCI auto-deploy trigger management with the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pintudeyudi](https://clawhub.ai/user/pintudeyudi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to operate Huawei Cloud SWR image replication and deployment triggers, including read-only checks before creating, updating, or deleting sync and trigger configurations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutating Huawei Cloud SWR commands can create, update, or delete sync and trigger configurations that affect live workloads.

Mitigation: Use least-privilege IAM scoped to specific SWR namespaces, repositories, and regions, begin with read-only checks, and require explicit human approval before create, update, or delete commands.

Risk: Enabled auto-deploy triggers and broad conditions such as condition=.* can update CCE or CCI workloads whenever matching images are pushed.

Mitigation: Start with triggers disabled where possible, prefer narrow tag or regex conditions, and verify the target cluster, namespace, workload, and container before enabling automation.

Risk: Image synchronization with override=true can overwrite existing images in target regions.

Mitigation: Default to override=false and use override=true only after verifying the target images and confirming overwrite intent.

Risk: Auto-sync with syncAuto=true persists and continues replicating future image pushes until removed.

Mitigation: Start with syncAuto=false for validation, audit sync configurations, and delete unwanted auto-sync rules when they are no longer needed.

## Reference(s):

- [SWR Automation API Reference Guide](references/swr-automation-api-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Task: Image Sync](references/task-image-sync.md)
- [Task: Trigger Management](references/task-trigger-management.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls and Solutions](references/common-pitfalls.md)
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html)
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/)
- [ClawHub Skill Page](https://clawhub.ai/pintudeyudi/skills/huawei-cloud-swr-image-automation)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and JSON policy examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud operations that require explicit user confirmation and least-privilege Huawei Cloud IAM permissions.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
