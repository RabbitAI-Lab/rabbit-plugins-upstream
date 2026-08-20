## Description:

Windows command-line guidance for choosing Git Bash, PowerShell, or WSL and avoiding encoding, MSYS2 argument rewriting, path, virtual environment, and Git configuration pitfalls on Windows 10/11.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenmo0414](https://clawhub.ai/user/chenmo0414)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to run command-line workflows on Windows 10/11 with the right shell and safer handling of encoding, MSYS2 path conversion, WSL boundaries, Python/Node tooling, Git, and virtual environments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup snippets can change user-level Python encoding variables, shell profile files, and global Git settings.

Mitigation: Review each setup command before applying it and limit changes to user-level configuration unless an operator explicitly approves broader changes.

Risk: The skill includes shell routing guidance for Windows workflows and is not a basis for an agent to perform administrator-only UAC actions.

Mitigation: Keep administrator-only actions as human-executed steps and avoid commands that wait on an unattended UAC prompt.

## Reference(s):

- [Skill release page](https://clawhub.ai/chenmo0414/skills/windows-shell)
- [Project homepage](https://github.com/Chenmo0414/win-encoding-fix)
- [Encoding details](references/encoding.md)
- [MSYS2 argument rewriting and symlinks](references/msys2.md)
- [Shell routing](references/shell-routing.md)
- [Git Bash pitfalls](references/gitbash-pitfalls.md)
- [WSL guidance](references/wsl.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell and PowerShell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and should be reviewed before applying user-level environment variable, shell profile, or global Git configuration changes.]

## Skill Version(s):

5.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
