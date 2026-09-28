## Description:

Analyzes Huawei Cloud WAF security event logs to identify attack patterns, affected assets, source trends, and protection rule recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Security engineers and cloud operators use this skill to query Huawei Cloud WAF events, summarize attack activity across multiple dimensions, and prepare prioritized WAF rule recommendations for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan marks the release suspicious because it can lead users toward high-impact WAF configuration changes and broad permissions.

Mitigation: Use the read-only IAM policy by default, review every generated command as a draft, and grant write-capable WAF permissions only when changes are intentionally being prepared.

Risk: Event-derived values can make generated commands unsafe or misleading if pasted directly into a shell.

Mitigation: Rebuild or safely quote values from WAF events before execution, validate business impact, and confirm rollback steps.

Risk: Personal or administrator Huawei Cloud credentials increase blast radius if commands are misused.

Mitigation: Use dedicated least-privilege Huawei Cloud credentials for analysis and separate elevated credentials only for approved production changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-waf-log-analysis)
- [IAM Policies for WAF Log Analysis](references/iam-policies.md)
- [hcloud CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Rule Recommendation Guide](references/rule-recommendation-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline hcloud and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-only analysis results and draft WAF rule commands for user review; it should not execute production changes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
