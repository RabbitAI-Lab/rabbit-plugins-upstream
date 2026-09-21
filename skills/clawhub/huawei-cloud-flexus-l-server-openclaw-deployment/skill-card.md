## Description:

Creates a Huawei Cloud Flexus L Instance, deploys OpenClaw, and helps configure models and messaging channels for the deployed OpenClaw instance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to provision Huawei Cloud Flexus L instances, deploy OpenClaw, and configure model providers or messaging channels for enterprise AI assistant workflows.

### Deployment Geography for Use:

China Huawei Cloud regions supported by the skill documentation: cn-north-4, cn-east-3, cn-south-1, and cn-southwest-2.

## Known Risks and Mitigations:

Risk: The skill uses high-impact Huawei Cloud authority to create paid infrastructure and run COC operations.

Mitigation: Use temporary, least-privilege Huawei credentials and review the IAM policy before running deployment, model, or channel actions.

Risk: Non-interactive deployment may create prepaid, auto-paid, auto-renewing resources.

Mitigation: Use interactive confirmation until billing behavior is acceptable, and verify resource lifecycle settings in the Huawei Cloud console.

Risk: Logs and command output may expose cloud or integration secrets.

Mitigation: Pass credentials through environment variables, avoid placing AK/SK/token or channel secrets in conversation text, and redact logs before sharing.

Risk: Remote COC script execution can run with elevated impact on the target instance.

Mitigation: Review and pin the shipped scripts before execution, then monitor COC execution IDs and outputs for unexpected behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-openclaw-deployment)
- [Publisher profile](https://clawhub.ai/user/huaweicloudskill)
- [IAM Permission Policy Reference](artifact/references/iam-policies.md)
- [Skill Verification Method](artifact/references/verification-method.md)
- [Huawei Cloud Flexus L console](https://console.huaweicloud.com/smb/?/resource/list)
- [Huawei Cloud PyPI mirror](https://repo.huaweicloud.com/repository/pypi/simple)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples; command execution returns text and status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires uv, python3, Huawei Cloud credentials, and Huawei Cloud permissions for Flexus L instance and COC operations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
