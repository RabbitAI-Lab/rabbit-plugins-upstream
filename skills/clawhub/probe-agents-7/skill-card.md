## Description:

Deploys PowerShell 7 and a set of command-line tools on Windows, helps resolve shell-output encoding issues, and provides optional user-level shell configuration and verification guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yujianyu](https://clawhub.ai/user/yujianyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Windows users use this skill to install or verify PowerShell 7 and common command-line tools, address shell-output encoding issues, and optionally configure pwsh as their default user-level shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may run packages that have not been independently verified, and default setup can change shell settings and file associations.

Mitigation: Prefer verified official installers; independently verify the PowerShell archive. Back up shell and editor settings, and use -SkipDefaults and -SkipRustTools when appropriate.

Risk: Troubleshooting guidance may suggest workarounds when security controls block an operation.

Mitigation: Respect host security denials rather than following workaround instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yujianyu/skills/probe-agents-7)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Diagnostic text]

**Output Format:** [PowerShell scripts and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
