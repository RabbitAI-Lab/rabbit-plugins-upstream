## Description:

Analyzes Huawei Cloud CDN domain traffic anomalies with hcloud CLI by detecting billing mode, querying traffic or bandwidth metrics, and comparing current usage against a three-month baseline and absolute thresholds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to investigate Huawei Cloud CDN domains for traffic theft, abnormal bandwidth spikes, and deviations from historical traffic baselines using read-only account queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Huawei Cloud credentials could be exposed if users paste AK/SK secrets into chat or screenshots.

Mitigation: Configure hcloud outside the conversation, use environment variables or the local CLI config, and avoid printing or sharing credential values.

Risk: Overbroad IAM permissions could allow actions beyond the skill's read-only analysis purpose.

Mitigation: Use a least-privilege IAM user limited to CDN domain, statistics, and billing read permissions.

Risk: Incorrect region, service area, or UTC+8 timestamp assumptions could produce misleading anomaly conclusions.

Mitigation: Confirm the CDN account assumptions before relying on the report, and use the bundled timestamp workflow for midnight-aligned query windows.

Risk: Write, delete, or billing-mode changes could affect production traffic or cost.

Mitigation: Keep the workflow read-only and refuse modification requests; perform any configuration changes manually through approved Huawei Cloud channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cdn-traffic-anomaly-analysis)
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/hcloudcli/index.html)
- [CLI installation guide](references/cli-installation-guide.md)
- [IAM permission policies](references/iam-policies.md)
- [API and CLI command reference](references/related-apis.md)
- [Traffic and bandwidth metric queries](references/task-query-metrics.md)
- [Threshold judgment](references/task-threshold-judgment.md)
- [Verification method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown analysis report with inline shell commands and tabular metric summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes billing mode, baseline statistics, current-window values, threshold comparison, and a Normal, Watch, or Anomalous conclusion.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
