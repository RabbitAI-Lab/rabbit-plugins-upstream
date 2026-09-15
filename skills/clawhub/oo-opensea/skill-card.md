## Description:

Use this skill for OpenSea (opensea.io) requests that search and read marketplace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search OpenSea and read NFT, collection, listing, offer, trait, and account data through the OOMOL oo CLI with server-side managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands that could be unsafe if run automatically or without verification.

Mitigation: Review the OOMOL installation path before use; do not let an agent run curl-to-bash or irm-to-iex installers automatically, and prefer a verified installer with checksums or signatures.

Risk: Future write or destructive OpenSea actions could change account or marketplace state if added to the connector.

Mitigation: Require explicit user confirmation of the action, target, payload, and expected effect before any write or destructive action is run.

## Reference(s):

- [OpenSea homepage](https://opensea.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-opensea)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before command execution and returns OpenSea data through oo CLI responses.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
