## Description:

Windows Shell gives agents practical guidance for choosing Git Bash, PowerShell, or WSL on Windows 10/11 and avoiding common encoding, MSYS2 path-conversion, virtual environment, and pipeline-status pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenmo0414](https://clawhub.ai/user/chenmo0414)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when working in Windows command-line environments to select the right shell and avoid silent failures from encoding defaults, MSYS2 argument rewriting, WSL filesystem boundaries, virtualenv activation, and shell pipeline status handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest optional one-time configuration commands that change user-level environment variables or global git settings.

Mitigation: Review the commands before running them and apply only the settings that match the user's Windows environment and project policy.

Risk: Windows shell guidance can affect command behavior when switching between Git Bash, PowerShell, and WSL.

Mitigation: Use the skill's shell-routing guidance to keep routine development commands in Git Bash and switch to PowerShell or WSL only for the documented cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenmo0414/skills/windows-shell)
- [Publisher profile](https://clawhub.ai/user/chenmo0414)
- [Project homepage](https://github.com/Chenmo0414/win-encoding-fix)
- [Encoding details](references/encoding.md)
- [Git Bash pitfalls](references/gitbash-pitfalls.md)
- [MSYS2 path conversion and symlinks](references/msys2.md)
- [Shell routing](references/shell-routing.md)
- [WSL guidance](references/wsl.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, tables, and reference links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and may include optional one-time user-level environment and git configuration commands.]

## Skill Version(s):

5.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
