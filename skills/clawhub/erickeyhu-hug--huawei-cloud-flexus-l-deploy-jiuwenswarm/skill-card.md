## Description: <br>
Deploys the JiuwenSwarm multi-agent collaboration platform on Huawei Cloud Flexus L instances, including instance creation, remote service deployment, model configuration, and message channel setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to provision Huawei Cloud Flexus L infrastructure and deploy JiuwenSwarm/JiuwenClaw with model API settings and optional Xiaoyi, Feishu, or DingTalk channel configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create Huawei Cloud resources and run remote deployment operations with powerful cloud and root-level access. <br>
Mitigation: Use a dedicated low-privilege Huawei Cloud account or temporary STS credentials, review permissions before installation, avoid the --confirm bypass, and verify costs and auto-renew settings before instance creation. <br>
Risk: Model, channel, and cloud credentials may appear in environment variables, configuration files, terminal output, or COC results. <br>
Mitigation: Pass secrets through environment variables, redact .env, config.yaml, terminal logs, and COC output before sharing, and rotate model or channel secrets after testing. <br>
Risk: Opening public service ports can expose the JiuwenSwarm web interface. <br>
Mitigation: Restrict public ports, especially port 5173, and only open web access temporarily when needed. <br>


## Reference(s): <br>
- [API Specification](references/api_specs.md) <br>
- [Deployment Checklist](references/deployment_checklist.md) <br>
- [IAM Permission Policies](references/iam_policies.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>
- [Huawei Cloud IAM FAQ](https://support.huaweicloud.com/iam_faq/iam_01_0620.html) <br>
- [Huawei Cloud Flexus Console](https://console.huaweicloud.com/flexus/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration values, and deployment status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce cloud deployment identifiers, public access URLs, COC task UUIDs, and error summaries.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
