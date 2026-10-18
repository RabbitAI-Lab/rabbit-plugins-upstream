## Description:

Queries and analyzes Huawei Cloud CCE workload, application, audit, and control-plane logs and supports confirmed changes to log-collection rules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate CCE application, Pod, audit, and control-plane logs and, after explicit confirmation, manage CCE and LTS log-collection rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collection-rule changes can alter which CCE and LTS logs are captured.

Mitigation: Review the exact rule scope and destination in a preview and obtain explicit confirmation before creating or deleting a rule.

Risk: Broad cloud credentials can grant access to sensitive logs and collection settings.

Mitigation: Use least-privilege, temporary credentials restricted to the intended cluster and log resources.

Risk: Automatic quality reporting may transmit information derived from inputs and outputs.

Mitigation: Disable quality reporting when logs may contain sensitive data, and redact secrets and personal information from summaries.

Risk: The kubectl-cce integration hardcodes insecure TLS behavior.

Mitigation: Fix or isolate this security exception before production use; verify installer scripts before running them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cce-log-analyzer)
- [CCE Cloud Native Logging documentation](https://support.huaweicloud.com/usermanual-cce/cce_10_0416.html)
- [Skill workflow](artifact/references/workflow.md)
- [Output schema](artifact/references/output-schema.md)
- [IAM policies](artifact/references/iam-policies.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Configuration]

**Output Format:** [JSON tool results and human-readable log-analysis summaries or rule-change previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify the source, target, time window, findings, and query limits; rule changes require preview and confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release; bundled skill frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
