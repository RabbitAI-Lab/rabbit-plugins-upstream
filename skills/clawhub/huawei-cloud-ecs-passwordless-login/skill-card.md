## Description:

Configure passwordless SSH login to Huawei Cloud ECS instances using COC, including IAM agency authorization, Ed25519 key generation, COC script deployment across one or many ECS instances, SSH testing, and timed key cleanup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and administrators use this skill to set up temporary passwordless SSH access to Huawei Cloud ECS instances through COC-managed script execution. It is intended for deliberate administrative workflows that need batch target resolution, connection verification, and post-use key cleanup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow grants the agent Huawei Cloud COC/IAM authority and SSH access to selected ECS hosts.

Mitigation: Install and run it only for deliberate administrative workflows, use the least-privileged practical IAM user, avoid root SSH where possible, and keep batches small.

Risk: SSH ControlMaster persistence intentionally keeps sessions usable after the temporary key is removed.

Mitigation: Remove or opt out of ControlMaster persistence when it is not required, and clean up SSH config entries and control sockets after the workflow.

Risk: Disabling strict host key checking can make SSH connections easier to misdirect.

Mitigation: Verify SSH host keys before use when operating in sensitive environments.

Risk: Temporary SSH keys or reusable COC scripts could linger if cleanup fails or the process is interrupted.

Mitigation: Validate or create a unique per-run COC script, confirm remote key removal, delete local key files, delete COC scripts, and use the documented fallback cleanup path for failed hosts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-ecs-passwordless-login)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/intl/en-us/usermanual-hcli/hcli_01_001.html)
- [Huawei Cloud KooCLI Linux Binary](https://hwcloudcli.obs.cn-north-1.myhuaweicloud.com/cli/latest/hcloud_linux_amd64)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands, status summaries, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-step progress, target resolution, SSH test results, cleanup timer details, and connection commands without exposing private key contents.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
