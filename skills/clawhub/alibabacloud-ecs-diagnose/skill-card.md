## Description:

Comprehensive Alibaba Cloud ECS instance diagnostics skill that performs cloud platform status checks and optional GuestOS diagnostics through Cloud Assistant for connectivity, performance, disk, network, and instance-status issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to diagnose standard Alibaba Cloud ECS instances and disks when users report connectivity failures, SSH timeouts, degraded performance, disk space or disk I/O issues, abnormal status, or system event alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or update mutable Aliyun CLI plugins and optional Python SDK dependencies.

Mitigation: Review the CLI installation path and dependency setup before use; require controlled plugin and dependency approval in sensitive environments.

Risk: Deep diagnostics can run commands inside cloud instances through Cloud Assistant.

Mitigation: Require explicit approval before Cloud Assistant execution and use a least-privilege RAM role with only the permissions needed for the selected diagnostic workflow.

Risk: Alibaba Cloud credentials are required for cloud API calls.

Mitigation: Configure credentials outside the agent session, avoid command-line secrets, and never print or request access key values in conversation.

Risk: The artifact includes high-impact remediation examples for cloud infrastructure changes.

Mitigation: Treat remediation commands as manual recommendations and require user approval before any infrastructure-changing action is run.

## Reference(s):

- [Acceptance Criteria: alibabacloud-ecs-diagnose](references/acceptance-criteria.md)
- [Aliyun CLI Installation & Configuration Guide](references/cli-installation-guide.md)
- [EBS Performance Diagnosis Events Reference](references/ebs-diagnosis-events.md)
- [Alibaba Cloud ECS Disk Performance / IO Bottleneck Diagnostic Guide](references/ebs-disk-performance-diagnose-design.md)
- [RAM Policies for ECS Diagnostics Skill](references/ram-policies.md)
- [Related CLI Commands](references/related-commands.md)
- [Alibaba Cloud ECS Remote Connection / Service Access Diagnostic Guide](references/remote-connection-diagnose-design.md)
- [Verification Methods for ECS Diagnostics](references/verification-method.md)
- [Aliyun CLI Plugin Mode](https://www.alibabacloud.com/help/cli/user-guide/use-alibaba-cloud-cli-in-plugin-mode)
- [ECS API Reference](https://www.alibabacloud.com/help/ecs/developer-reference/api-overview)
- [Cloud Assistant Documentation](https://www.alibabacloud.com/help/ecs/user-guide/cloud-assistant-overview)
- [Cloud Monitor ECS Metrics](https://www.alibabacloud.com/help/cms/developer-reference/metrics-of-ecs)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, API calls, Guidance]

**Output Format:** [Markdown diagnostic report with inline shell commands and JSON excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires confirmed Alibaba Cloud region and ECS instance or disk identifiers; deep diagnostics may run Cloud Assistant commands after approval.]

## Skill Version(s):

0.0.4 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
