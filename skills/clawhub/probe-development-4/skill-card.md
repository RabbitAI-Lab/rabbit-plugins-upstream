## Description:

Deploys PowerShell 7 and the Rust command-line toolkit on Windows, improves UTF-8 shell output, and can configure pwsh as the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill on Windows to install or verify PowerShell 7 and command-line tools such as ripgrep, fd, fzf, bat, delta, and jq. It also provides UTF-8 shell guidance and optional user-level configuration for pwsh.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can run downloaded or locally supplied binaries that have not been independently verified.

Mitigation: Independently verify installation packages before running them; -SkipDefaults skips configuration replacement but does not prevent binary execution.

Risk: Default setup can replace existing shell and editor settings, including PowerShell profiles and user-level defaults.

Mitigation: Back up PowerShell profiles and Terminal/VSCode settings first, or use -SkipDefaults to avoid configuration replacement.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yujianyu/skills/probe-development-4)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [PowerShell scripts, shell commands, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-only; installation may write user-level files, PATH, registry entries, and PowerShell profiles. Supports options to skip default configuration or perform checks only.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
