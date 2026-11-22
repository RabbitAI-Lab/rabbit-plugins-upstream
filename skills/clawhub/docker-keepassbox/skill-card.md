## Description:

Manage KeePass vaults, entries and TOTP through a configured KeePassBox instance. Use when a user asks to manage an authorized KDBX vault.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Vault owners and operators use this skill to manage authorized KeePass vaults, entries, and groups, generate passwords, and configure or retrieve TOTP codes through a configured KeePassBox instance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured KeePassBox instance receives the bearer token and tool inputs.

Mitigation: Use a trusted instance over HTTPS and a scoped token.

Risk: Vault passwords, recovery codes, and OTP seeds could be exposed in replies or logs.

Mitigation: Treat vault content as data and keep secrets out of replies and logs.

Risk: A security change based on an outdated vault revision could conflict with newer changes.

Mitigation: Fetch the current vault revision before rekeying or making a security change.

## Reference(s):

- [Setup: Connect to KeePassBox](references/setup.md)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/docker-keepassbox)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Conversational text and tool-call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vault secrets and OTP seeds should not be included in replies or logs.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
