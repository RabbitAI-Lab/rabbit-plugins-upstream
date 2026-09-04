## Description:

Read-only diagnostics for Alibaba Cloud CDN traffic and bandwidth anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to investigate Alibaba Cloud CDN traffic spikes, bandwidth anomalies, bill surges, suspected hotlinking, and suspicious access patterns. It locates anomalous time windows from read-only usage data, analyzes offline access logs, and produces evidence-based remediation guidance without changing CDN configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses configured aliyun CLI credentials to read CDN usage metrics and offline access logs.

Mitigation: Use a RAM policy limited to sts:GetCallerIdentity and the documented CDN Describe actions.

Risk: Downloaded offline access logs may remain on disk when --keep-logs is used.

Mitigation: Avoid --keep-logs unless retention is required, and delete retained logs according to local data-handling policy.

Risk: Manual protection guidance can disrupt legitimate traffic if applied without business-scenario validation.

Mitigation: Review the report evidence and confirm the affected traffic pattern before applying Referer, URL authentication, IP, or User-Agent controls.

## Reference(s):

- [Anomaly Detection Flow](references/anomaly-detection-flow.md)
- [CDN Protection Capabilities](references/protection-capabilities.md)
- [RAM Policies](references/ram-policies.md)
- [Report Template](references/report-template.md)
- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cdn-traffic-anomaly)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report or JSON diagnostic document with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include usage baselines, anomalous windows, access-log forensics, rule hits, scenario classification, warnings, and manual-only recommendations.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
