## Description: <br>
Deploys the JiuwenSwarm/JiuwenClaw multi-agent collaboration platform on Huawei Cloud Flexus L instances, including instance creation, remote installation, model configuration, and Xiaoyi, Feishu, or DingTalk channel setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to provision or target a Huawei Cloud Flexus L instance, deploy JiuwenSwarm, verify the service, and configure model or messaging-channel credentials. <br>

### Deployment Geography for Use: <br>
China (Huawei Cloud cn-north-4) <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create paid Huawei Cloud resources. <br>
Mitigation: Require explicit user approval for resource creation, verify estimated costs and auto-renew settings, and avoid noninteractive confirmation unless the exact resource has already been approved. <br>
Risk: The skill can run root-level remote commands on cloud servers through Huawei Cloud COC. <br>
Mitigation: Use temporary, least-privilege credentials; review generated commands before execution; and monitor COC execution UUIDs and logs. <br>
Risk: The deployed web service and default CORS settings may expose a public interface. <br>
Mitigation: Restrict security group ingress for port 5173, narrow allowed origins, and close public access when the web UI is not needed. <br>
Risk: Model, Huawei Cloud, and messaging-channel credentials may be exposed through files, prompts, or logs. <br>
Mitigation: Use STS credentials where possible, redact secrets from logs, avoid printing credentials, and tighten file permissions for API keys and channel secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-deploy-jiuwenswarm) <br>
- [API Specification](references/api_specs.md) <br>
- [Deployment Checklist](references/deployment_checklist.md) <br>
- [IAM Permission Policies](references/iam_policies.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Huawei Cloud IAM FAQ](https://support.huaweicloud.com/iam_faq/iam_01_0620.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code, markdown] <br>
**Output Format:** [Markdown guidance with shell commands, status text, generated configuration, and JSON status files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instance, order, public IP, COC execution UUID, deployment status, web access URL, and troubleshooting outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
