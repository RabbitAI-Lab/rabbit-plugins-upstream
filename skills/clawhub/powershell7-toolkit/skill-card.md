## Description:

Deploys PowerShell 7 and the Rust high-performance CLI toolchain (ripgrep, fd, fzf, bat, delta, and jq) on Windows, addresses Chinese text-encoding issues, and can configure pwsh as the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install and configure PowerShell 7 and a Rust-based command-line toolkit on Windows, troubleshoot text-encoding issues, and verify the resulting setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may run installation packages whose authenticity has not been independently verified.

Mitigation: Independently verify an official PowerShell ZIP and select it explicitly with -ZipPath before running the installer.

Risk: Enabling defaults can replace existing PowerShell profiles and application settings.

Mitigation: Use -SkipDefaults to avoid replacing profiles and application settings; back up existing PowerShell profiles and terminal settings before enabling defaults.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yujianyu/skills/powershell7-toolkit)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [PowerShell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-specific; installation may change user-level settings when defaults are enabled.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
