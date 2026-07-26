## Description: <br>
Provides Windows command-line encoding and compatibility guidance for GBK/UTF-8, PowerShell and pwsh, Python, Node.js, Git, and code generation on Windows 10/11 with MSYS2 or Git Bash. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenmo0414](https://clawhub.ai/user/chenmo0414) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and coding agents use this skill to avoid garbled Windows shell output and to generate Python, Node.js, PowerShell, and Git commands that handle GBK and UTF-8 encoding correctly. It is most relevant for Windows 10/11 systems using MSYS2 or Git Bash. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional setup commands can persistently change Windows user environment variables, shell startup files, and global Git configuration. <br>
Mitigation: Review the setup commands before running them, apply them only to the intended Windows user account, and keep a plan to revert environment variables, ~/.bash_profile, ~/.bashrc, and global Git settings if they affect other tools. <br>
Risk: Using the wrong encoding for existing files or tool output can still produce corrupted text or misleading command results. <br>
Mitigation: Confirm whether each file or tool emits UTF-8, GBK/936, UTF-16, or raw bytes before applying conversion guidance, and test changes in a non-critical shell or repository first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenmo0414/skills/windows-shell) <br>
- [Project homepage from ClawHub metadata](https://github.com/Chenmo0414/win-encoding-fix) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell, PowerShell, Python, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows-specific guidance for command execution, file encoding, environment setup, and global Git configuration.] <br>

## Skill Version(s): <br>
4.2.0 (source: SKILL.md frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
