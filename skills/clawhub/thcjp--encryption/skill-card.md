## Description:

This skill helps agents encrypt files, assess password security, manage keys, and review code for cryptographic practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security-focused users can use this skill to guide file encryption, password security checks, key rotation planning, and cryptographic code review. It is intended for encryption-related data protection and audit workflows, not general system configuration or network administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed as an encryption helper, but the security evidence describes its instructions as broad and inconsistent.

Mitigation: Review each proposed operation before execution and grant file, command, or secret-handling access only when the requested action is clear.

Risk: Encryption, password, and key-management workflows can expose sensitive files, real keys, or passwords.

Mitigation: Use copies of important files, avoid sharing real secrets unless their handling is understood, and prefer documented local handling over external API use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/encryption)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON examples, shell commands, and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file operations, command execution, password checks, key handling steps, and audit findings for human review.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
