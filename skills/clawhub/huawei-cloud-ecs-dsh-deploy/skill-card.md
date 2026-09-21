## Description:

Huawei Cloud Flexus X Instance Deployment - DeepSeek Harness (dsh).

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to provision a Huawei Cloud Flexus X instance, install DeepSeek Harness, and receive post-deployment access and verification guidance. It is intended for managed cloud deployment workflows that require explicit user confirmation before creating billable infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment can create billable Huawei Cloud resources.

Mitigation: Require explicit confirmation of region, flavor, and billing mode before deployment, and direct users to official Huawei Cloud pricing information.

Risk: Huawei Cloud credentials and optional DeepSeek API keys could be exposed if handled in conversation or command output.

Mitigation: Use temporary least-privilege credentials through environment variables, avoid printing secrets, and review credential handling before installation or execution.

Risk: Security evidence says the actual network setup may contradict SSH-only access claims and could expose the web UI to cloud-network peers.

Mitigation: Review the security group and network behavior after deployment, avoid relying on SSH-only claims until the code is fixed, and bind or remove nginx according to the intended access model.

Risk: Automatic confirmation and force-delete options can create or remove cloud resources without sufficient review.

Mitigation: Avoid --auto-confirm and --force-delete unless the operator fully understands the impact and has verified the target resources.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Conversation Examples](references/conversation-examples.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [DeepSeek Harness GitHub](https://github.com/deepseek-ai/deepseek-harness)
- [Huawei Cloud Flexus X Documentation](https://support.huaweicloud.com/productdesc-flexusx/pd_01_0002.html)
- [Huawei Cloud Pricing Calculator](https://www.huaweicloud.com/pricing/calculator.html#/hecs)
- [Huawei Cloud AK/SK Authentication](https://support.huaweicloud.com/api-iam/iam_01_0001.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command examples, deployment summaries, credential-handling guidance, and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Huawei Cloud region, flavor, billing mode, server identifiers, SSH tunnel command, and post-deployment security checklist.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
