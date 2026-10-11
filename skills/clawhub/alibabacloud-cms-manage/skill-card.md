## Description:

Helps agents use the Alibaba Cloud CLI to manage CloudMonitor monitoring, alerts, integrations, and onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to query and manage Alibaba Cloud monitoring resources, configure alerting, and onboard services to CloudMonitor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Onboarding steps may expose cluster credentials through a shared kubeconfig or long-lived temporary access.

Mitigation: Use a dedicated kubeconfig instead of the global ~/.kube/config and minimize temporary credential duration.

Risk: Agent installation commands may download software over HTTP or execute unverified installers.

Mitigation: Prefer HTTPS downloads and verify checksums or signatures before running installers.

Risk: Generated management commands can modify monitoring resources with the privileges of the active account.

Mitigation: Review commands before execution and use least-privilege Alibaba Cloud profiles.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/sdk-team/skills/alibabacloud-cms-manage)
- [Alibaba Cloud CLI installation](https://help.aliyun.com/document_detail/121541.html)
- [Alibaba Cloud CLI updates](https://help.aliyun.com/zh/cli/update-cli)
- [Monitoring integration guidance](references/integration-management.md)
- [Application monitoring guidance](references/apm.md)
- [Cluster onboarding guidance](references/cs-onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change Alibaba Cloud resources; review before execution.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
