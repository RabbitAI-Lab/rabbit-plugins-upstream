## Description:

BAT/PowerShell 脚本踩坑经验库 helps developers troubleshoot Windows and Linux batch and PowerShell scripts, covering encoding, cmd syntax, PowerShell 5.1/7 compatibility, cross-platform pwsh behavior, and defensive security-tool scripting practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security-tool maintainers use this skill to diagnose BAT/PowerShell scripting failures, avoid Windows compatibility traps, and review defensive-tool implementation patterns with human oversight.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security verdict is suspicious because the skill includes anti-termination, kernel-driver, and AV-evasion-style guidance.

Mitigation: Install only for controlled defensive-tool development and require human review before applying process-protection, kernel-driver, or AV-sensitive guidance.

Risk: The artifact discusses changes to hosts files, services, Defender, firewall, test-signing, and similar system-level behavior.

Mitigation: Require clear user consent, backups, rollback steps, and manual approval before an agent applies those changes.

Risk: The artifact includes runnable command and scripting patterns that may affect Windows security tooling or system configuration.

Mitigation: Treat generated commands and code as proposals; review them in a controlled environment before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mowenqwq/skills/bat-ps1-dev)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline BAT, PowerShell, shell, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bilingual troubleshooting notes and safety review cautions.]

## Skill Version(s):

1.67.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
