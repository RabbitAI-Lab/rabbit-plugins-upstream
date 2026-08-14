## Description:

加密文件 helps agents encrypt files, assess password security, manage key rotation, and review cryptographic practices for development and audit workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to handle file encryption workflows, evaluate password handling, manage key rotation records, and audit code for cryptographic practices. It is best suited to controlled workspaces where file writes, commands, plaintext, and keys can be reviewed before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle plaintext, encryption keys, encrypted outputs, file writes, and command execution without clearly documented limits.

Mitigation: Review proposed operations before execution, run only in a controlled workspace, and use non-production files unless command limits and key-handling expectations are clarified.

Risk: External API behavior and API key handling are not clearly specified.

Mitigation: Use scoped test credentials, avoid exposing production secrets, and confirm whether any external services receive plaintext, keys, file paths, or generated artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/encryption)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [JSON and Markdown guidance, with optional file artifacts, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include encrypted files, decryption credentials, password assessments, hashes, key-rotation records, and audit recommendations.]

## Skill Version(s):

1.0.1 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
