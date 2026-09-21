## Description:

One-click deployment tool for Hermes on Huawei Cloud Flexus L instances that supports deployment, ModelArts model configuration, robot channel configuration, and gateway management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to deploy the Hermes AI Agent platform on Huawei Cloud Flexus L instances, configure ModelArts models, connect Feishu or WeCom channels, manage the gateway, and query deployment status.

### Deployment Geography for Use:

Global, subject to Huawei Cloud regional availability and the skill's supported deployment regions.

## Known Risks and Mitigations:

Risk: The skill can create paid Huawei Cloud resources.

Mitigation: Review billing settings before deployment and use a test account or budget controls when validating the skill.

Risk: The skill requires Huawei Cloud credentials that can create resources and run remote scripts.

Mitigation: Use temporary least-privilege credentials and avoid passing secrets on the command line.

Risk: Bot and gateway access may be broadly open after channel setup.

Mitigation: Manually restrict Feishu, WeCom, and gateway user access before exposing the bot.

## Reference(s):

- [IAM Permissions Policy Reference](artifact/references/iam-policies.md)
- [Skill Verification Method](artifact/references/verification-method.md)
- [Huawei Cloud PyPI Mirror](https://repo.huaweicloud.com/repository/pypi/simple)
- [ModelArts MaaS API Endpoint](https://api.modelarts-maas.com/v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create cloud resources, configure remote services, and return instance IDs, execution IDs, status values, and error messages.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact package metadata is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
