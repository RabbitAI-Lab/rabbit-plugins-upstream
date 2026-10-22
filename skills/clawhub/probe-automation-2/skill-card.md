## Description:

Installs PowerShell 7 and common Rust-based command-line tools on Windows, configures UTF-8 output and optional default-shell settings, and includes a verification script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Windows developers and engineers use this skill to install or verify PowerShell 7 and common command-line tools, resolve UTF-8 output issues, and optionally configure pwsh as the default shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may execute downloaded software without verified integrity.

Mitigation: Prefer an official PowerShell archive; verify its published SHA-256 before supplying it with -ZipPath, and avoid untrusted custom mirrors.

Risk: Installation can overwrite existing shell profiles and terminal or editor settings.

Mitigation: Back up PowerShell profiles and terminal/editor settings first; use -SkipDefaults and -SkipRustTools to limit changes and additional downloads.

Risk: Suggested workarounds could bypass client security protections.

Mitigation: Respect security denials and do not follow workarounds that bypass them.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/yujianyu/skills/probe-automation-2)
- [Publisher profile](https://clawhub.ai/user/yujianyu)
- [Microsoft Get-FileHash documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash?view=powershell-7.5#example-3-compute-the-hash-value-of-a-stream)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with PowerShell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-focused installation, configuration, verification, and rollback guidance.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata; artifact frontmatter and changelog state 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
