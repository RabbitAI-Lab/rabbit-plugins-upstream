## Description:

Manage Huawei Cloud ModelArts Notebook instances through full lifecycle operations via the hcloud CLI across instance, lease, tag, image, flavor, cluster, feature, and dynamic storage workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect and manage Huawei Cloud ModelArts Notebook instances, including lifecycle actions, image operations, storage attachment, lease renewal, tag management, and flavor or cluster queries. It is intended for users who already have hcloud CLI access to the target Huawei Cloud account and region.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide create, start, delete, storage, image, and lease operations that may modify cloud resources, remove assets, or incur charges.

Mitigation: Use least-privilege IAM permissions, review proposed commands, require explicit user confirmation for write operations, and check pricing before chargeable create or start actions.

Risk: Credential setup guidance may expose AK/SK secrets if copied into chat, scripts, process arguments, or unsafe install flows.

Mitigation: Do not paste AK/SK values into the agent session, do not read credential files, avoid curl-to-bash installation, and configure credentials outside the agent session using the provider's documented tooling.

## Reference(s):

- [CLI Command Examples](references/cli-command-examples.md)
- [IAM Policies](references/iam-policies.md)
- [Known Issues and Practical Solutions](references/known-issues.md)
- [BSS On-Demand Pricing Inquiry](references/pricing-inquiry.md)
- [Verification Method](references/verification-method.md)
- [API Paths](references/api-paths.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud hcloud CLI Documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud ModelArts API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/ModelArts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and occasional JSON or Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill may propose or run hcloud CLI commands after checking credentials, region, pricing for chargeable actions, and user confirmation for write operations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
