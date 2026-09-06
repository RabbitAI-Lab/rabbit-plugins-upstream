## Description:

Deploys DeepSeek Harness (dsh) on Huawei Cloud Flexus X ECS instances with user confirmation, credential handling, and SSH-tunneled web access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to create, verify, manage, and delete Huawei Cloud ECS deployments for DeepSeek Harness. It is intended for external users who need a guided deployment flow with explicit confirmation before paid resources are created.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create paid Huawei Cloud resources.

Mitigation: Require explicit user confirmation of region, instance flavor, and billing mode before deployment, and direct users to the official Huawei Cloud pricing calculator.

Risk: Cloud access keys, security tokens, generated root passwords, and optional DeepSeek API keys may be exposed if handled carelessly.

Mitigation: Use temporary least-privilege credentials through environment variables, avoid command-line secrets, do not print secret values, and rotate or protect generated credentials after deployment.

Risk: The deployed dsh web interface can run workflows and should not be exposed publicly.

Mitigation: Keep dsh bound to 127.0.0.1, access it through an SSH local port-forwarding tunnel, and restrict security group ingress to TCP 22 from the user's /32 IP.

Risk: Delete operations can remove ECS resources and associated data.

Mitigation: Verify exact server IDs or names before deletion and avoid force-delete options unless the user has intentionally accepted the impact.

Risk: Disabling TLS verification can expose cloud API traffic and credentials.

Mitigation: Keep SSL verification enabled for production use and treat HW_VERIFY_SSL=false as a testing-only override.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Methods](references/verification-method.md)
- [Conversation Examples](references/conversation-examples.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [DeepSeek Harness GitHub](https://github.com/deepseek-ai/deepseek-harness)
- [Huawei Cloud Flexus X Documentation](https://support.huaweicloud.com/productdesc-flexusx/pd_01_0002.html)
- [Huawei Cloud AK/SK Authentication](https://support.huaweicloud.com/api-iam/iam_01_0001.html)
- [Huawei Cloud Pricing Calculator](https://www.huaweicloud.com/pricing/calculator.html#/hecs)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment replies should include copy-paste-ready SSH tunnel commands, resource details, and post-deployment security group guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/scripts/pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
