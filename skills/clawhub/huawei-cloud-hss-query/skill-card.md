## Description:

Query and manage Huawei Cloud HSS (Host Security Service) for daily security inspection and incident response, covering host assets, vulnerabilities, security baselines, intrusion alerts, login audit logs, risk scoring, and alert handling status updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, cloud administrators, and incident responders use this skill to inspect Huawei Cloud HSS posture, review vulnerabilities and baselines, investigate intrusion and login events, and update alert or vulnerability handling status when explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Huawei Cloud HSS alert or vulnerability handling status through ChangeEvent or ChangeVulStatus.

Mitigation: Use query-only IAM permissions for routine inspections, grant write permissions only when status changes are required, and require explicit per-action confirmation before ignore, whitelist, repair, verify, or similar operations.

Risk: Huawei Cloud AK/SK credentials and the hcloud local configuration are sensitive.

Mitigation: Do not provide AK/SK secrets to the agent; configure hcloud directly in the user's terminal and treat ~/.hcloud as confidential.

Risk: Overbroad HSS permissions increase the impact of accidental alert or vulnerability state changes.

Mitigation: Prefer the documented least-privilege query policy and scope permissions to the target project or enterprise project whenever possible.

## Reference(s):

- [hcloud CLI installation and authentication](references/cli-installation-guide.md)
- [Least-privilege IAM policies for HSS](references/iam-policies.md)
- [Verification and testing methods](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [HSS event class ID reference](references/hss-event-class-reference.md)
- [hcloud CLI installer](https://cn-north-4-hdn-koocli.obs.cn-north-4.myhuaweicloud.com/cli/latest/hcloud_install.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and structured JSON risk summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-only query commands, confirmation-gated alert or vulnerability status update commands, and concise incident-response recommendations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
