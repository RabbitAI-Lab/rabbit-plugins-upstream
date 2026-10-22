## Description:

Deploys PowerShell 7 and a Windows command-line toolkit, configures UTF-8 output and shell defaults, and provides verification and rollback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Windows developers and technical users use this skill to install or upgrade PowerShell 7 and common command-line tools, troubleshoot UTF-8 output, and optionally configure user-level shell defaults.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer may download binaries through mirrors that have not been independently verified.

Mitigation: Prefer an independently verified local PowerShell ZIP with -ZipPath, and use -SkipRustTools and -SkipDefaults when appropriate.

Risk: Enabling defaults can modify shell profiles and user-level shell or terminal settings.

Mitigation: Back up PowerShell profiles, Windows Terminal settings, and VS Code settings first; use -SkipDefaults to avoid default changes and review the documented rollback steps.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yujianyu/skills/probe-other-5)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with PowerShell commands and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Following installation guidance may change user-level shell settings; default changes are optional.]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
