## Description:

Create Huawei Cloud Flexus L Instance (Lightweight Server), deploy OpenClaw application platform on it, and support installation and configuration of models and channels for deployed OpenClaw instances.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to deploy OpenClaw on Huawei Cloud Flexus L instances, then configure language models and messaging channels.

### Deployment Geography for Use:

China (documented region examples are in China; verify current service availability).

## Known Risks and Mitigations:

Risk: Cloud and model credentials may be exposed in output or logs.

Mitigation: Use narrowly scoped temporary credentials, avoid production credentials during review, remove secret-bearing COC scripts after use, and rotate any credentials already exposed in logs.

Risk: Instance deployment may incur recurring charges.

Mitigation: Review and explicitly confirm payment and renewal terms before creating an instance.

Risk: Unverified downloads may run with administrator privileges.

Mitigation: Verify installer sources and integrity before execution, and do not run unverified downloads with administrator privileges.

Risk: An exposed OpenClaw Web UI may be reachable over an unsafe connection.

Mitigation: Access the Web UI through a private connection or a restricted HTTPS endpoint.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-flexus-l-server-openclaw-deployment)
- [Huawei Cloud Flexus console](https://console.huaweicloud.com/smb/?/resource/list)
- [Huawei Cloud Python package index](https://repo.huaweicloud.com/repository/pypi/simple)

## Skill Output:

**Output Type(s):** [guidance, shell commands, JSON configuration]

**Output Format:** [Markdown instructions with shell-command examples and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deployment requires Huawei Cloud credentials and permissions; Web UI access must be enabled separately in the Huawei Cloud console.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
