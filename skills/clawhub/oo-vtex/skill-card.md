## Description:

VTEX helps agents search and read VTEX catalog data through the OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to retrieve VTEX catalog products, brands, category trees, product and SKU IDs, and storefront search results through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly in a shell.

Mitigation: Review the oo CLI installation path before installing; prefer an official, version-pinned, checksum-verified installer or inspect the downloaded script before execution.

Risk: VTEX and OOMOL accounts may expose more access than needed for catalog lookup.

Mitigation: Connect accounts with the minimum scopes needed for read-only catalog work.

## Reference(s):

- [VTEX homepage](https://vtex.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vtex)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses and action schemas; current documented VTEX actions are read-only.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
