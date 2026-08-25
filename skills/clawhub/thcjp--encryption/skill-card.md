## Description:

文件加密、密码安全、密钥管理、代码加密审计工具，帮助开发者处理文件加密、密码哈希验证、密钥轮换管理和代码加密实践审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to encrypt specified files, evaluate password security, manage key rotation, and review encryption practices for data protection and compliance workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may modify or replace files during encryption.

Mitigation: Provide only the exact file paths intended for encryption, confirm whether the result is written in place or as a new file, and keep backups of important files.

Risk: Secrets or unrelated API keys could be exposed through the agent environment.

Mitigation: Avoid placing unrelated API keys or secrets in the environment before running the skill.

Risk: Encryption outputs may be unusable if the key or decryption credential is lost.

Mitigation: Store encryption keys and decryption credentials in an approved secure location before relying on encrypted files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/encryption)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style summaries, with encrypted file outputs when file encryption is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include password strength assessments, hash values, key rotation records, compliance checks, and follow-up security recommendations.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
