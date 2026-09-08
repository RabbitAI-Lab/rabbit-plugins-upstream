## Description:

Query Huawei Cloud VPCEP (VPC Endpoint) names by keyword and list VPC endpoints across a region for read-only inspection and resource management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to list Huawei Cloud VPCEP endpoints, find endpoints by fuzzy name keyword, and summarize endpoint status, VPC, IP, and creation time during inventory or daily inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud credentials may be exposed through shared shells, logs, or local configuration while using the CLI or SDK.

Mitigation: Use least-privilege VPCEP read-only credentials, keep secrets out of shared terminals and logs, and rely on environment variables or approved local credential storage.

Risk: CLI installation introduces supply-chain risk if the downloaded hcloud binary is not the expected Huawei Cloud package.

Mitigation: Install from the documented Huawei Cloud source and verify the source or checksum where possible before use.

Risk: Fuzzy name filters can return broader or unexpected endpoint results during security inventory.

Mitigation: Confirm filtered results against expected endpoint names, IDs, VPCs, and statuses before acting on the inventory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-vpcep-name-list)
- [Publisher profile](https://clawhub.ai/user/erickeyhu-hug)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Linux amd64 download](https://hwcloudcli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_cli_linux_amd64.tar.gz)
- [Huawei Cloud KooCLI macOS amd64 download](https://hwcloudcli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_cli_mac_amd64.tar.gz)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash commands, JSON examples, and optional Python SDK code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only VPCEP query guidance; results may include endpoint names, IDs, status, VPC IDs, endpoint IPs, creation times, and total counts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
