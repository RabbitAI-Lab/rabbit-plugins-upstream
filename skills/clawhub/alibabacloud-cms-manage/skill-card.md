## Description:

Guides agents through Alibaba CloudMonitor (CMS) aliyun cms2 operations for observability onboarding, integrations, APM, RUM, Prometheus, alerting, events, metrics, and dashboard workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to plan and execute Alibaba Cloud CMS observability tasks through the aliyun cms2 CLI, including onboarding resources, managing integrations, querying metrics, and configuring alerts. It is intended for guided operational work where cloud-side and Kubernetes changes are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide persistent Alibaba Cloud or Kubernetes changes.

Mitigation: Use a least-privilege aliyun profile and require human review of the exact command, target resources, expected impact, and risks before any write is executed.

Risk: LicenseKey/authToken values and generated plans or reports may contain sensitive operational data.

Mitigation: Treat credentials, generated plans, and reports as sensitive; avoid logging, sharing, or committing them unless they have been reviewed and sanitized.

Risk: Installer guidance can be risky when it relies on direct shell execution from remote URLs.

Mitigation: Avoid direct curl-to-bash installers; prefer official documentation, explicit commands, and reviewable installation steps.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cms-manage)
- [Alibaba Cloud CLI Installation](https://help.aliyun.com/document_detail/121541.html)
- [Alibaba Cloud CLI Update Guide](https://help.aliyun.com/zh/cli/update-cli)
- [Integration Common Rules](references/integration-common.md)
- [Integration Management](references/integration-management.md)
- [Prometheus Management](references/prometheus-management.md)
- [Alerting Module](references/alerting.md)
- [Application Monitoring (APM) Module](references/apm.md)
- [Real User Monitoring (RUM) Module](references/rum.md)
- [AI Observability Module](references/ai.md)
- [RAM Policy Reference](references/ram-policies.md)
- [Related APIs](assets/related_apis.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON/YAML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires aliyun CLI 3.3.15 or newer with the cms2 command available; generated commands may operate on Alibaba Cloud and Kubernetes resources.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
