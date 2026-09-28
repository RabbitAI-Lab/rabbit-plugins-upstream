## Description:

Migrate an existing nansen-cli wallet from insecure password storage (env files, .credentials) to the new secure keychain-backed flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet users and their agents use this skill to identify insecure password storage, migrate an existing nansen-cli wallet to the OS keychain, and check that the wallet remains accessible.

### Deployment Geography for Use:

Global; subject to applicable geographic and sanctions checks.

## Known Risks and Mitigations:

Risk: Wallet passwords could be exposed through chat, command text, or logs.

Mitigation: Use a local trusted CLI prompt or another non-logged secret entry path; never paste passwords into chat or include them in generated commands.

Risk: Private-key reveal or export during verification could disclose wallet keys.

Mitigation: Prefer a safer decrypt-only check; invoke private-key reveal or export only if the CLI offers no safer verification method.

## Reference(s):

- [Nansen Wallet Keychain Migration on ClawHub](https://clawhub.ai/nansen-devops/skills/nansen-wallet-keychain-migration)
- [ClawHub publisher profile: nansen-devops](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the nansen CLI and access to the existing wallet.]

## Skill Version(s):

0.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
