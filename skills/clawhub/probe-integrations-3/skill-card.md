## Description:

Deploys PowerShell 7 and Rust command-line tools on Windows, configures UTF-8 shell output and pwsh defaults, and provides verification and usage guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install or update PowerShell 7 and common Rust command-line utilities on Windows, configure their user-level shell defaults, and check the resulting setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can execute an unauthenticated PowerShell archive, including one obtained through automatic mirror downloads.

Mitigation: Authenticate an official PowerShell ZIP independently, pass it with -ZipPath, and use -SkipDefaults and -SkipRustTools to avoid automatic archive selection, mirror downloads, and configuration replacement. Honor client security blocks.

Risk: Enabling defaults can overwrite shell profiles, terminal settings, and registry entries.

Mitigation: Back up affected profiles, terminal settings, and registry entries before enabling defaults; restore prior settings rather than deleting entire keys.

## Reference(s):

- [PowerShell releases](https://github.com/PowerShell/PowerShell/releases)
- [Troubleshooting guide](references/troubleshooting.md)
- [ClawHub release](https://clawhub.ai/yujianyu/skills/probe-integrations-3)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [PowerShell scripts and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation and user-level shell configuration changes; optional diagnostic report.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
