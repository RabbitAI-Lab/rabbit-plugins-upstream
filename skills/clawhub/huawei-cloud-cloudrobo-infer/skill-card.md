## Description:

Manage CloudRobo inference services by deploying models, checking service status and logs, and starting, stopping, updating, or deleting services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ML platform operators use this skill to deploy CloudRobo models as inference services, monitor deployment state and logs, and manage service lifecycle operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled verification script can stop, alter, or delete an existing service without confirmation.

Mitigation: Avoid running it with SERVICE_ID set until a read-only version is available; test any required mutations only against a disposable service with explicit approval.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication and Access Control](references/iam-policies.md)
- [Service Configuration Catalog](references/service-config-catalog.md)
- [Verification Method](references/verification-method.md)
- [Validation Rules](references/validation-rules.md)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cloudrobo-infer)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes service status and log summaries when used with CloudRobo.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
