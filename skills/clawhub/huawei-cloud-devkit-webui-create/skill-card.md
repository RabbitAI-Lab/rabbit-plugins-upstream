## Description:

Installs Kunpeng DevKit in WebUI mode on Huawei Cloud by guiding Kunpeng ECS preparation, remote installation, verification, and secure KMS cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to create or select a Kunpeng aarch64 ECS and install Kunpeng DevKit in WebUI mode. It also guides prerequisite checks, security group setup, installation verification, and cleanup of the KMS key used during setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use cloud credentials to create ECS, EIP, security-group, and KMS resources.

Mitigation: Use least-privilege IAM permissions scoped to the DevKit workflow and review all resource changes before execution.

Risk: Opening SSH and WebUI ports can expose the instance to public network access.

Mitigation: Restrict security group sources to the user's IP address or VPN instead of 0.0.0.0/0.

Risk: The installation downloads and runs DevKit packages and scripts on a root-access ECS.

Mitigation: Confirm package sources, verify signatures or integrity checks, and stop if verification fails.

Risk: SSH access and DevKit setup depend on sensitive credentials, generated passwords, logs, and KMS decrypt operations.

Mitigation: Do not print secrets, verify SSH host keys, protect logs, and run KMS cleanup only after successful installation verification.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-devkit-webui-create)
- [Prerequisites](references/prerequisites.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [ECS Creation Guide](references/ecs-creation-guide.md)
- [SSH Connection Guide](references/ssh-connection-guide.md)
- [DevKit Installation Workflow](references/devkit-installation-workflow.md)
- [DevKit Installation Guide](references/devkit-installation-guide.md)
- [Polling Progress Guide](references/polling-progress-guide.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Security Design](references/security-design.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include cloud resource identifiers, verification status, and cleanup steps; secrets should not be printed or requested in conversation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
