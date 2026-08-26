## Description:

Deploys JiuwenSwarm or JiuwenClaw on Huawei Cloud Flexus L instances and guides instance creation, COC remote deployment, model setup, and messaging channel configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to provision or target Huawei Cloud Flexus L instances, deploy the JiuwenSwarm or JiuwenClaw platform, and configure model APIs plus Xiaoyi, Feishu, or DingTalk message channels.

### Deployment Geography for Use:

Global use; Huawei Cloud deployment target is cn-north-4.

## Known Risks and Mitigations:

Risk: The skill can create or modify billable Huawei Cloud resources.

Mitigation: Require explicit user confirmation before cloud changes and review costs, auto-renew settings, resource sizes, region, and target instance IDs before execution.

Risk: The skill can run remote commands as root on target instances through Huawei Cloud COC.

Mitigation: Review the remote scripts, target hosts, COC execution UUIDs, and logs before continuing between deployment phases.

Risk: Huawei Cloud, model API, and messaging channel credentials are needed for deployment and configuration.

Mitigation: Use temporary least-privilege credentials where possible, provide secrets only through environment variables or secured inputs, avoid printing secrets in chat or logs, and rotate keys used during testing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-flexus-l-deploy-jiuwenswarm)
- [API Specification](references/api_specs.md)
- [IAM Permission Policies](references/iam_policies.md)
- [Deployment Checklist](references/deployment_checklist.md)
- [Troubleshooting Guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, status summaries, configuration values, URLs, and error messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include deployment status, COC execution UUIDs, instance identifiers, web access URLs, and remediation steps; secrets should not be printed or pasted.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
