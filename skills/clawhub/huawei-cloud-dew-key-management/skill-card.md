## Description:

Use when managing secrets, credentials, encryption keys, certificates, or sensitive data on Huawei Cloud DEW through CSMS and KMS metadata workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud engineers, and security operators use this skill to list and diagnose Huawei Cloud CSMS secrets and KMS keys, audit key usage, and perform gated key or rotation management while keeping secret values out of the agent context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide cloud operations that require broad CSMS, KMS, and CTS permissions.

Mitigation: Use a dedicated least-privilege Huawei Cloud principal, restrict allowed regions and resources, and test write actions in a sandbox before production use.

Risk: Automatic quality reporting may send execution metadata to the configured reporting endpoint.

Mitigation: Disable quality reporting unless explicitly required and do not override SKILL_QUALITY_ENDPOINT to an untrusted host.

Risk: Write, rotation, deletion, and metadata audit actions can affect sensitive cloud resources.

Mitigation: Require explicit user confirmation for metadata audits and all write or delete actions, and preserve the irreversible KMS deletion warning before scheduling deletion.

Risk: Secret values or cloud credentials could be exposed if blocked operations or unsafe output patterns are bypassed.

Mitigation: Keep secret-value reads blocked, use runtime injection for secret consumption, and never echo AK/SK credentials, passwords, tokens, or secret values.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [hcloud CLI Installation and Authentication Guide](references/cli-installation-guide.md)
- [CSMS Usage Guide](references/csms-usage.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [IAM Policies](references/iam-policies.md)
- [KMS Usage Guide](references/kms-usage.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud DEW Documentation](https://support.huaweicloud.com/dew/)
- [Huawei Cloud DEW API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/DEW/doc)
- [Huawei Cloud KooCLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, Code]

**Output Format:** [Markdown with inline shell commands, JSON summaries, tables, and short code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs must summarize metadata only and must not include secret values, AK/SK credentials, passwords, or tokens.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
