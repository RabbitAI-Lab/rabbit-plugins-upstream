## Description: <br>
Manages Huawei Cloud Flexus L server lifecycle tasks, including creating, renewing, and unsubscribing instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to manage Huawei Cloud Flexus L instances for provisioning, renewals, and resource cleanup. It supports cost-sensitive lifecycle actions that may create charges, payments, refunds, or cancellations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, renew, pay for, refund, or unsubscribe billable Huawei Cloud resources. <br>
Mitigation: Use temporary least-privilege credentials, review dry-run previews first, and require explicit confirmation before executing cost-affecting actions. <br>
Risk: Security evidence reports disabled TLS verification in sensitive API calls. <br>
Mitigation: Treat disabled TLS verification as a production blocker and fix certificate verification before production use. <br>
Risk: The skill requires credentials with broad cloud and billing permissions. <br>
Mitigation: Prefer scoped temporary AK/SK credentials with a security token and avoid exposing credentials in commands, logs, or conversation output. <br>


## Reference(s): <br>
- [Huawei Cloud Flexus L Instance Create API](https://support.huaweicloud.com/api-flexusl/create_instance_0001.html) <br>
- [Huawei Cloud Console](https://console.huaweicloud.com/) <br>
- [IAM API Reference](https://support.huaweicloud.com/api-iam/iam_01_0001.html) <br>
- [API Reference](references/api-reference.md) <br>
- [Permission Guide](references/permission-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Image Specs Guide](references/image-specs-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and structured parameter summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include dry-run previews, confirmation prompts, error summaries, and Huawei Cloud resource identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
