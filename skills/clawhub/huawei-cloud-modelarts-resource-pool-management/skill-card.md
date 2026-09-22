## Description:

Manage Huawei Cloud ModelArts dedicated resource pools and node pools through hcloud CLI workflows covering lifecycle, node, network, tag, plugin, workload, scheduled event, OS configuration, flavor, and pricing operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and platform operators use this skill to inspect and manage Huawei Cloud ModelArts dedicated resource pools, node pools, network resources, tags, plugins, workloads, scheduled events, OS settings, and resource flavors. It also guides pricing inquiry before chargeable create or expansion operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact cloud operations such as reset, delete, resize, plugin creation, and scheduled-event acceptance.

Mitigation: Use least-privilege Huawei Cloud IAM permissions, prefer read-only permissions unless writes are required, and require explicit user confirmation before high-impact actions.

Risk: The release security summary flags unsafe hcloud install guidance.

Mitigation: Verify any hcloud installer or downloaded CLI package out of band before running it.

Risk: The release security summary flags inconsistent credential-handling instructions.

Mitigation: Do not expose AK/SK values to the agent; configure credentials outside the agent session and use only credential presence checks.

## Reference(s):

- [CLI Command Examples](references/cli-command-examples.md)
- [API Paths](references/api-paths.md)
- [IAM Policies](references/iam-policies.md)
- [Known Issues and Workarounds](references/known-issues.md)
- [BSS On-Demand Pricing Inquiry](references/pricing-inquiry.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON]

**Output Format:** [Markdown guidance with hcloud CLI commands, JSON snippets, and confirmation steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations require explicit confirmation; chargeable create or expansion operations require pricing inquiry before execution.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
