## Description:

SellerSprite (sellersprite.com). Use this skill for SellerSprite searching and data-reading requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve SellerSprite data for Amazon product research, ASIN details, competitor lookup, API usage, and reverse ASIN keyword analysis. The normal workflow inspects the live connector schema before running read-oriented SellerSprite actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include curl-to-bash and PowerShell iex installers that execute remotely downloaded code.

Mitigation: Review the installer source and trust boundary before running setup commands; use the normal read-only SellerSprite query workflow once the oo CLI and connection are already configured.

## Reference(s):

- [SellerSprite homepage](https://www.sellersprite.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub SellerSprite skill page](https://clawhub.ai/oomol/skills/oo-sellersprite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger oo CLI connector calls that return JSON data from SellerSprite.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
