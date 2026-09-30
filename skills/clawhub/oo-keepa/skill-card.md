## Description:

Keepa helps agents search and read Keepa product, seller, deal, category, token, and Amazon marketplace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, commerce analysts, and marketplace operators use this skill to query Keepa for Amazon product discovery, seller research, product snapshots, historical price and rank data, category lookup, deal lists, and token status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a remote installer command that could execute code on the user's machine.

Mitigation: Review official oo CLI installation documentation and verify the installer source before running shell or PowerShell install commands.

Risk: Keepa and OOMOL API calls may consume paid tokens.

Mitigation: Check token status and understand token costs before running token-expensive list, deal, or history actions.

## Reference(s):

- [Keepa homepage](https://keepa.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-keepa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides oo CLI connector schema and run commands; command results may return JSON data and execution metadata.]

## Skill Version(s):

1.0.4 (source: server release and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
