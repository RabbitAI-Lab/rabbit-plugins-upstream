## Description:

Lists a Huawei Cloud tenant’s CDN accelerated domains with filters and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operations engineers use this skill to inventory accelerated domains and review their names, status, CNAMEs, and business types. It supports read-only CDN checks through Huawei Cloud credentials configured outside chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes certificate-bypass options, and package integrity should be reviewed.

Mitigation: Use verified packages from Huawei’s official downloads with published checksums in an isolated environment.

Risk: The read-only assurance warrants review before use.

Mitigation: Use dedicated read-only CDN credentials and keep executable overrides unset or administrator-controlled.

## Reference(s):

- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud CDN list verification and API details](artifact/references/verification-method.md)
- [Least-privilege CDN IAM policy](artifact/references/iam-policies.md)
- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-cdn-list)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Full-field table, raw JSON array, or accelerated-domain names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated results with optional server-side filters]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
