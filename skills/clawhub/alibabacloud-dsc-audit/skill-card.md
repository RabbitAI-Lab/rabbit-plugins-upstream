## Description:

Queries Alibaba Cloud Data Security Center risk events and supports manual handling of a user-confirmed risk event.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Security and cloud operations teams use this skill to inspect Alibaba Cloud Data Security Center risk events and record manual handling decisions after confirming the exact RiskId and audit text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live handling persistently marks an Alibaba Cloud DSC alert as processed.

Mitigation: Run live handling only after verifying the exact RiskId and HandleDetail text; use dry-run rehearsal when validation is needed without changing alert state.

Risk: Overbroad Alibaba Cloud RAM permissions can allow handling actions when only visibility is needed.

Mitigation: Grant least-privilege RAM permissions and use query-only permissions for read-only workflows.

Risk: Long-lived AccessKeys increase credential exposure risk in cloud administration workflows.

Mitigation: Prefer STS or role-based credentials and avoid reading, echoing, or entering AccessKey values in the agent session.

## Reference(s):

- [Alibaba Cloud Python SDK Generic Invocation Documentation](https://help.aliyun.com/zh/sdk/developer-reference/generalized-call-python)
- [Alibaba Cloud DSC Audit on ClawHub](https://clawhub.ai/sdk-team/skills/alibabacloud-dsc-audit)
- [Data Security Center API Reference](references/related-apis.md)
- [Data Security Center RAM Permission Configuration](references/ram-policies.md)
- [Aliyun CLI Installation Guide](references/cli-installation-guide.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and script output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled Python scripts for paginated query and gated manual handling workflows.]

## Skill Version(s):

0.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
