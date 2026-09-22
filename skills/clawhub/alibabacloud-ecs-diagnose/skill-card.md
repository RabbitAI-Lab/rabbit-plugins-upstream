## Description:

Comprehensive Alibaba Cloud ECS instance diagnostics skill that performs systematic troubleshooting for cloud platform status, connectivity, performance, disk, and GuestOS issues via Aliyun CLI, Cloud Monitor, Cloud Assistant, and optional EBS diagnosis APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to diagnose Alibaba Cloud ECS instances that are unreachable, slow, out of disk space, reporting high CPU or memory usage, affected by system events, or experiencing disk IO performance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer and plugin-update steps can execute or install code from external Alibaba Cloud distribution paths.

Mitigation: Review and independently trust the installer and plugin sources before use; prefer documented package-manager or manual installation paths when available.

Risk: Deep diagnostics can run commands inside cloud servers through Cloud Assistant.

Mitigation: Require explicit approval before executing Cloud Assistant commands, review the exact commands first, and use a least-privilege Alibaba Cloud identity.

Risk: Alibaba Cloud AccessKey secrets may be exposed if entered or printed in command lines or chat.

Mitigation: Use existing credential profiles, environment configuration, STS, OAuth, or RAM roles; do not paste, echo, or place AccessKey secrets in examples.

## Reference(s):

- [Aliyun CLI Installation & Configuration Guide](references/cli-installation-guide.md)
- [Related CLI Commands](references/related-commands.md)
- [RAM Policies for ECS Diagnostics Skill](references/ram-policies.md)
- [Verification Methods for ECS Diagnostics](references/verification-method.md)
- [Alibaba Cloud ECS Remote Connection / Service Access Diagnostic Guide](references/remote-connection-diagnose-design.md)
- [Alibaba Cloud ECS Disk Performance / IO Bottleneck Diagnostic Guide](references/ebs-disk-performance-diagnose-design.md)
- [EBS Performance Diagnosis Events Reference](references/ebs-diagnosis-events.md)
- [Acceptance Criteria: alibabacloud-ecs-diagnose](references/acceptance-criteria.md)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-ecs-diagnose)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown, code, configuration]

**Output Format:** [Markdown diagnostic guidance with Aliyun CLI commands, optional Python fallback instructions, and structured findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-confirmed Alibaba Cloud region and instance or disk identifiers; Cloud Assistant commands and cloud API calls require appropriate RAM permissions.]

## Skill Version(s):

0.0.4 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
