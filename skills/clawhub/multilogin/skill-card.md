## Description:

Helps agents manage Multilogin X browser profiles with the xcli CLI, including disposable profile launch, saved profile lifecycle actions, and launcher status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[multilogincom](https://clawhub.ai/user/multilogincom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to install and run Multilogin X CLI tooling, launch headless or desktop browser profiles, manage cloud-phone profiles, and troubleshoot launcher/profile operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow downloads mutable native binaries from latest-version endpoints.

Mitigation: Use pinned and verified binary versions from a trusted Multilogin source, and review generated install commands before execution.

Risk: Account passwords, proxy credentials, and delegated node messages may expose secrets if pasted directly into commands.

Mitigation: Avoid placing secrets in shell history or remote-node messages; use explicit credential handling and rotate exposed credentials.

Risk: Cloud-phone starts can consume metered mobile minutes and ADB access can expose active remote-device control.

Mitigation: Check plan limits before starting phones, require confirmation before enabling ADB, stop phones when finished, and disable ADB/disconnect sessions after use.

Risk: Profile deletes, transfers, 2FA changes, and remote-node delegation can affect account state or access.

Mitigation: Require explicit user confirmation before destructive, billing-related, access-control, or delegated execution steps.

## Reference(s):

- [Multilogin X skill page](https://clawhub.ai/multilogincom/skills/multilogin)
- [xcli latest version endpoint](https://ml000x-dev-dists.s3.eu-north-1.amazonaws.com/cli-mlx/latest)
- [mlx-launcher latest version endpoint](https://ml000x-dev-dists.s3.eu-north-1.amazonaws.com/launcher-mlx/latest)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational CLI guidance for xcli, mlx-launcher, profile management, cloud-phone workflows, ADB access, and troubleshooting.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
