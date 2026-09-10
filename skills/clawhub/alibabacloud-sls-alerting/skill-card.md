## Description:

Manage Alibaba Cloud SLS alerts and notifications. Use when configuring SLS alert rules, managing notification resources, or investigating alert events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to configure, inspect, update, and diagnose Alibaba Cloud SLS alert rules, notification resources, and alert events through Aliyun CLI workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an installer path that uses a remote shell script.

Mitigation: Avoid the curl-to-bash path unless the Aliyun CLI installer is independently trusted and verified; use platform binaries or managed installation where appropriate.

Risk: The skill can create, update, enable, disable, or delete live SLS alerting and notification configuration.

Mitigation: Confirm the intended project, region, resource namespace, and operation before writes; read back changes and compare the intended fields.

Risk: Using the skill may give the agent access to an existing Aliyun CLI authentication context.

Mitigation: Use least-privilege RAM permissions for the requested operation and keep credentials out of chat, environment dumps, and command output.

Risk: Notification users, webhooks, headers, secrets, and dynamic callback URLs can expose sensitive operational data.

Mitigation: Treat notification destinations and webhook configuration as sensitive, reuse approved resources where possible, and avoid printing secrets or personal identifiers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sdk-team/skills/alibabacloud-sls-alerting)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Manage Alert Rules](references/rules/manage-alert-rules.md)
- [Manage Alert Notifications](references/notifications/manage-notifications.md)
- [Alert Event Diagnosis](references/diagnosis/diagnose.md)
- [Region and Endpoint Configuration](references/regions.md)
- [RAM Policies - SLS Alerting](references/ram-policies.md)
- [Related APIs - SLS Alerting](references/related-apis.md)
- [Alibaba Cloud CLI Documentation](https://help.aliyun.com/zh/cli/)
- [Alibaba Cloud CLI Credential Configuration](https://help.aliyun.com/zh/cli/configure-credentials/)
- [SLS Alert Monitoring Rule Schema](https://help.aliyun.com/zh/sls/developer-reference/data-structure-of-an-alert-monitoring-rule)
- [SLS Alert Resource Data Schema](https://help.aliyun.com/zh/sls/developer-reference/data-structure-of-alert-resource-data)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Aliyun CLI commands and offline validation steps; cloud changes require configured authentication and user authorization.]

## Skill Version(s):

0.0.1 (source: server release metadata and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
