## Description:

This skill supports JumpServer searching and reading tasks through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to inspect JumpServer accounts, assets, asset nodes, permissions, terminal sessions, and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes unverified remote script execution for installing the oo CLI.

Mitigation: Prefer a verified, pinned, or manually reviewed oo CLI installer before using the skill.

Risk: The connector scope can expose JumpServer account, asset, permission, session, and user data visible to the configured token.

Mitigation: Use least-privilege JumpServer connection scopes and review connector access before installation.

Risk: The action surface may be broader than the read-only release description suggests.

Mitigation: Limit use to the listed read/list actions unless a separate reviewed workflow covers write or destructive actions.

## Reference(s):

- [ClawHub JumpServer skill](https://clawhub.ai/oomol/skills/oo-jumpserver)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [JumpServer homepage](https://www.jumpserver.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON from the oo CLI when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
