## Description: <br>
Supports Huawei Cloud Flexus L instance and traffic queries, plus confirmed start, stop, reboot, password reset, and server metadata update operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operators and developers use this skill to inspect Huawei Cloud Flexus L instances, monitor traffic package usage, and carry out operational changes such as lifecycle actions, password resets, and metadata updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use Huawei Cloud credentials to change server state, including lifecycle actions, password resets, and metadata updates. <br>
Mitigation: Use temporary least-privilege credentials, verify exact ECS, BSS, Config, and IAM permissions, confirm target instance IDs and regions, and require explicit confirmation before every state-changing operation. <br>
Risk: Credential handling mistakes could expose AK, SK, or security token values. <br>
Mitigation: Pass credentials through environment variables, do not paste secrets into chat, avoid commands that print secrets, and rotate or revoke credentials after use when appropriate. <br>
Risk: The security scan marked the release suspicious because credential and permission guidance is incomplete or unsafe. <br>
Mitigation: Review the skill before installation, restrict use to environments where Huawei Cloud Flexus L operations are intended, and validate commands against the documented IAM policy before execution. <br>


## Reference(s): <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Huawei Cloud Flexus Application Server L Instance Documentation](https://support.huaweicloud.com/intl/zh-cn/flexusl_faq/faq_01_0003.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud credentials and explicit user confirmation before lifecycle, password, or metadata changes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
