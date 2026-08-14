## Description:

Use when you need to manage Multilogin X browser profiles: launch quick disposable profiles, list/start/stop saved profiles, or check launcher status using the xcli CLI tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[multilogincom](https://clawhub.ai/user/multilogincom)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to install and run Multilogin X CLI tooling, manage anti-detect browser profiles, and administer related mobile profile workflows through guided shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers high-trust Multilogin administration beyond browser launching, including credential, billing, transfer, 2FA, cloud-phone, ADB, file, object, script, and cookie commands.

Mitigation: Install only when broad account administration is intended, review planned commands before execution, and confirm destructive or billing-impacting actions manually.

Risk: Credentials and short-lived ADB glogin codes can be exposed if placed in command lines, logs, or cross-node messages.

Mitigation: Prompt for secrets at execution time where possible, avoid logging or persisting them, and do not pass passwords through shared messages.

Risk: Delete, transfer, mobile-phone start, file deletion, and billing-related commands can cause permanent changes or charges.

Mitigation: Check limits before starting cloud phones, stop phones when complete, and require explicit confirmation before irreversible or billable actions.

## Reference(s):

- [Multilogin X ClawHub Skill](https://clawhub.ai/multilogincom/skills/multiloginx)
- [Multilogin Publisher Profile](https://clawhub.ai/user/multilogincom)
- [Multilogin X CLI Latest Version Endpoint](https://ml000x-dev-dists.s3.eu-north-1.amazonaws.com/cli-mlx/latest)
- [Multilogin X Launcher Latest Version Endpoint](https://ml000x-dev-dists.s3.eu-north-1.amazonaws.com/launcher-mlx/latest)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires xcli and mlx-launcher binaries; some commands require authenticated Multilogin credentials and an active launcher.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
