## Description:

Provides Huawei Cloud Elastic IP cost optimization workflows using hcloud CLI to list EIPs, identify idle resources, generate reports, configure monitoring alerts, and maintain audit logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to analyze Huawei Cloud EIP inventory, estimate avoidable idle-IP costs, generate text, HTML, or JSON reports, and set up monitoring alerts without releasing or deleting resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation includes broad cloud-management policy examples even though the normal workflow is read-only analysis.

Mitigation: Use the minimal read-only IAM policy for EIP list and detail access, and avoid full-management permissions unless separately reviewed and approved.

Risk: Credential handling can expose Huawei Cloud AK/SK values if users place secrets in shell history, command-line arguments, logs, or conversations.

Mitigation: Prefer hcloud interactive configuration or managed temporary credentials, never pass AK/SK values as command-line arguments, and rotate credentials regularly.

Risk: Optional monitoring can create local cron jobs and send outbound webhook or email alerts.

Mitigation: Review cron entries and alert destinations before enabling monitoring, and remove scheduled jobs when monitoring is no longer required.

Risk: Cost estimates can be inaccurate because the API evidence states billing mode is unavailable and estimates use a bandwidth-based model.

Mitigation: Treat generated savings figures as advisory and confirm current region-specific pricing and billing mode before taking business action.

## Reference(s):

- [IAM Permission Policies](references/iam-policies.md)
- [EIP API Reference Guide](references/eip-api-guide.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)
- [Huawei Cloud CLI Reference](https://support.huaweicloud.com/cli/reference.html)
- [Huawei Cloud IAM User Guide](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus text, HTML, and JSON report outputs from bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include EIP status summaries, idle analysis, estimated CNY costs, alert setup guidance, and audit log exports.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
