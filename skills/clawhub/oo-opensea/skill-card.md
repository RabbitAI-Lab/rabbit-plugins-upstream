## Description:

OpenSea (opensea.io) skill for searching and reading OpenSea data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search OpenSea and read NFT, collection, listing, offer, trait, and statistics data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute local code if run without verification.

Mitigation: Review setup before installation, prefer verified official releases or package-manager installation, and avoid allowing an agent to run remote installer commands automatically.

Risk: Future write or destructive OpenSea actions could change or remove account state if added to the connector.

Mitigation: Require explicit user confirmation of the exact payload, target, and expected effect before running any action tagged write or destructive.

## Reference(s):

- [OpenSea homepage](https://opensea.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-opensea)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include OpenSea connector results returned as JSON through the oo CLI.]

## Skill Version(s):

1.0.3 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
