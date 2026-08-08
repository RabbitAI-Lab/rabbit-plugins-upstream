## Description: <br>
Creates a Huawei Cloud Flexus L Instance, deploys the OpenClaw application platform, and supports model and messaging-channel configuration for deployed OpenClaw instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations engineers use this skill to provision Huawei Cloud Flexus L instances for OpenClaw and then configure models and messaging channels such as WeCom, Feishu, DingTalk, and QQ. It is intended for OpenClaw deployment and post-deployment setup workflows that can create billable cloud resources. <br>

### Deployment Geography for Use: <br>
Global, subject to Huawei Cloud service availability and the skill's documented supported regions. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create billable Huawei Cloud resources with prepaid monthly charging and auto-renew behavior. <br>
Mitigation: Review resource settings before execution, use a controlled test account or project, and confirm billing and renewal settings in Huawei Cloud after deployment. <br>
Risk: Model and channel setup can run remote COC scripts on the target instance. <br>
Mitigation: Run setup only after reviewing the script behavior and accepting remote execution on the instance; use temporary credentials with only the documented minimum permissions. <br>
Risk: Huawei Cloud AK/SK, security tokens, model API keys, and channel secrets may be exposed if passed on command lines or logged. <br>
Mitigation: Prefer environment variables or secure interactive entry, avoid command history exposure, and rotate credentials after testing or any suspected exposure. <br>


## Reference(s): <br>
- [IAM Permission Policy Reference](references/iam-policies.md) <br>
- [Skill Verification Method](references/verification-method.md) <br>
- [Huawei Cloud Python Package Index Mirror](https://repo.huaweicloud.com/repository/pypi/simple) <br>
- [Huawei Cloud Flexus L Instance Console](https://console.huaweicloud.com/smb/?/resource/list) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with command-line invocations and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include deployment status, resource identifiers, COC execution results, and manual Web UI access steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, skill metadata, pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
