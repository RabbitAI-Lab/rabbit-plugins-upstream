## Description:

Windows command-line encoding and compatibility guidance for GBK/UTF-8 behavior, MSYS2 path conversion, PowerShell and pwsh interoperability, Python and Node.js usage, Git configuration, and code-generation rules on Windows 10/11 with MSYS2 or Git Bash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenmo0414](https://clawhub.ai/user/chenmo0414)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose and avoid Windows shell encoding, path-conversion, and interop issues when issuing commands or generating Python, Node.js, PowerShell, and Git workflows for Windows 10/11 with MSYS2 or Git Bash.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup commands can persistently change Windows user environment variables, shell startup files, and global Git configuration.

Mitigation: Review each persistent setting before applying it, especially on shared or managed machines, and prefer command-scoped encoding or path-conversion settings when broad changes are not needed.

Risk: MSYS2 path conversion and Windows encoding behavior can silently alter arguments or produce misleading command output if the guidance is applied to the wrong failure mode.

Mitigation: Classify failures as encoding issues or path-conversion issues before applying fixes, and test commands in the target Windows shell environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenmo0414/skills/windows-shell)
- [Project homepage](https://github.com/Chenmo0414/win-encoding-fix)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell, PowerShell, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Windows-focused guidance for command-line behavior, file encoding, environment variables, and Git configuration.]

## Skill Version(s):

4.4.0 (source: server release evidence, SKILL.md frontmatter, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
