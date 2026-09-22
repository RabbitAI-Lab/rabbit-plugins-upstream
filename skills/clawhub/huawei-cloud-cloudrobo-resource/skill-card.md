## Description:

Query Huawei Cloud CloudRobo resource quotas and resource pools to inspect CCE and ModelArts capacity, filtering, pagination, and pool details for training, evaluation, and inference workloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to inspect CloudRobo compute quotas and resource pool availability before launching training, evaluation, or inference workloads. It supports read-only CLI and SDK workflows for quota lists, filtered pool lists, and pool detail inspection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Huawei Cloud AK/SK credentials for CloudRobo CLI and SDK access.

Mitigation: Use least-privilege credentials, prefer environment variables over plaintext config files, and rotate long-lived credentials according to the account security policy.

Risk: The security evidence flags unsafe SSL-verification guidance as a weakness.

Mitigation: Keep SSL verification enabled for normal use and only disable it in tightly controlled debugging environments.

Risk: Traffic logging can expose sensitive request or response details during debugging.

Mitigation: Keep traffic logging disabled in production and review logs for sensitive data before sharing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-resource)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [API Paths](references/api-paths.md)
- [Resource Config Reference](references/resource-config-catalog.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline bash, PowerShell, JSON, YAML, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CloudRobo CLI and SDK workflows that return JSON responses from quota and resource pool queries.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
