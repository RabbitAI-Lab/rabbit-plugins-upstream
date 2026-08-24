## Description:

Huawei Cloud MRS cluster alarm diagnosis skill that analyzes user-provided alarm information, uses the LakeWatch API client and per-alarm knowledge base, and returns root cause, repair steps, and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operations engineers, SREs, and support teams use this skill to diagnose Huawei Cloud MRS alarm events when an alarm ID, alarm name, occurrence time, cluster ID, and node context are available. It guides read-only evidence collection through LakeWatch and produces a concise diagnosis report with repair suggestions that require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports overly broad authenticated MRS Manager proxy access.

Mitigation: Before installation, remove or restrict generic manager-access POST and wildcard proxy entries and allow only the read paths required for supported diagnosis flows.

Risk: The bundled LakeWatch configuration can disable TLS verification for intranet endpoints.

Mitigation: Enable TLS verification or configure a trusted CA certificate for production and trusted controlled environments.

Risk: The skill handles LakeWatch credentials and cached tokens.

Mitigation: Store only encrypted passwords, protect config/token/key files with owner-only permissions, and avoid exposing credentials or tokens in conversation or logs.

Risk: Alarm remediation guidance may include operational repair actions.

Mitigation: Keep diagnosis commands read-only and require explicit human approval before any repair command is run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-host-alarm-diagnose)
- [Acceptance Criteria - MRS Alarm Diagnosis](references/acceptance-criteria.md)
- [CLI Installation Guide - MRS Alarm Diagnosis](references/cli-installation-guide.md)
- [IAM Policies - MRS Alarm Diagnosis](references/iam-policies.md)
- [LakeWatch API Client](references/lakewatch-api-client.md)
- [Related Commands - MRS Alarm Diagnosis](references/related-commands.md)
- [Verification Method - MRS Alarm Diagnosis](references/verification-method.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown diagnosis report with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repair actions are presented as suggestions and require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
