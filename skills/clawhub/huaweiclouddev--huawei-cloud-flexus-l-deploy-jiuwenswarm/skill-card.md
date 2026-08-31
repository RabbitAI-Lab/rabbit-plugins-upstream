## Description:

One-click deployment of the JiuwenSwarm multi-agent collaboration platform on Huawei Cloud Flexus L instances, including instance creation, COC-based deployment, model configuration, and message channel setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to provision Huawei Cloud Flexus L instances and deploy JiuwenSwarm/JiuwenClaw, then configure model APIs and Xiaoyi, Feishu, or DingTalk message channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan verdict is suspicious because the skill weakens stored cloud credentials and handles secrets during deployment.

Mitigation: Review before installing, use least-privilege or temporary Huawei Cloud credentials, and avoid allowing encrypted hcloud profiles to be rewritten as plaintext unless that behavior is acceptable.

Risk: The deployed JiuwenSwarm web interface can be exposed on public port 5173.

Mitigation: Keep inbound port 5173 closed by default, open it only when needed, and add appropriate access controls before external access.

Risk: Model and channel API keys may appear in outputs or COC logs.

Mitigation: Avoid sharing logs that may contain secrets and rotate model or channel API keys after exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-deploy-jiuwenswarm)
- [API Specification](references/api-specs.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Deployment Checklist](references/deployment-checklist.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Troubleshooting Guide](references/troubleshooting.md)
- [Huawei Cloud IAM FAQ](https://support.huaweicloud.com/iam_faq/iam_01_0620.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, configuration values, and deployment status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce cloud deployment commands, generated configuration, COC task identifiers, and web access URLs for the deployed service.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
