## Description:

Entry skill for the aliyun CLI distribution of CloudMonitor (CMS), covering CMS module operations such as Integration Policy/Center, APM, RUM, Prometheus Service, recording rules, alerting, alert history, event hub, PromQL, cloud resources, service observability, onboarding, and metric queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and cloud operations teams use this skill to plan and run Alibaba Cloud CMS observability tasks through aliyun cms2, including onboarding resources, querying metrics, managing alerts, and generating configuration or execution guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful Alibaba Cloud CMS operations that may create, update, delete, start, or stop cloud resources.

Mitigation: Use a least-privilege Alibaba Cloud profile and require explicit confirmation before any cloud-side write or high-impact create.

Risk: Upgrade commands, remote installers, kubeconfig writes, cluster changes, and file report generation may affect the local environment or connected infrastructure.

Mitigation: Review exact commands before execution and limit local and cluster permissions to the task being performed.

Risk: Tag mutation permissions can broaden the operational impact of onboarding and management workflows.

Mitigation: Avoid granting tag mutation unless the workflow specifically requires it.

Risk: APM and RUM onboarding can expose tokens or endpoints in command output, configuration snippets, or generated files.

Mitigation: Treat APM and RUM tokens as secrets and do not print, log, or commit them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-cms-manage)
- [Alibaba Cloud CLI Installation](https://help.aliyun.com/document_detail/121541.html)
- [Alibaba Cloud CLI Update Guide](https://help.aliyun.com/zh/cli/update-cli)
- [AI Observability Module](references/ai.md)
- [Alerting Module](references/alerting.md)
- [Application Monitoring (APM) Module](references/apm.md)
- [APM Metric Catalog](references/apm-metrics.md)
- [Batch Onboarding of Cloud Service Metrics](references/batch-onboarding-workflow.md)
- [Cloud Service Onboarding](references/cloud-onboarding.md)
- [Container (CS) Onboarding](references/cs-onboarding.md)
- [ECS Host Onboarding](references/ecs-onboarding.md)
- [Event Hub Module](references/event-hub.md)
- [Grafana Dashboard Rules](references/grafana-dashboard-rules.md)
- [Integration Common Rules](references/integration-common.md)
- [Integration Policy Diagnosis](references/integration-diagnosis.md)
- [Prometheus Management](references/prometheus-management.md)
- [RAM Policy Reference](references/ram-policies.md)
- [Real User Monitoring (RUM) Module](references/rum.md)
- [UModel Metric Catalog (K8s Pod)](references/umodel-metrics.md)
- [Related Alibaba Cloud CMS APIs](assets/related_apis.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON bodies, configuration snippets, and optional report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation for cloud-side writes and high-impact local actions; APM and RUM tokens should be treated as secrets.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
