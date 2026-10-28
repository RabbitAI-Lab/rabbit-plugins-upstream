## Description:

Lists Huawei Cloud CCE clusters in a region through KooCLI, with an SDK fallback and table, JSON, name-only, and client-side filtering options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to inspect CCE cluster inventory in a Huawei Cloud region, review cluster details, and filter results by name or ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented CLI wrapper reports telemetry, and the available evidence does not establish what it collects or where it sends the data.

Mitigation: Review the wrapper source, collected data, and reporting destination before use; set SKILL_QUALITY_REPORT=0 to use the documented reporting opt-out.

Risk: The SDK fallback directly reads cloud credentials despite contrary documentation, and the read-only guard has limits.

Mitigation: Review the fallback behavior, use list-only IAM permissions, and keep executable overrides unset.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-cce-list)
- [KooCLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM policy](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Markdown table, JSON array, or plain cluster-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports a region override and optional client-side name or ID filters; use JSON when all returned fields are needed.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
