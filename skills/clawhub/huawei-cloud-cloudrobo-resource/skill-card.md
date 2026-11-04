## Description:

Query CloudRobo quotas and resource pools, including workspace and Domain quotas, filtered pool listings, and node-level pool details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

CloudRobo users and platform engineers can inspect workspace and Domain compute quotas, filter resource pools, and review node capacity when planning training, evaluation, or inference workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installation guidance recommends disabling SSL certificate verification when SSL errors occur, which can expose requests to interception.

Mitigation: Keep certificate verification enabled and repair certificate errors before using real credentials.

Risk: The optional SDK test interpolates a supplied pool ID into Python source, so an untrusted value could be interpreted as code.

Mitigation: Use only trusted, validated UUIDs until the test passes pool IDs as data rather than source code.

Risk: The external dependency implementation was not bundled for review.

Mitigation: Review the dependency implementation separately before using it with real credentials.

## Reference(s):

- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [IAM Policies and Credential Guidance](artifact/references/iam-policies.md)
- [CloudRobo API Paths](artifact/references/api-paths.md)
- [Resource Configuration Catalog](artifact/references/resource-config-catalog.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with bash examples; CloudRobo query results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only quota and resource pool queries; requires CloudRobo credentials and workspace context.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
