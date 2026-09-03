## Description:

Diagnose abnormal Huawei Cloud CDN HTTP status codes by quantifying 4xx/5xx volume, localizing the affected code and time window, distinguishing edge-generated from origin-generated failures, and producing read-only troubleshooting evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, site reliability engineers, and CDN operators use this skill to investigate Huawei Cloud CDN 4xx/5xx spikes, separate edge-side from origin-side causes, inspect distribution and access-log evidence, and prepare a diagnosis report without changing CDN configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect CDN status, configuration, and log-download links for a selected domain and time window.

Mitigation: Use a read-only IAM user such as CDN Domain Viewer and confirm the domain, region, and time window before running queries or downloading logs.

Risk: Access keys, secret keys, and active CLI credentials could be exposed if pasted into chat or stored in source control.

Mitigation: Use the active hcloud profile or environment-based credential setup, and do not paste or echo AK/SK values in chat, logs, or files.

Risk: Changing CDN configuration during diagnosis could affect production traffic, cache state, access control, TLS, or billing.

Mitigation: Keep the workflow read-only and refuse create, update, delete, refresh, preheat, ownership-verification, billing, and statistics-configuration operations.

Risk: Downloaded access logs and extracted abnormal-status rows may include request paths, client IPs, user agents, and CDN edge IPs.

Mitigation: Limit log collection to the confirmed incident window, protect presigned log links and extracted JSON, and share only the evidence needed for diagnosis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cdn-abnormal-status-code-analysis)
- [Huawei Cloud hcloud CLI documentation](https://support.huaweicloud.com/hcloudcli/index.html)
- [Huawei Cloud CDN API reference](https://support.huaweicloud.com/api-cdn/cdn-api-pdf.pdf)
- [API and CLI command reference](references/related-apis.md)
- [IAM permission policies](references/iam-policies.md)
- [Prohibited operations](references/prohibited-operations.md)
- [Task discovery](references/task-discovery.md)
- [Task localize](references/task-localize.md)
- [Task root cause](references/task-rootcause.md)
- [Task forensics](references/task-forensics.md)
- [Task report](references/task-report.md)
- [Verification method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code]

**Output Format:** [Markdown diagnosis report with inline hcloud commands and JSON log-extraction results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; the helper script emits a single JSON object with rows, count, and error fields.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
