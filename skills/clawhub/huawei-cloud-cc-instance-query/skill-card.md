## Description:

Queries Huawei Cloud Cloud Connect (CC) resources via hcloud CLI for cloud connections, bandwidth packages, inter-region bandwidths, network instances, cloud connection routes, and cross-account authorisations without performing write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and operators use this skill to inspect Huawei Cloud Cloud Connect topology and audit related bandwidth, routing, network instance, and cross-account authorisation state through read-only hcloud CLI queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can query Huawei Cloud Connect metadata through the configured hcloud profile, which may expose account topology in command output.

Mitigation: Use CC ReadOnlyAccess or equivalent least-privilege permissions and avoid sharing outputs that reveal account topology.

Risk: If domain_id is omitted or incorrect, queries may target the wrong account context.

Mitigation: Specify domain_id and region explicitly for each query and verify them before execution.

Risk: The setup flow downloads and runs a Huawei Cloud CLI installer script.

Mitigation: Verify the official installer source and review the script before running it in the target environment.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [API Reference](references/api-reference.md)
- [Huawei Cloud hcloud CLI Installer](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only hcloud CLI queries that return Huawei Cloud JSON or formatted CLI output.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
