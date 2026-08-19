## Description:

Migrate an existing nansen-cli wallet from insecure password storage (env files, .credentials) to the new secure keychain-backed flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to assess an existing nansen-cli wallet password setup and migrate insecure password storage to the OS keychain-backed flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to verify migration with a command that may print wallet private keys into logs or transcripts.

Mitigation: Replace key-revealing verification with a non-secret unlock or decryption check before installation or use.

Risk: Credential-file reads and wallet password migration can expose sensitive wallet material if performed without explicit user approval.

Mitigation: Require explicit user approval before reading credential files or running commands that handle wallet passwords, and avoid echoing or logging secret values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-wallet-keychain-migration)
- [Publisher profile](https://clawhub.ai/user/nansen-devops)
- [nansen-cli package](https://www.npmjs.com/package/nansen-cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet-migration commands that act on local password storage.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
