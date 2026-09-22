## Description:

Manages Huawei Cloud Flexus L instances by querying instance and traffic information, starting, stopping, rebooting servers, resetting passwords, and updating instance metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to operate Huawei Cloud Flexus L instances, including inventory lookup, lifecycle actions, password resets, metadata updates, and traffic package checks.

### Deployment Geography for Use:

Global, subject to Huawei Cloud service region availability

## Known Risks and Mitigations:

Risk: The skill can change Huawei Cloud Flexus L resources, including lifecycle state, passwords, and instance metadata.

Mitigation: Require explicit human confirmation before lifecycle, password, and update actions, and verify the target instance and region before execution.

Risk: Huawei Cloud credentials can grant access to cloud resources if mishandled.

Mitigation: Use least-privilege temporary credentials through environment variables and do not paste, log, print, or echo AK/SK/token values.

Risk: Some operational safeguards are documented in instructions rather than enforced by the scripts.

Mitigation: Review each intended operation before running scripts and keep IAM permissions limited to the required ECS and BSS actions.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud Flexus Application Server L Instance Documentation](https://support.huaweicloud.com/intl/zh-cn/flexusl_faq/faq_01_0003.html)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-ops)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline bash command examples and command output summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud resource status, traffic usage, and operation results; sensitive credentials should not be echoed.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
