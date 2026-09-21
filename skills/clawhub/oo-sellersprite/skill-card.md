## Description:

SellerSprite (sellersprite.com). Use this skill for SellerSprite requests that read, create, or update data through the OOMOL SellerSprite connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SellerSprite through an OOMOL-connected account, including API usage checks, ASIN detail lookup, competitor research, product research, and reverse ASIN keyword research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer one-liners that could execute changing code without integrity checks.

Mitigation: Do not let an agent run the remote installer automatically; install the oo CLI through trusted, versioned instructions with checksum or signature verification, then connect SellerSprite manually.

Risk: SellerSprite actions tagged as write can change data through the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before executing write actions, and inspect the live action schema before building a payload.

## Reference(s):

- [SellerSprite ClawHub Listing](https://clawhub.ai/oomol/skills/oo-sellersprite)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SellerSprite Homepage](https://www.sellersprite.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect live action schemas and run SellerSprite connector actions; write actions require user confirmation before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
