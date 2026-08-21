## Description:

Generates strong passwords, alphanumeric passwords, numeric PINs, and memorable passphrases locally without network access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonyhuya](https://clawhub.ai/user/tonyhuya)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to generate local passwords, PINs, or passphrases for account setup and credential hygiene without sending secrets over the network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Passphrase mode uses a very small built-in word list, which can produce weaker passphrases for high-security accounts.

Mitigation: Prefer strong random password modes for important accounts, or expand the word list before relying on passphrases.

Risk: Generated passwords are printed to the terminal and may be exposed through terminal scrollback, screen sharing, or logs.

Mitigation: Run it in a private local terminal and move generated secrets directly into a password manager.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonyhuya/skills/password-gen)
- [Publisher profile](https://clawhub.ai/user/tonyhuya)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated credentials are emitted locally by the shell script; passphrase mode uses a small built-in word list.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
