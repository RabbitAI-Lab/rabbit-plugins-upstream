## Description:

Queries Huawei Cloud Cloud Connect (CC) Global Connection Bandwidth (GCB) resources via hcloud CLI, including single-resource details, filtered lists, tenant configuration, and bind-eligible bandwidths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud CC Global Connection Bandwidth resources, review tenant GCB configuration and quotas, and find bandwidths eligible for binding to CC, GEIP, GCN, or GSN services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud credentials may be exposed if AK/SK values are hardcoded or shared in logs.

Mitigation: Configure hcloud with a secure profile or prompted environment variables, and avoid storing AK/SK values in scripts or shared transcripts.

Risk: Cloud network inventory, quotas, and bound-instance details may be sensitive even though the skill is query-only.

Mitigation: Use a least-privilege identity with CC ReadOnlyAccess or equivalent and share command output only with authorized users.

Risk: Installing or configuring hcloud changes the local execution environment.

Mitigation: Review the Huawei Cloud installer and credential-profile setup before running them, and prefer the official hcloud installation guide.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cc-gcb-query)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM Policies](references/iam-policies.md)
- [API Reference](references/api-reference.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Data Flow Diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with hcloud CLI commands and expected JSON response fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud CC GCB queries require hcloud authentication, a region, a domain_id, and operation-specific IDs or filters.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
