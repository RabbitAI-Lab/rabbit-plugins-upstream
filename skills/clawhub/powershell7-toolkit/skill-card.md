## Description:

Deploys PowerShell 7 and Rust-based command-line tools on Windows, improves UTF-8 output, and configures pwsh as the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this Windows-focused skill to install or verify PowerShell 7 and command-line tools, address encoding issues, and configure pwsh as the default shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The toolkit runs unverified downloads from third-party proxies and may erase existing shell configuration during setup.

Mitigation: Start with -CheckOnly, prefer a separately verified installation using Microsoft's guide, and back up PowerShell profiles and terminal/editor settings. Avoid default setup until download verification and configuration preservation are addressed; -SkipDefaults does not disable executable downloads.

## Reference(s):

- [Microsoft PowerShell installation guide](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with PowerShell code blocks and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-focused; installation and setup can change user and system configuration.]

## Skill Version(s):

1.1.5 (source: target metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
