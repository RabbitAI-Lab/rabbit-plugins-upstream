## Description:

Deploys PowerShell 7 and Rust-based command-line tools on Windows, configures UTF-8 shell output, and can set pwsh as the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT

## Use Case:

Developers and Windows users use this skill to deploy PowerShell 7 and command-line utilities, improve UTF-8 output, and optionally configure user-level shell defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may use unverified mirror downloads and can change existing shell or editor settings.

Mitigation: Prefer independently verified upstream packages, use -SkipDefaults until configuration changes are reviewed, and back up PowerShell profiles, editor settings, and affected registry entries; uninstall instructions do not restore prior values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yujianyu/skills/probe-lifestyle-11)
- [Microsoft Get-FileHash verification guidance](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.6)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with PowerShell code blocks and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes optional installation, verification, and user-level configuration steps.]

## Skill Version(s):

0.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
