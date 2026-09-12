## Description:

Query CloudRobo resource quotas and resource pools, including workspace and Domain-level quotas with CCE/ModelArts isolation, pool filtering, and pool details with node-level status and resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to inspect CloudRobo compute capacity before training, evaluation, and inference workloads. It helps agents produce read-only CLI and SDK guidance for quota checks, resource-pool filtering, and pool-detail lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed CloudRobo workflows can expose or misuse Huawei Cloud AK/SK credentials if configured broadly or stored in plaintext.

Mitigation: Use least-privilege AK/SK credentials, prefer environment-based secret handling, and avoid plaintext long-lived secrets where possible.

Risk: Disabling TLS verification can weaken credential and API traffic protection.

Mitigation: Keep TLS verification enabled for real credentials and restrict CLOUDROBO_VERIFY_SSL=false to controlled debugging only.

Risk: The bundled SDK test script runs with local credential-rich environments and caller-provided POOL_ID values.

Mitigation: Review the test script before execution, run it only in trusted environments, and avoid untrusted POOL_ID input.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cloudrobo-resource)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [API Paths](references/api-paths.md)
- [Resource Config Reference](references/resource-config-catalog.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash, PowerShell, JSON, YAML, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CloudRobo resource-query workflows; generated commands may require Huawei Cloud AK/SK credentials and workspace context.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
