## Description:

Lists Huawei Cloud public and private DNS zones and record sets in read-only mode, with table, JSON, or domain-name output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators can inventory Huawei Cloud DNS zones and record sets, inspect their details, or obtain names and JSON for follow-on work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted region value can send authenticated cloud requests to an unintended server.

Mitigation: Wait for a release that rejects unsupported regions and constrains executable overrides before providing credentials; use a dedicated account limited to DNS listing and keep credentials out of chat.

## Reference(s):

- [KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-Privilege IAM Policies](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text table, domain-name list, or JSON array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only DNS inventory; format is selected by the user.]

## Skill Version(s):

1.0.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
