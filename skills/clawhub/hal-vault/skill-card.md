## Description:

Securely store, search, and use secrets (API keys, tokens, passwords, SSH keys) with hal-vault, an SSH-key encrypted local secret store.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to store, find, rotate, and inject local credentials while keeping raw secret values out of chat, logs, and files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Real credentials may be exposed in command transcripts if secret values are pasted into visible shell command text.

Mitigation: Use the CLI's hidden prompt or protected stdin, keep displayed results masked, and reserve --reveal for command substitution only.

Risk: Installing or invoking an unpinned credential-handling binary can increase supply-chain risk.

Mitigation: Use a trusted, pinned hal-vault release and verify the artifact where possible before installation.

Risk: Vault material can be exposed if vault data and its SSH key are stored together or committed.

Mitigation: Use a dedicated vault-only SSH key, keep it outside the project tree, and exclude per-project vault directories from version control.

## Reference(s):

- [hal-vault ClawHub page](https://clawhub.ai/ofoxai/skills/hal-vault)
- [hal-vault skill homepage](https://github.com/ofoxai/skills/tree/main/skills/hal-vault)
- [hal-vault CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Raw secret values should remain masked in agent-visible output; revealed values are intended only for command substitution into another process.]

## Skill Version(s):

1.1.0 (source: server release metadata, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
