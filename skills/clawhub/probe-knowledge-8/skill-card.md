## Description:

Deploys PowerShell 7 and developer command-line tools on Windows, configures UTF-8 shell defaults, and provides installation verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install PowerShell 7 and a Windows command-line toolkit, configure user-level shell defaults, and verify the setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may execute unverified mirror downloads, replace existing shell settings, and suggest workarounds for client security blocks.

Mitigation: Back up PowerShell profiles and Windows Terminal/VSCode settings before enabling defaults. Prefer an official PowerShell ZIP whose SHA-256 hash you independently verify; keep client security restrictions in force and use an authorized workflow if execution is blocked.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yujianyu/skills/probe-knowledge-8)
- [PowerShell releases (official SHA-256 reference)](https://github.com/PowerShell/PowerShell/releases)
- [troubleshooting.md](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with PowerShell commands and scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May install files and modify current-user PATH, profiles, registry settings, and file associations.]

## Skill Version(s):

0.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
