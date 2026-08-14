## Description:

Analyzes Huawei Cloud CDN traffic anomalies by querying hcloud billing, domain, traffic, and bandwidth metrics and comparing recent usage against three-month baselines and absolute thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to investigate Huawei Cloud CDN traffic or bandwidth anomalies, validate domains, identify the active billing mode, and produce a read-only anomaly report with baseline and threshold comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the agent's existing hcloud configuration to read CDN domains, billing mode, and traffic statistics.

Mitigation: Use a Huawei Cloud sub-account with the documented read-only CDN permissions and avoid pasting AK/SK secrets into chat.

Risk: A user may request CDN write, delete, disable, or billing-mode changes while using the skill.

Mitigation: Keep execution limited to the disclosed read-only commands and direct configuration changes to the Huawei Cloud console or manual CLI use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-cdn-traffic-anomaly-analysis)
- [Huawei Cloud CLI Documentation](https://support.huaweicloud.com/hcloudcli/index.html)
- [IAM Permission Policies](references/iam-policies.md)
- [Related APIs](references/related-apis.md)
- [Task Query Metrics](references/task-query-metrics.md)
- [Task Threshold Judgment](references/task-threshold-judgment.md)
- [Verification Method](references/verification-method.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis report with inline hcloud and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only CDN analysis output; uses existing hcloud configuration and a local timestamp helper for UTC+8-aligned current and baseline windows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
