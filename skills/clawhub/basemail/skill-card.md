## Description:

BaseMail lets agents register a wallet-linked @basemail.ai address on Base, then send and read email using SIWE authentication and cached tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daaab](https://clawhub.ai/user/daaab)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use BaseMail to give agents a verifiable email identity, register or authenticate through wallet signing, and send and read confirmation email without human intervention.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Managed wallet setup can expose a full wallet recovery phrase in terminal output or logs.

Mitigation: Prefer a dedicated wallet with no funds or valuable permissions, avoid managed setup in logged non-interactive environments, and protect any recovery phrase as a secret.

Risk: Stored BaseMail tokens and encrypted private-key files can enable email access or wallet authentication if disclosed.

Mitigation: Protect ~/.basemail/token.json and private-key.enc as secrets, keep file permissions restricted, and exclude BaseMail state from version control or shared artifacts.

Risk: The skill can send and read email through the BaseMail API once credentials are configured.

Mitigation: Review recipients and message content before use in sensitive workflows, and rotate BaseMail tokens or API keys if they may have been exposed.

## Reference(s):

- [ClawHub BaseMail Skill](https://clawhub.ai/daaab/skills/basemail)
- [BaseMail Website](https://basemail.ai)
- [BaseMail API Documentation](https://api.basemail.ai/api/docs)
- [Base Names](https://www.base.org/names)
- [Base Chain](https://base.org)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and BaseMail credentials or a dedicated wallet identity for registration.]

## Skill Version(s):

1.9.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
