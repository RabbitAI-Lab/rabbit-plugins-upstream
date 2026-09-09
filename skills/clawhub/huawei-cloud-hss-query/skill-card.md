## Description:

Query and manage Huawei Cloud HSS (Host Security Service) for daily security inspection and incident response, including host assets, vulnerabilities, baselines, intrusion alerts, login audit logs, risk scoring, and confirmed alert-status updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators, cloud administrators, and incident responders use this skill to inspect Huawei Cloud HSS posture, investigate vulnerabilities or intrusion alerts, review login activity, and prepare confirmed alert-handling actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can update Huawei Cloud HSS alert or vulnerability handling status.

Mitigation: Use query-only IAM permissions for routine inspection, grant HSS write permissions only when status updates are intended, and confirm every ChangeEvent or ChangeVulStatus command before execution.

Risk: The included test script executes command strings from the package test JSON.

Mitigation: Run the test script only from a trusted, unmodified package and review test command definitions before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-hss-query)
- [hcloud CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies for HSS Skill](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [HSS Event Class ID Reference](references/hss-event-class-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with hcloud CLI commands and structured JSON risk summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON by default; mutating alert or vulnerability status commands require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
