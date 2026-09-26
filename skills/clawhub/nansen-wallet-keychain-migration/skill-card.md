## Description:

Migrate an existing nansen-cli wallet from insecure password storage (env files, .credentials) to the new secure keychain-backed flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and wallet operators use this skill to migrate a nansen-cli wallet password from legacy file or environment storage into the OS keychain, then verify that the migrated password can decrypt the wallet without exposing key material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles wallet passwords and can involve legacy files that contain secrets.

Mitigation: Do not paste wallet passwords into chat; set them locally in the shell and avoid logging or storing them.

Risk: The `--reveal` verification step is high-risk because incorrect redirection could expose private key material.

Mitigation: Discard command output, rely only on the exit code, and prefer a safer password-check command if the CLI provides one.

Risk: Cleanup commands may remove `~/.nansen/.env`, which could contain values beyond the wallet password.

Mitigation: Inspect and back up the file before cleanup, and remove only the wallet-password entry when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-keychain-migration)
- [ClawHub Publisher Profile](https://clawhub.ai/user/nansen-devops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides command selection and verification; does not produce a persistent artifact.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
