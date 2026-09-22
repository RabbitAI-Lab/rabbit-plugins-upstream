## Description:

Diagnoses abnormal Huawei Cloud CDN HTTP 4xx/5xx status codes with read-only hcloud CLI queries, edge-versus-origin status statistics, top-N distribution checks, and per-request log forensics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and CDN operators use this skill to investigate 4xx/5xx spikes on Huawei Cloud CDN domains, determine whether errors are edge-generated or origin-returned, and assemble a concise diagnosis report with remediation boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CDN access logs and presigned log links can contain client IPs, URLs, user agents, and traffic details.

Mitigation: Treat log links and downloaded log output as sensitive, limit sharing, and retain only the rows needed for the incident analysis.

Risk: Using a broad cloud credential profile can expose more CDN account information than the diagnosis needs.

Mitigation: Run the workflow with a least-privilege Huawei Cloud CDN read-only profile such as CDN Domain Viewer or equivalent read-only query permissions.

Risk: CDN configuration changes, refreshes, preheats, or deletes can affect production traffic if performed outside the skill's read-only boundary.

Mitigation: Keep the agent workflow limited to documented GET/read-only operations and route any configuration change to the Huawei Cloud console or a separately reviewed manual command.

Risk: Abnormal status-code root cause can be misattributed if edge and back-to-origin status statistics are not checked separately.

Mitigation: Validate edge status statistics, back-to-source status statistics, top-N distribution, and representative log rows before acting on remediation guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cdn-abnormal-status-code-analysis)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Prohibited Operations](references/prohibited-operations.md)
- [API and CLI Command Reference](references/related-apis.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud CLI Documentation](https://support.huaweicloud.com/hcloudcli/index.html)
- [Huawei Cloud CDN API Reference](https://support.huaweicloud.com/api-cdn/cdn-api-pdf.pdf)
- [Huawei Cloud CDN Log Format Reference](https://support.huaweicloud.com/intl/zh-cn/bestpractice-cdn/cdn_01_0252.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown diagnosis guidance with hcloud CLI command blocks and JSON log-forensics output from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflow; generated findings should be reviewed before operational remediation.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
