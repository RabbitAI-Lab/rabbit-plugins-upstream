## Description:

BidSketch lets an agent search and read BidSketch clients, proposals, and proposal content through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected BidSketch account use this skill to list and retrieve clients, proposals, proposal content, and client-specific proposals without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer one-liners that execute downloaded code.

Mitigation: Install the oo CLI from a verified, signed, or checksum-pinned source before using the BidSketch connector.

Risk: The skill accesses live BidSketch account data through an OOMOL-connected account.

Mitigation: Use an account with appropriate BidSketch access and review returned client and proposal data before sharing it outside the authorized workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bidsketch)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [BidSketch Homepage](https://www.bidsketch.com/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash and PowerShell command examples plus JSON payload and response conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only BidSketch connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
