## Description:

Deploys PowerShell 7 and selected Rust command-line tools on Windows, configures UTF-8 shell output, and can set pwsh as the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install or verify PowerShell 7 and a set of Rust command-line utilities on Windows, and to configure user-level shell settings when desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The toolkit may run programs from downloads that are not authenticated.

Mitigation: Prefer official installers until downloads are authenticated; if proceeding, explicitly choose a verified PowerShell ZIP.

Risk: Setup may overwrite existing shell settings.

Mitigation: Back up PowerShell, Windows Terminal, and VSCode settings first; use -SkipDefaults and -SkipRustTools to limit automatic changes, and respect host security denials.

## Reference(s):

- [PowerShell toolkit troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [PowerShell scripts and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional switches control installation paths, tool selection, and user-level default configuration.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
