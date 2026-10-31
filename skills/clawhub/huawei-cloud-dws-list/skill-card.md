## Description:

Lists Huawei Cloud DWS clusters in a tenant region, with filtering, pagination, and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to inspect Huawei Cloud DWS cluster inventory for a selected tenant region, including cluster status, configuration, and connection details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment overrides may bypass the read-only guard.

Mitigation: Remove production executable overrides or tightly control the launch environment.

Risk: The setup guide runs a downloaded KooCLI installer without verification.

Mitigation: Install KooCLI using verified vendor instructions and validate the installer source before execution.

Risk: The SDK fallback reads credentials from environment variables.

Mitigation: Use dedicated credentials limited to DWS listing and keep secrets out of chat, logs, and shared environments.

Risk: Cluster output can expose addresses and configuration.

Mitigation: Review and redact inventory output before sharing or storing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dws-list)
- [KooCLI Installation & Credential Guide](references/cli-installation-guide.md)
- [Least Privilege IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Full-field cluster table, JSON array, or cluster-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-scoped cluster inventory; supports client-side filters and pagination.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
