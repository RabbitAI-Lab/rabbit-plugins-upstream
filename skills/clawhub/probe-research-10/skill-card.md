## Description:

Deploys PowerShell 7 and Rust command-line tools on Windows, configures UTF-8 shell output, and can make PowerShell 7 the default shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install or upgrade PowerShell 7 and a Windows command-line toolchain, resolve shell encoding problems, and configure PowerShell 7 as the default shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may download binaries through mirrors without verifying them.

Mitigation: Avoid the one-command installation until download verification is fixed; independently verify an official PowerShell archive and use -ZipPath with -SkipDefaults and -SkipRustTools.

Risk: Enabling defaults may overwrite existing shell and editor settings.

Mitigation: Back up existing profiles and application settings before enabling defaults, review registry removal instructions, and follow host execution restrictions.

## Reference(s):

- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-focused setup guidance and scripts; installation may download binaries and change user-level shell settings.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
