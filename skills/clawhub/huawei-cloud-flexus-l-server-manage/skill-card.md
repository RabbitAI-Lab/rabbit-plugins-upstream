## Description: <br>
Manages Huawei Cloud Flexus L server lifecycle: create, renew, and unsubscribe instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud Flexus L servers across provisioning, renewal, and cancellation workflows. It supports region, image, and specification lookup plus dry-run and confirmation flows for billable actions. <br>

### Deployment Geography for Use: <br>
Huawei Cloud Flexus L supported regions in Mainland China, Hong Kong, China, and Singapore. <br>

## Known Risks and Mitigations: <br>
Risk: Billable or destructive cloud operations may create, renew, auto-pay, auto-renew, or unsubscribe resources. <br>
Mitigation: Run dry-run first, verify region, resource IDs, payment defaults, auto-renew settings, and related components, then require explicit confirmation before execution. <br>
Risk: Unsafe TLS settings are reported by the security evidence, which can expose cloud API traffic on untrusted networks. <br>
Mitigation: Avoid untrusted networks and fix TLS verification before using the skill against real Huawei Cloud accounts. <br>
Risk: Huawei Cloud AK/SK credentials or security tokens could be exposed if passed in commands or logs. <br>
Mitigation: Use least-privilege temporary credentials through environment variables, include security tokens when available, and mask or omit secrets from conversation and logs. <br>


## Reference(s): <br>
- [API Reference](references/api-reference.md) <br>
- [IAM Permissions Guide](references/iam-policies.md) <br>
- [Flexus L System Images and Specifications Reference](references/image-specs-guide.md) <br>
- [Permission Guide](references/permission-guide.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Huawei Cloud Flexus L Instance Purchase Guide](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html) <br>
- [Huawei Cloud AK/SK Authentication Guide](https://support.huaweicloud.com/api-iam/iam_01_0001.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-style dry-run or result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run previews, confirmation prompts, and API result summaries; secrets should not be displayed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
