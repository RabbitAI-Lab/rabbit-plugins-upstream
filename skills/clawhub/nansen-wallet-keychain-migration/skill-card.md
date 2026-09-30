## Description:

Migrate an existing nansen-cli wallet from insecure password storage (env files, .credentials) to the new secure keychain-backed flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet users and developers use this skill to move existing nansen-cli wallet passwords from insecure files or environment storage into the OS keychain and verify the migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-assisted migration can expose wallet passwords through chat or access to plaintext credential files.

Mitigation: Enter passwords yourself in a local terminal; do not share passwords in chat or let an agent read plaintext files unless you understand the exposure risk.

Risk: Private-key reveal commands used for verification require particular care.

Mitigation: Prefer running private-key-related verification yourself locally; never display, log, or share the revealed keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nansen-devops/skills/nansen-wallet-keychain-migration)
- [Nansen CLI browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Migration steps and verification guidance; no wallet secrets are intended as output.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
