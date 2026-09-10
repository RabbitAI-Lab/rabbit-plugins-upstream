## Description:

Manage Huawei Cloud ModelArts dedicated resource pools and node pools through full lifecycle operations via hcloud CLI, covering resource pool management, pool nodes, node pools, network resources, tags, plugins, workloads, scheduled events, OS configuration, and resource flavor/event queries, with BSS pricing inquiry before chargeable operations and confirmation for write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and platform engineers use this skill to administer Huawei Cloud ModelArts dedicated resource pools and node pools through guided hcloud CLI workflows. It supports read, write, pricing, troubleshooting, IAM, and pre-flight checks for resource pool operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful cloud-changing actions for Huawei Cloud ModelArts resource pools.

Mitigation: Use a least-privilege IAM user and require explicit review and confirmation before create, update, delete, resize, reboot, accept, or chargeable actions.

Risk: Credential handling needs review because the release evidence flags a credential-handling contradiction.

Mitigation: Do not paste AK/SK into chat or agent-run code; configure credentials outside the agent session and use presence-only checks.

Risk: The release evidence flags a recommended remote installer script.

Mitigation: Review installer scripts before running them and prefer controlled installation steps when operating in managed environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-modelarts-resource-pool-management)
- [CLI Command Examples](references/cli-command-examples.md)
- [API Paths](references/api-paths.md)
- [IAM Policies](references/iam-policies.md)
- [Known Issues and Workarounds](references/known-issues.md)
- [BSS On-Demand Pricing Inquiry](references/pricing-inquiry.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud hcloud CLI Documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline hcloud CLI commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pricing inquiry steps and confirmation prompts before chargeable or write operations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
