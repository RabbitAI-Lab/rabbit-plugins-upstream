## Description:

BoxHero helps agents read BoxHero inventory, team, and location data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read BoxHero inventory items, location records, and linked team information from an OOMOL-connected BoxHero account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute changing code on a user's machine.

Mitigation: Use an independently verified OOMOL CLI installation path before running installer commands, and avoid repeating setup unless authentication or connection errors require it.

Risk: BoxHero data passes through OOMOL's connector service during use.

Mitigation: Install and use the skill only when the user trusts OOMOL's CLI distribution and connector service for the relevant BoxHero account data.

## Reference(s):

- [ClawHub BoxHero Skill](https://clawhub.ai/oomol/skills/oo-boxhero)
- [BoxHero Homepage](https://www.boxhero-app.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on live BoxHero connector schemas, authenticated OOMOL account state, and connected BoxHero permissions.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
