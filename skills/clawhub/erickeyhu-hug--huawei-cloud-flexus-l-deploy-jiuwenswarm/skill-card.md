## Description:

Automates deployment of the JiuwenSwarm/JiuwenClaw multi-agent collaboration platform on Huawei Cloud Flexus L instances, including instance creation, COC-based deployment, model API setup, and Xiaoyi, Feishu, or DingTalk channel configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to deploy JiuwenSwarm on Huawei Cloud Flexus L, configure model credentials, and connect supported message channels. It is intended for users who can review cloud costs, IAM permissions, network exposure, and remote execution effects before running deployment actions.

### Deployment Geography for Use:

China (Huawei Cloud cn-north-4 target region)

## Known Risks and Mitigations:

Risk: The skill handles Huawei Cloud credentials and can create paid cloud resources.

Mitigation: Use temporary STS credentials with least privilege, confirm resource creation and expected charges before execution, and avoid exposing AK/SK/Token values in prompts or logs.

Risk: Deployment relies on remote root-level script execution on target instances.

Mitigation: Review the deployment scripts and requested IAM permissions before use, run only against intended instances, and monitor COC task output for unexpected actions.

Risk: The deployed web service may require public ingress on port 5173.

Mitigation: Restrict security group ingress, CORS settings, and sender allowlists to trusted sources; close public access when it is no longer needed.

Risk: Security evidence reports unsafe or under-scoped defaults around secrets, logs, and world-readable configuration.

Mitigation: Avoid sharing logs or generated configuration until secret-printing and file-permission issues have been reviewed and fixed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-flexus-l-deploy-jiuwenswarm)
- [API Specification](artifact/references/api_specs.md)
- [Deployment Checklist](artifact/references/deployment_checklist.md)
- [IAM Permission Policies](artifact/references/iam_policies.md)
- [Troubleshooting Guide](artifact/references/troubleshooting.md)
- [Huawei Cloud IAM FAQ](https://support.huaweicloud.com/iam_faq/iam_01_0620.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, status text, and deployment configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May lead the agent through cloud API calls and remote execution steps after explicit user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
