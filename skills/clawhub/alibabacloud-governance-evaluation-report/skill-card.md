## Description:

Alibaba Cloud Governance Center evaluation report skill for querying governance maturity check results, generating structured risk reports, and account compliance analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud governance, security, and platform teams use this skill to inspect Alibaba Cloud Governance Center maturity results, identify high-priority risks, and produce concise remediation-oriented reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses local Aliyun CLI credentials to query Alibaba Cloud Governance Center.

Mitigation: Use a least-privilege read-only RAM profile, confirm which profile or environment credentials will be used, and run it only for intended governance reporting.

Risk: Setup guidance can persistently change Aliyun CLI plugin behavior through plugin updates and automatic plugin installation.

Mitigation: Review plugin update and auto-plugin-install settings before enabling them, and prefer verified package-manager or checksum-verified CLI installation paths.

Risk: Governance findings can include sensitive resource identifiers and account compliance details.

Mitigation: Keep generated reports in the chat unless explicitly needed elsewhere, and share results only with authorized cloud governance or security stakeholders.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-governance-evaluation-report)
- [Aliyun CLI Releases](https://github.com/aliyun/aliyun-cli/releases)
- [Cloud Governance Center Documentation](https://help.aliyun.com/zh/governance/)
- [Governance API Reference](https://help.aliyun.com/zh/governance/developer-reference/api-governance-2021-01-20-overview)
- [Report Format: Overall Overview](references/report-format-overview.md)
- [Report Format: Pillar or Keyword Analysis](references/report-format-pillar.md)
- [Report Format: Individual Check-Item Analysis](references/report-format-detail.md)
- [RAM Policies](references/ram-policies.md)
- [Verification Methods](references/verification-method.md)
- [Aliyun CLI Installation & Configuration Guide](references/cli-installation-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline shell commands and structured JSON-derived findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are returned in conversation; the helper script queries read-only Governance Center APIs and caches metadata locally.]

## Skill Version(s):

0.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
