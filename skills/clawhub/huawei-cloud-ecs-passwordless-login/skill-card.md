## Description:

Configure passwordless SSH login to Huawei Cloud ECS instances using COC by automating IAM agency authorization, SSH key generation, COC script deployment, SSH testing, and timed key cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to establish temporary passwordless SSH access to Huawei Cloud ECS instances through COC, including agency setup, script execution, connection verification, and cleanup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow creates privileged SSH access to a Huawei Cloud ECS instance.

Mitigation: Use a test or tightly scoped account first and install only when root-level SSH access is intended.

Risk: SSH access can survive key cleanup through ControlMaster configuration and socket state.

Mitigation: Manually remove the SSH config entry and socket after use, and confirm authorized_keys and temporary keys are deleted.

Risk: Existing COC scripts or broad agency permissions can expand the impact of execution.

Mitigation: Verify any existing COC script before execution and avoid broad FOREVER agency permissions where possible.

Risk: Host-key verification is weakened by the workflow's SSH options.

Mitigation: Restore SSH host-key verification after setup and use normal known_hosts checks for ongoing access.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/intl/en-us/usermanual-hcli/hcli_01_001.html)
- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-passwordless-login)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and structured status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes IAM, COC, SSH, and cleanup steps for a single target ECS workflow.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
