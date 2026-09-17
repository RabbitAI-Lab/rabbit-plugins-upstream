## Description:

SellerSpace helps agents search and read SellerSpace data through the OOMOL `oo` CLI and connected SellerSpace account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SellerSpace-connected Amazon store, product, advertising, and FBA shipment data without handling raw SellerSpace credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI from verified official documentation or a pinned, checksum-verified release before using the skill.

Risk: Login and SellerSpace connection setup can attach an account to the connector.

Mitigation: Run login or connection setup only when you explicitly intend to connect that account, and otherwise use the installed and connected CLI directly.

## Reference(s):

- [ClawHub SellerSpace Skill](https://clawhub.ai/oomol/skills/oo-sellerspace)
- [SellerSpace Homepage](https://www.sellerspace.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SellerSpace query results as JSON returned by the `oo` CLI.]

## Skill Version(s):

1.0.2 (source: evidence.release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
