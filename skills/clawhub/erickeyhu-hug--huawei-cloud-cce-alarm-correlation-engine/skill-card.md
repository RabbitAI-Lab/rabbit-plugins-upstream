## Description: <br>
Huawei Cloud AOM alarm correlation and alarm-rule management skill for CCE operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to query Huawei Cloud AOM alarms, correlate active and historical CCE alarm streams, inspect cluster alarm health, and manage AOM alarm and notification rules through preview-and-confirm workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, disable, or delete Huawei Cloud AOM alarm and notification rules, which can affect monitoring coverage. <br>
Mitigation: Install it only for authorized Huawei Cloud operators, use least-privilege IAM permissions, and require preview review plus explicit confirmation before any mutation or cleanup action. <br>
Risk: Credential exposure is possible if users print, store, or pass AK/SK and tokens carelessly. <br>
Mitigation: Prefer a configured hcloud profile, avoid AK/SK environment fallback when possible, and do not expose credentials in commands, logs, files, or responses. <br>


## Reference(s): <br>
- [Workflow](references/workflow.md) <br>
- [Risk Rules](references/risk-rules.md) <br>
- [Output Schema](references/output-schema.md) <br>
- [Operation Guide](references/operation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [CCE Event List](references/cce-event-list.md) <br>
- [CCE Alarm Center Prometheus Metric Alarm Reference](references/cce-prometheus-metric-alarms.md) <br>
- [Huawei Cloud CCE Event Documentation](https://support.huaweicloud.com/usermanual-cce/cce_10_0902.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with dispatcher shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include alarm summaries, grouped alarm correlations, mutation previews, confirmation requirements, queried alarm resources, and follow-up risk items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
