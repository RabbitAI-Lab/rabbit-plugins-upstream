## Description:

Taggun enables agents to inspect Taggun connector schemas and run receipt or invoice extraction, campaign listing, settings lookup, and validation actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Taggun receipt and invoice extraction, campaign ID listing, campaign settings lookup, and validation actions without handling raw Taggun API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run an unverified remote installer script on the user's machine.

Mitigation: Review or replace the installer with a verified package, or validate downloaded scripts with checksum or signature checks before execution.

Risk: Receipt or invoice URLs and Taggun campaign information are processed through OOMOL and Taggun.

Mitigation: Use approved public HTTPS URLs and confirm data-sharing expectations before running extraction or validation actions.

## Reference(s):

- [ClawHub Taggun Skill](https://clawhub.ai/oomol/skills/oo-taggun)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Taggun Homepage](https://www.taggun.io/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, json, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; command outputs include Taggun data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
