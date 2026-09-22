## Description:

Installs Kunpeng DevKit in WebUI mode on Huawei Cloud by creating or using a Kunpeng ECS, managing credentials with KMS, and running the DevKit installer through scripted SSH workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud engineers use this skill to prepare Huawei Cloud Kunpeng infrastructure, install Kunpeng DevKit WebUI, verify service access, and manage credential cleanup after installation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automates high-impact cloud and root actions.

Mitigation: Install only in a dedicated test or disposable Huawei Cloud account or ECS with least-privilege credentials.

Risk: Security group rules may expose SSH or DevKit WebUI services broadly.

Mitigation: Restrict security-group sources to the user's IP address or VPN instead of 0.0.0.0/0.

Risk: Custom DevKit package URLs can create unsafe package trust.

Mitigation: Do not use custom package URLs unless the signer is independently verified.

Risk: SSH setup can expose root credentials to host-key substitution or untrusted endpoints.

Mitigation: Verify SSH host keys before sending root credentials.

Risk: KMS cleanup can disable or delete a key that was not created by this run.

Mitigation: Avoid cleanup-kms unless the key alias or ID has been confirmed as created by this run.

## Reference(s):

- [Prerequisites - Kunpeng DevKit WebUI Installation](references/prerequisites.md)
- [CLI Installation Guide - Kunpeng DevKit WebUI Mode](references/cli-installation-guide.md)
- [IAM Permission Policies - Kunpeng DevKit WebUI Mode](references/iam-policies.md)
- [ECS Creation Guide - Kunpeng DevKit WebUI Mode](references/ecs-creation-guide.md)
- [Security Design - Password Lifecycle and Tool Separation](references/security-design.md)
- [SSH Connection Guide - Python paramiko SSH](references/ssh-connection-guide.md)
- [DevKit Installation Workflow](references/devkit-installation-workflow.md)
- [Installation Guide - Kunpeng DevKit WebUI Mode](references/devkit-installation-guide.md)
- [Polling Progress Guide](references/polling-progress-guide.md)
- [Verification Method - Kunpeng DevKit WebUI Mode Installation](references/verification-method.md)
- [Acceptance Criteria - huawei-cloud-devkit-webui-create](references/acceptance-criteria.md)
- [Troubleshooting - Kunpeng DevKit WebUI Mode Installation](references/troubleshooting.md)
- [Huawei Cloud KooCLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003_02.html)
- [Huawei Cloud KooCLI Configuration Guide](https://support.huaweicloud.com/productdesc-hcli/hcli_01_0001.html)
- [Kunpeng DevKit Official Installation Documentation](https://www.hikunpeng.com/document/detail/zh/kunpengdevps/install/installguide/KunpengDevKit_0018.html)
- [Kunpeng DevKit Download Center](https://www.hikunpeng.com/developer/devkit/download)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and script invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational steps for Huawei Cloud resources, SSH installation, verification, and KMS cleanup.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
