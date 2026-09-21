## Description:

Query Huawei Cloud OBS statistics including bucket capacity and object counts, extranet and intranet download traffic with month-over-month comparison, and total request counts with month-over-month comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to inspect Huawei Cloud OBS bucket usage and monitoring metrics, including storage capacity, traffic, and request trends, without performing write or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries cloud bucket metadata and monitoring metrics, so over-broad IAM credentials could expose more OBS information than needed.

Mitigation: Use a least-privilege read-only IAM user limited to OBS listing, OBS read metadata, and CES metric queries.

Risk: Huawei Cloud access keys could be exposed if pasted into chat or placed directly on command lines.

Mitigation: Use interactive credential setup or environment variables and do not ask users to provide AK/SK values in conversation.

Risk: CLI installation steps depend on downloaded hcloud and obsutil binaries and may involve elevated permissions.

Mitigation: Verify hcloud and obsutil download sources before installation and before any sudo-based setup.

Risk: Requests outside the documented read-only statistics workflows could lead to destructive OBS operations.

Mitigation: Refuse delete, batch delete, empty bucket, and object removal requests; keep the skill limited to bucket listing and metric queries.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [OBS CES Monitoring Metrics Reference](references/obs-metrics.md)
- [Related APIs](references/related-apis.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting](references/troubleshooting.md)
- [Huawei Cloud OBS Monitoring Metrics](https://support.huaweicloud.com/usermanual-obs/obs_03_0010.html)
- [Huawei Cloud CES ShowMetricData API](https://support.huaweicloud.com/api-ces/ces_03_0059.html)
- [Huawei Cloud OBS API Reference](https://support.huaweicloud.com/api-obs/obs_04_0001.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and tabular CLI/script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided region, bucket name, time range, and configured Huawei Cloud CLI credentials.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
