## Description: <br>
Creates a Huawei Cloud Flexus L Instance, deploys the OpenClaw application platform, and supports model and channel configuration for deployed OpenClaw instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to deploy OpenClaw on Huawei Cloud Flexus L servers, then configure LLM providers and messaging channels such as WeCom, Feishu, DingTalk, and QQ. <br>

### Deployment Geography for Use: <br>
Limited to Huawei Cloud regions listed by the skill evidence: China North-Beijing-4, China East-Shanghai-1, China South-Guangzhou, and China Southwest-Guiyang-1. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Huawei Cloud credentials and downstream model or channel secrets. <br>
Mitigation: Use restricted, temporary credentials; prefer environment variables; avoid passing secrets on command lines; and review output before sharing logs. <br>
Risk: The deployment can create billable Huawei Cloud resources with auto-pay or auto-renew behavior. <br>
Mitigation: Confirm region, instance settings, billing impact, quotas, and cleanup plans before deployment. <br>
Risk: Model and channel setup may execute downloaded installer scripts remotely as root. <br>
Mitigation: Run only on isolated or approved instances, inspect the referenced installer behavior before use, and accept remote execution only when it matches the deployment policy. <br>
Risk: OpenClaw Web UI access requires manual network exposure. <br>
Mitigation: Restrict access to trusted IP ranges or private access paths and avoid exposing the Web UI broadly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-flexus-l-server-openclaw-deployment) <br>
- [IAM Permission Policy Reference](references/iam-policies.md) <br>
- [Skill Verification Method](references/verification-method.md) <br>
- [Huawei Cloud Flexus L Instance Console](https://console.huaweicloud.com/smb/?/resource/list) <br>
- [Huawei Cloud PyPI mirror](https://repo.huaweicloud.com/repository/pypi/simple) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud resource IDs, region identifiers, credential environment variable names, and model or channel configuration examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata, OpenClaw frontmatter metadata, and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
